from coursework1.model import Dataset
from coursework1 import ma, db

# Flask-Marshmallow Schemas
# See https://marshmallow-sqlalchemy.readthedocs.io/en/latest/#generate-marshmallow-schemas

class DatasetSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of a dataset class. Inherits all the attributes from the Dataset class."""

    class Meta:
        model = Dataset
        # include_fk = True
        load_instance = True
        sqla_session = db.session
        # include_relationships = True

