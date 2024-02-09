from flask import current_app as app

@app.route('/')
def hello():
  return f"Hello!"

from coursework1.schema import DatasetSchema2019, DatasetSchema2018, DatasetSchema2017, DatasetSchema2016, DatasetSchema2015
from coursework1.model import Dataset2019, Dataset2018, Dataset2017, Dataset2016, Dataset2015
from coursework1 import db

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

# 2019 ROUTES

# Use route and specify the HTTP method(s). If you do not specify the methods then it will default to GET.
# Returns a list of all datasets in JSON
@app.route('/dataset_2019', methods=['GET'])
def get_datasets_2019():
    """Returns a list of all datasets in the database in JSON."""
    # Get all the datasets from the database
    datasets = db.session.execute(db.select(Dataset2019)).scalars()
    # Serialize the queryset
    result = datasets_schema_2019.dump(datasets)
    return {"datasets": result}

# Returns a single dataset in JSON
@app.get('/dataset_2019/<id>')
def get_dataset_2019(id):
   """Returns the dataset with the specified id in JSON."""
   # Get the dataset from the database
   dataset = db.session.execute(db.select(Dataset2019).where(Dataset2019.id == id)).scalar_one_or_none()
   # Serialize the dataset
   result = dataset_schema_2019.dump(dataset)
   return {"dataset": result}

from flask import request

@app.post('/dataset_2019')
def add_data_2019():
   """ Adds a new dataset to the 2019 database

   Gets the JSON data from the request body and uses this to deserialise JSON to an object using Marshmallow 
   event_schema.load()

   :returns: JSON """
   dt_json = request.get_json()
   data = dataset_schema_2019.load(dt_json)
   db.session.add(data)
   db.session.commit()
   return {"message":f"Data added successfully to the 2019 database. ID: {data.id}"}


@app.delete('/dataset_2019/<int:id>')
def delete_data_2019(id):
   """ Deletes a dataset from the database
   
   Get the dataset from the database using the id and delete it from the database

   :returns: JSON """
   data = db.session.execute(db.select(Dataset2019).filter_by(id=id)).scalar_one_or_none()
   db.session.delete(data)
   db.session.commit()
   return {"message":f"Data deleted successfully from the 2019 database. ID: {data.id}"}

from flask import make_response

@app.patch('/dataset_2019/<id>')
def update_data_2019(id):
   """Updates changed fields for the dataset
   
   """
   # Find the data in the dataset
   exising_data = db.session.execute(db.select(Dataset2019).filter_by(id=id)).scalar_one_or_none()
   # Get the updated details from the json sent in the HTTP patch request
   data_json = request.get_json()
   # Use Marshmallow to update the exisiting data records with the changes from the JSON
   data_updated = dataset_schema_2019.load(data_json, instance=exising_data, partial=True)
   # Commit the changes to the database
   db.session.add(data_updated)
   db.session.commit()
   # Return JSON showing the updated record
   updated_data = db.session.execute(db.select(Dataset2019).filter_by(id=id)).scalar_one_or_none()
   result = dataset_schema_2019.dump(updated_data)
   response = make_response(result, 200)
   response.headers['Content-Type'] = 'application/json'

   return response   
   

# 2018 ROUTES

# Returns a list of all datasets in JSON
@app.route('/dataset_2018', methods=['GET'])
def get_datasets_2018():
    """Returns a list of all datasets in the database in JSON."""
    # Get all the datasets from the database
    datasets = db.session.execute(db.select(Dataset2018)).scalars()
    # Serialize the queryset
    result = datasets_schema_2018.dump(datasets)
    return {"datasets": result}

# Returns a single dataset in JSON
@app.get('/dataset_2018/<id>')
def get_dataset_2018(id):
   """Returns the dataset with the specified id in JSON."""
   # Get the dataset from the database
   dataset = db.session.execute(db.select(Dataset2018).where(Dataset2018.id == id)).scalar_one_or_none()
   # Serialize the dataset
   result = dataset_schema_2018.dump(dataset)
   return {"dataset": result}

@app.post('/dataset_2018')
def add_data_2018():
   """ Adds a new dataset to the database

   Gets the JSON data from the request body and uses this to deserialise JSON to an object using Marshmallow 
   event_schema.load()

   :returns: JSON """
   dt_json = request.get_json()
   data = dataset_schema_2018.load(dt_json)
   db.session.add(data)
   db.session.commit()
   return {"message":f"Data added successfully to the database. ID: {data.id}"}


@app.delete('/dataset_2018/<int:id>')
def delete_data_2018():
   """ Deletes a dataset from the database
   
   Get the dataset from the database using the id and delete it from the database

   :returns: JSON """
   data = db.session.execute(db.select(Dataset2018).filter_by(id=id)).scalar_one_or_none()
   db.session.delete(data)
   db.session.commit()
   return {"message":f"Data deleted successfully from the database. ID: {data.id}"}

# 2017 ROUTES

# Returns a list of all datasets in JSON
@app.route('/dataset_2017', methods=['GET'])
def get_datasets_2017():
    """Returns a list of all datasets in the database in JSON."""
    # Get all the datasets from the database
    datasets = db.session.execute(db.select(Dataset2017)).scalars()
    # Serialize the queryset
    result = datasets_schema_2017.dump(datasets)
    return {"datasets": result}

# Returns a single dataset in JSON
@app.get('/dataset_2017/<id>')
def get_dataset_2017(id):
   """Returns the dataset with the specified id in JSON."""
   # Get the dataset from the database
   dataset = db.session.execute(db.select(Dataset2017).where(Dataset2017.id == id)).scalar_one_or_none()
   # Serialize the dataset
   result = dataset_schema_2017.dump(dataset)
   return {"dataset": result}

@app.post('/dataset_2017')
def add_data_2017():
   """ Adds a new dataset to the database

   Gets the JSON data from the request body and uses this to deserialise JSON to an object using Marshmallow 
   event_schema.load()

   :returns: JSON """
   dt_json = request.get_json()
   data = dataset_schema_2017.load(dt_json)
   db.session.add(data)
   db.session.commit()
   return {"message":f"Data added successfully to the database. ID: {data.id}"}


@app.delete('/dataset_2017/<int:id>')
def delete_data_2017():
   """ Deletes a dataset from the database
   
   Get the dataset from the database using the id and delete it from the database

   :returns: JSON """
   data = db.session.execute(db.select(Dataset2017).filter_by(id=id)).scalar_one_or_none()
   db.session.delete(data)
   db.session.commit()
   return {"message":f"Data deleted successfully from the database. ID: {data.id}"}

# 2016 ROUTES

# Returns a list of all datasets in JSON
@app.route('/dataset_2016', methods=['GET'])
def get_datasets_2016():
    """Returns a list of all datasets in the database in JSON."""
    # Get all the datasets from the database
    datasets = db.session.execute(db.select(Dataset2016)).scalars()
    # Serialize the queryset
    result = datasets_schema_2016.dump(datasets)
    return {"datasets": result}

# Returns a single dataset in JSON
@app.get('/dataset_2016/<id>')
def get_dataset_2016(id):
   """Returns the dataset with the specified id in JSON."""
   # Get the dataset from the database
   dataset = db.session.execute(db.select(Dataset2016).where(Dataset2016.id == id)).scalar_one_or_none()
   # Serialize the dataset
   result = dataset_schema_2016.dump(dataset)
   return {"dataset": result}

@app.post('/dataset_2016')
def add_data_2016():
   """ Adds a new dataset to the database

   Gets the JSON data from the request body and uses this to deserialise JSON to an object using Marshmallow 
   event_schema.load()

   :returns: JSON """
   dt_json = request.get_json()
   data = dataset_schema_2016.load(dt_json)
   db.session.add(data)
   db.session.commit()
   return {"message":f"Data added successfully to the database. ID: {data.id}"}

@app.delete('/dataset_2016/<int:id>')
def delete_data_2016():
   """ Deletes a dataset from the database
   
   Get the dataset from the database using the id and delete it from the database

   :returns: JSON """
   data = db.session.execute(db.select(Dataset2016).filter_by(id=id)).scalar_one_or_none()
   db.session.delete(data)
   db.session.commit()
   return {"message":f"Data deleted successfully from the database. ID: {data.id}"}

# 2015 ROUTES

# Returns a list of all datasets in JSON
@app.route('/dataset_2015', methods=['GET'])
def get_datasets_2015():
    """Returns a list of all datasets in the database in JSON."""
    # Get all the datasets from the database
    datasets = db.session.execute(db.select(Dataset2015)).scalars()
    # Serialize the queryset
    result = datasets_schema_2015.dump(datasets)
    return {"datasets": result}

# Returns a single dataset in JSON
@app.get('/dataset_2015/<id>')
def get_dataset_2015(id):
   """Returns the dataset with the specified id in JSON."""
   # Get the dataset from the database
   dataset = db.session.execute(db.select(Dataset2015).where(Dataset2015.id == id)).scalar_one_or_none()
   # Serialize the dataset
   result = dataset_schema_2015.dump(dataset)
   return {"dataset": result}

@app.post('/dataset_2015')
def add_data_2015():
   """ Adds a new dataset to the database

   Gets the JSON data from the request body and uses this to deserialise JSON to an object using Marshmallow 
   event_schema.load()

   :returns: JSON """
   dt_json = request.get_json()
   data = dataset_schema_2015.load(dt_json)
   db.session.add(data)
   db.session.commit()
   return {"message":f"Data added successfully to the database. ID: {data.id}"}

@app.delete('/dataset_2015/<int:id>')
def delete_data_2015():
   """ Deletes a dataset from the database
   
   Get the dataset from the database using the id and delete it from the database

   :returns: JSON """
   data = db.session.execute(db.select(Dataset2015).filter_by(id=id)).scalar_one_or_none()
   db.session.delete(data)
   db.session.commit()
   return {"message":f"Data deleted successfully from the database. ID: {data.id}"}



   


