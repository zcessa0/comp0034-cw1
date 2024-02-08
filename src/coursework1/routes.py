from flask import current_app as app
from coursework1.schemas import DatasetSchema


@app.route('/')
def hello():
  return f"Hello!"

# Flask-Marshmallow Schemas
dataset_schema = DatasetSchema()
datasets_schema = DatasetSchema(many=True)

# Use route and specify the HTTP method(s). If you do not specify the methods then it will default to GET.

