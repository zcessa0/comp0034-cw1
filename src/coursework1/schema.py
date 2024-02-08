from coursework1.model import Dataset2019, Dataset2018, Dataset2017, Dataset2016, Dataset2015
from coursework1 import ma, db

# Flask-Marshmallow Schemas
# See https://marshmallow-sqlalchemy.readthedocs.io/en/latest/#generate-marshmallow-schemas

class DatasetSchema2019(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of a dataset class. Inherits all the attributes from the Dataset class."""

    class Meta:
        model = Dataset2019
        # include_fk = True
        load_instance = True
        sqla_session = db.session
        # include_relationships = True

class DatasetSchema2018(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of a dataset class. Inherits all the attributes from the Dataset class."""

    class Meta:
        model = Dataset2018
        # include_fk = True
        load_instance = True
        sqla_session = db.session
        # include_relationships = True

class DatasetSchema2017(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of a dataset class. Inherits all the attributes from the Dataset class."""

    class Meta:
        model = Dataset2017
        # include_fk = True
        load_instance = True
        sqla_session = db.session
        # include_relationships = True

class DatasetSchema2016(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of a dataset class. Inherits all the attributes from the Dataset class."""

    class Meta:
        model = Dataset2016
        # include_fk = True
        load_instance = True
        sqla_session = db.session
        # include_relationships = True

class DatasetSchema2015(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of a dataset class. Inherits all the attributes from the Dataset class."""

    class Meta:
        model = Dataset2015
        # include_fk = True
        load_instance = True
        sqla_session = db.session
        # include_relationships = True

