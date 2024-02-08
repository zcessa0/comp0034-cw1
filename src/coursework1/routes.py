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


   


