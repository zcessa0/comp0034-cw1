from flask import current_app as app

@app.route('/')
def hello():
  return f"Hello!"

from coursework1.schema import DatasetSchema
from coursework1.model import Dataset
from coursework1 import db

# Flask-Marshmallow Schemas
dataset_schema = DatasetSchema(many=True)

# Use route and specify the HTTP method(s). If you do not specify the methods then it will default to GET.
@app.route('/dataset', methods=['GET'])
def get_dataset():
    """Get all datasets"""
    # Get all the datasets from the database
    datasets = db.session.execute(db.select(Dataset)).scalars()
    # Serialize the queryset
    result = dataset_schema.dump(datasets)
    return {"datasets": result}

