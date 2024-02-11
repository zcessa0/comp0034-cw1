import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
import logging
from logging.config import dictConfig
import csv
from pathlib import Path

class Base(DeclarativeBase):
    pass

# Initialise the database
db = SQLAlchemy(model_class=Base)
ma = Marshmallow()

# Create the Flask app
def create_app(test_config=None):
    logging.basicConfig(filename='couresework1_error.log', level=logging.DEBUG)
    # create the Flask app
    app = Flask(__name__, instance_relative_config=True)

    # configure the Flask app 
    app.config.from_mapping(
        SECRET_KEY='v0Ues_DPFLSkik0Y6UWGFA',
        # Set the location of the database file called fsm.sqlite which will be in the app's instance folder
        SQLALCHEMY_DATABASE_URI= "sqlite:///" + os.path.join(app.instance_path, 'coursework1.sqlite'),  
    )


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialise Flask with the SQLAlchemy database extension
    db.init_app(app)
    # Create a global Flask-Marshmallow object
    ma.init_app(app)
    
    # Models are defined in the models module, so you must import them before calling create_all, otherwise SQLAlchemy
    # will not know about them.
    from coursework1.model import Dataset2019, Dataset2018, Dataset2017, Dataset2016, Dataset2015

    # Create the tables in the database
    with app.app_context():
        db.create_all() # Create the database and tables if they don't already exist
        add_data_from_csv(app) # Add data to the database if it does not already added
        from coursework1 import routes # Add data to the database if it does not already added

    # Configure logging
    dictConfig({
        'version': 1.0,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "coursework1_log.log",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["wsgi", "file"]},
    })

    app.logger.info('The app is starting...')
        
    return app


from coursework1.model import Dataset2019, Dataset2018, Dataset2017, Dataset2016, Dataset2015
# Function to add data from CSV file
def add_data_from_csv(app):
    """Adds data to the database if it does not already exist."""
    datasets = [(Dataset2019, slice(0, 6)), (Dataset2018, slice(6, 12)), (Dataset2017, slice(12, 18)),
                (Dataset2016, slice(18, 24)), (Dataset2015, slice(24, 30))]
    
    for dataset_class, columns_slice in datasets:
        dataset = db.session.query(dataset_class).first()
        if not dataset:
            app.logger.info(f"Start adding {dataset_class.__name__} data to the database")
            dataset_file = Path(__file__).parent.joinpath("data", "dataset_prepared.csv")
            with open(dataset_file, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip header row
                for row in csv_reader:
                    d = dataset_class(
                        location=row[columns_slice.start],
                        ps_enroll=row[columns_slice.start + 1],
                        ps_eligible=row[columns_slice.start + 2],
                        sc_enroll=row[columns_slice.start + 3],
                        sc_eligible=row[columns_slice.start + 4]
                    )
                    db.session.add(d)
                db.session.commit()

