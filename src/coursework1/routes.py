from flask import current_app as app

@app.route('/')
def hello():
  return f"Hello!"

from coursework1.schema import DatasetSchema
from coursework1.model import Dataset
from coursework1 import db

# Flask-Marshmallow Schemas
datasets_schema = DatasetSchema(many=True)
dataset_schema = DatasetSchema()

# Use route and specify the HTTP method(s). If you do not specify the methods then it will default to GET.
# Returns a list of all datasets in JSON
@app.route('/dataset', methods=['GET'])
def get_datasets():
    """Returns a list of all datasets in the database in JSON."""
    # Get all the datasets from the database
    datasets = db.session.execute(db.select(Dataset)).scalars()
    # Serialize the queryset
    result = datasets_schema.dump(datasets)
    return {"datasets": result}

# Returns a single dataset in JSON
@app.get('/dataset/<id>')
def get_dataset(id):
   """Returns the dataset with the specified id in JSON."""
   # Get the dataset from the database
   dataset = db.session.execute(db.select(Dataset).where(Dataset.id == id)).scalar_one_or_none()
   # Serialize the dataset
   result = dataset_schema.dump(dataset)
   return {"dataset": result}

   


