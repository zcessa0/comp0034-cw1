from flask import current_app as app, request, abort, jsonify
from coursework1.schema import DatasetSchema2019, DatasetSchema2018, DatasetSchema2017, DatasetSchema2016, DatasetSchema2015
from coursework1.model import Dataset2019, Dataset2018, Dataset2017, Dataset2016, Dataset2015
from coursework1 import db
import logging
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError


@app.route('/')
def hello():
  return f"Hello!"


# Flask-Marshmallow Schemas
datasets_schema_2019= DatasetSchema2019(many=True)
dataset_schema_2019= DatasetSchema2019()

datasets_schema_2018= DatasetSchema2018(many=True)
dataset_schema_2018= DatasetSchema2018()

datasets_schema_2017= DatasetSchema2017(many=True)
dataset_schema_2017= DatasetSchema2017()

datasets_schema_2016= DatasetSchema2016(many=True)
dataset_schema_2016= DatasetSchema2016()

datasets_schema_2015= DatasetSchema2015(many=True)
dataset_schema_2015= DatasetSchema2015()

# ERROR HANDLING

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG

@app.errorhandler(404)
def resource_not_found(e):
    """Error handler for 404"""
    return jsonify(error=str(e)), 404

@app.errorhandler(ValidationError)
def register_validation_error(error):
    """Error handler for marshmallow schema validation errors"""
    response = error.messages 
    return response, 400

# 2019 ROUTES

# Use route and specify the HTTP method(s). If you do not specify the methods then it will default to GET.
# Returns a list of all datasets in JSON
@app.route('/dataset_2019', methods=['GET'])
def get_datasets_2019():
    """Returns a list of all datasets in the database in JSON."""
    try:
        datasets = db.session.execute(db.select(Dataset2019)).scalars()
        result = datasets_schema_2019.dump(datasets)
        return {"datasets": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")

# Returns a single dataset in JSON
@app.get('/dataset_2019/<id>')
def get_dataset_2019(id):
   """Returns the dataset with the specified id in JSON."""
   try:
      logging.debug(f"Attempting to retrieve dataset with ID: {id}")
      dataset = db.session.execute(db.select(Dataset2019).where(Dataset2019.id == id)).scalar_one_or_none()
      if dataset is None:
          logging.debug(f"No dataset found for ID: {id}")
          abort(404, description="Dataset not found")
      result = dataset_schema_2019.dump(dataset)
      return {"dataset": result}
   except SQLAlchemyError as e:
      logging.exception("An error occurred while querying the database")
      abort(404, description="Dataset not found.")

@app.post('/dataset_2019')
def add_data_2019():
    """ Adds a new dataset to the 2019 database."""
    try:
        dt_json = request.get_json()
        data = dataset_schema_2019.load(dt_json)
        db.session.add(data)
        db.session.commit()
        return {"message": f"Data added successfully to the 2019 database. ID: {data.id}"}, 201
    except ValidationError as e:
        logging.exception("Validation error occurred while adding data to the 2019 database")
        return {"error": str(e)}, 400


@app.delete('/dataset_2019/<int:id>')
def delete_data_2019(id):
    """ Deletes a dataset from the 2019 database."""
    try:
        data = db.session.execute(db.select(Dataset2019).filter_by(id=id)).scalar_one_or_none()
        if data is None:
            abort(404, description=f"Dataset with ID {id} not found")
        db.session.delete(data)
        db.session.commit()
        return {"message": f"Data deleted successfully from the 2019 database. ID: {data.id}"}, 200
    except SQLAlchemyError as e:
        logging.exception("An error occurred while deleting data from the 2019 database")
        abort(404, description="Dataset not found")

@app.patch('/dataset_2019/<id>')
def update_data_2019(id):
    """Updates changed fields for the 2019 dataset."""
    try:
        existing_data = db.session.execute(db.select(Dataset2019).filter_by(id=id)).scalar_one_or_none()
        if existing_data is None:
            abort(404, description="Dataset not found")
        data_json = request.get_json()
        data_updated = dataset_schema_2019.load(data_json, instance=existing_data, partial=True)
        db.session.add(data_updated)
        db.session.commit()
        updated_data = db.session.execute(db.select(Dataset2019).filter_by(id=id)).scalar_one_or_none()
        result = dataset_schema_2019.dump(updated_data)
        return jsonify({"message": "Dataset updated", "updated_data": result}), 200
    
    except ValidationError as e:
        logging.exception("Validation error occurred while updating data in the 2019 database")
        return {"error": str(e)}, 400
   

# 2018 ROUTES

# Define routes for 2018 datasets
@app.route('/dataset_2018', methods=['GET'])
def get_datasets_2018():
    """Returns a list of all datasets in the database for 2018."""
    try:
        datasets = db.session.execute(db.select(Dataset2018)).scalars()
        result = datasets_schema_2018.dump(datasets)
        return {"datasets": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")

@app.route('/dataset_2018/<id>', methods=['GET'])
def get_dataset_2018(id):
    """Returns the dataset with the specified id for 2018."""
    try:
        dataset = db.session.execute(db.select(Dataset2018).where(Dataset2018.id == id)).scalar_one_or_none()
        if dataset is None:
            logging.debug(f"No dataset found for ID: {id}")
            abort(404, description="Dataset not found")
        result = dataset_schema_2018.dump(dataset)
        return {"dataset": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")

@app.route('/dataset_2018', methods=['POST'])
def add_data_2018():
    """Adds a new dataset to the 2018 database."""
    try:
        dt_json = request.get_json()
        data = dataset_schema_2018.load(dt_json)
        db.session.add(data)
        db.session.commit()
        return {"message": f"Data added successfully to the 2018 database. ID: {data.id}"}, 201
    except ValidationError as e:
        logging.exception("Validation error occurred while adding data to the 2018 database")
        return {"error": str(e)}, 400

@app.route('/dataset_2018/<int:id>', methods=['DELETE'])
def delete_data_2018(id):
    """Deletes a dataset from the 2018 database."""
    try:
        data = db.session.execute(db.select(Dataset2018).filter_by(id=id)).scalar_one_or_none()
        if data is None:
            abort(404, description=f"Dataset with ID {id} not found")
        db.session.delete(data)
        db.session.commit()
        return {"message": f"Data deleted successfully from the 2018 database. ID: {data.id}"}, 200
    except SQLAlchemyError as e:
        logging.exception("An error occurred while deleting data from the 2018 database")
        abort(404, description="Dataset not found")
        
@app.patch('/dataset_2018/<id>')
def update_data_2018(id):
    """Updates changed fields for the 2018 dataset."""
    try:
        existing_data = db.session.execute(db.select(Dataset2018).filter_by(id=id)).scalar_one_or_none()
        if existing_data is None:
            abort(404, description="Dataset not found")
        data_json = request.get_json()
        data_updated = dataset_schema_2018.load(data_json, instance=existing_data, partial=True)
        db.session.add(data_updated)
        db.session.commit()
        updated_data = db.session.execute(db.select(Dataset2018).filter_by(id=id)).scalar_one_or_none()
        result = dataset_schema_2018.dump(updated_data)
        return jsonify({"message": "Dataset updated", "updated_data": result}), 200
    except ValidationError as e:
        logging.exception("Validation error occurred while updating data in the 2018 database")
        return {"error": str(e)}, 400

# Define routes for 2017 datasets
@app.route('/dataset_2017', methods=['GET'])
def get_datasets_2017():
    """Returns a list of all datasets in the database for 2017."""
    try:
        datasets = db.session.execute(db.select(Dataset2017)).scalars()
        result = datasets_schema_2017.dump(datasets)
        return {"datasets": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")

@app.route('/dataset_2017/<id>', methods=['GET'])
def get_dataset_2017(id):
    """Returns the dataset with the specified id for 2017."""
    try:
        dataset = db.session.execute(db.select(Dataset2017).where(Dataset2017.id == id)).scalar_one_or_none()
        if dataset is None:
            logging.debug(f"No dataset found for ID: {id}")
            abort(404, description="Dataset not found")
        result = dataset_schema_2017.dump(dataset)
        return {"dataset": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")


@app.route('/dataset_2017', methods=['POST'])
def add_data_2017():
    """Adds a new dataset to the 2017 database."""
    try:
        dt_json = request.get_json()
        data = dataset_schema_2017.load(dt_json)
        db.session.add(data)
        db.session.commit()
        return {"message": f"Data added successfully to the 2017 database. ID: {data.id}"}, 201
    except ValidationError as e:
        logging.exception("Validation error occurred while adding data to the 2017 database")
        return {"error": str(e)}, 400

@app.route('/dataset_2017/<int:id>', methods=['DELETE'])
def delete_data_2017(id):
    """Deletes a dataset from the 2017 database."""
    try:
        data = db.session.execute(db.select(Dataset2017).filter_by(id=id)).scalar_one_or_none()
        if data is None:
            abort(404, description=f"Dataset with ID {id} not found")
        db.session.delete(data)
        db.session.commit()
        return {"message": f"Data deleted successfully from the 2017 database. ID: {data.id}"}, 200
    except SQLAlchemyError as e:
        logging.exception("An error occurred while deleting data from the 2017 database")
        abort(404, description="Dataset not found")

@app.patch('/dataset_2017/<id>')
def update_data_2017(id):
    """Updates changed fields for the 2017 dataset."""
    try:
        existing_data = db.session.execute(db.select(Dataset2017).filter_by(id=id)).scalar_one_or_none()
        if existing_data is None:
            abort(404, description="Dataset not found")
        data_json = request.get_json()
        data_updated = dataset_schema_2017.load(data_json, instance=existing_data, partial=True)
        db.session.add(data_updated)
        db.session.commit()
        updated_data = db.session.execute(db.select(Dataset2017).filter_by(id=id)).scalar_one_or_none()
        result = dataset_schema_2017.dump(updated_data)
        return jsonify({"message": "Dataset updated", "updated_data": result}), 200
    except ValidationError as e:
        logging.exception("Validation error occurred while updating data in the 2017 database")
        return {"error": str(e)}, 400

# Define routes for 2016 datasets
@app.route('/dataset_2016', methods=['GET'])
def get_datasets_2016():
    """Returns a list of all datasets in the database for 2016."""
    try:
        datasets = db.session.execute(db.select(Dataset2016)).scalars()
        result = datasets_schema_2016.dump(datasets)
        return {"datasets": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")

@app.route('/dataset_2016/<id>', methods=['GET'])
def get_dataset_2016(id):
    """Returns the dataset with the specified id for 2016."""
    try:
        dataset = db.session.execute(db.select(Dataset2016).where(Dataset2016.id == id)).scalar_one_or_none()
        if dataset is None:
            logging.debug(f"No dataset found for ID: {id}")
            abort(404, description="Dataset not found")
        result = dataset_schema_2016.dump(dataset)
        return {"dataset": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")

@app.route('/dataset_2016', methods=['POST'])
def add_data_2016():
    """Adds a new dataset to the 2016 database."""
    try:
        dt_json = request.get_json()
        data = dataset_schema_2016.load(dt_json)
        db.session.add(data)
        db.session.commit()
        return {"message": f"Data added successfully to the 2016 database. ID: {data.id}"}, 201
    except ValidationError as e:
        logging.exception("Validation error occurred while adding data to the 2016 database")
        return {"error": str(e)}, 400

@app.route('/dataset_2016/<int:id>', methods=['DELETE'])
def delete_data_2016(id):
    """Deletes a dataset from the 2016 database."""
    try:
        data = db.session.execute(db.select(Dataset2016).filter_by(id=id)).scalar_one_or_none()
        if data is None:
            abort(404, description=f"Dataset with ID {id} not found")
        db.session.delete(data)
        db.session.commit()
        return {"message": f"Data deleted successfully from the 2016 database. ID: {data.id}"}, 200
    except SQLAlchemyError as e:
        logging.exception("An error occurred while deleting data from the 2016 database")
        abort(404, description="Dataset not found")

@app.patch('/dataset_2016/<id>')
def update_data_2016(id):
    """Updates changed fields for the 2016 dataset."""
    try:
        existing_data = db.session.execute(db.select(Dataset2016).filter_by(id=id)).scalar_one_or_none()
        if existing_data is None:
            abort(404, description="Dataset not found")
        data_json = request.get_json()
        data_updated = dataset_schema_2016.load(data_json, instance=existing_data, partial=True)
        db.session.add(data_updated)
        db.session.commit()
        updated_data = db.session.execute(db.select(Dataset2016).filter_by(id=id)).scalar_one_or_none()
        result = dataset_schema_2016.dump(updated_data)
        return jsonify({"message": "Dataset updated", "updated_data": result}), 200
    except ValidationError as e:
        logging.exception("Validation error occurred while updating data in the 2016 database")
        return {"error": str(e)}, 400

# Define routes for 2015 datasets
@app.route('/dataset_2015', methods=['GET'])
def get_datasets_2015():
    """Returns a list of all datasets in the database for 2015."""
    try:
        datasets = db.session.execute(db.select(Dataset2015)).scalars()
        result = datasets_schema_2015.dump(datasets)
        return {"datasets": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")

@app.route('/dataset_2015/<id>', methods=['GET'])
def get_dataset_2015(id):
    """Returns the dataset with the specified id for 2015."""
    try:
        dataset = db.session.execute(db.select(Dataset2015).where(Dataset2015.id == id)).scalar_one_or_none()
        if dataset is None:
            logging.debug(f"No dataset found for ID: {id}")
            abort(404, description="Dataset not found")
        result = dataset_schema_2015.dump(dataset)
        return {"dataset": result}
    except SQLAlchemyError as e:
        logging.exception("An error occurred while querying the database")
        abort(404, description="Dataset not found")

@app.route('/dataset_2015', methods=['POST'])
def add_data_2015():
    """Adds a new dataset to the 2015 database."""
    try:
        dt_json = request.get_json()
        data = dataset_schema_2015.load(dt_json)
        db.session.add(data)
        db.session.commit()
        return {"message": f"Data added successfully to the 2015 database. ID: {data.id}"}, 201
    except ValidationError as e:
        logging.exception("Validation error occurred while adding data to the 2015 database")
        return {"error": str(e)}, 400

@app.route('/dataset_2015/<int:id>', methods=['DELETE'])
def delete_data_2015(id):
    """Deletes a dataset from the 2015 database."""
    try:
        data = db.session.execute(db.select(Dataset2015).filter_by(id=id)).scalar_one_or_none()
        if data is None:
            abort(404, description=f"Dataset with ID {id} not found")
        db.session.delete(data)
        db.session.commit()
        return {"message": f"Data deleted successfully from the 2015 database. ID: {data.id}"}, 200
    except SQLAlchemyError as e:
        logging.exception("An error occurred while deleting data from the 2015 database")
        abort(404, description="Dataset not found")

@app.patch('/dataset_2015/<id>')
def update_data_2015(id):
    """Updates changed fields for the 2015 dataset."""
    try:
        existing_data = db.session.execute(db.select(Dataset2015).filter_by(id=id)).scalar_one_or_none()
        if existing_data is None:
            abort(404, description="Dataset not found")
        data_json = request.get_json()
        data_updated = dataset_schema_2015.load(data_json, instance=existing_data, partial=True)
        db.session.add(data_updated)
        db.session.commit()
        updated_data = db.session.execute(db.select(Dataset2015).filter_by(id=id)).scalar_one_or_none()
        result = dataset_schema_2015.dump(updated_data)
        return jsonify({"message": "Dataset updated", "updated_data": result}), 200
    except ValidationError as e:
        logging.exception("Validation error occurred while updating data in the 2015 database")
        return {"error": str(e)}, 400






   


