from flask import current_app as app

@app.route('/')
def hello():
  return f"Hello!"

from coursework1.schema import DatasetSchema2019, DatasetSchema2018
from coursework1.model import Dataset2019, Dataset2018
from coursework1 import db

# Flask-Marshmallow Schemas
datasets_schema_2019= DatasetSchema2019(many=True)
dataset_schema_2019= DatasetSchema2019()

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
def delete_data_2019():
   """ Deletes a dataset from the database
   
   Get the dataset from the database using the id and delete it from the database

   :returns: JSON """
   data = db.session.execute(db.select(Dataset2019).filter_by(id=id)).scalar_one_or_none()
   db.session.delete(data)
   db.session.commit()
   return {"message":f"Data deleted successfully from the 2019 database. ID: {data.id}"}

# Flask-Marshmallow Schemas
datasets_schema_2018= DatasetSchema2018(many=True)
dataset_schema_2018= DatasetSchema2018()

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

from flask import request

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

   


