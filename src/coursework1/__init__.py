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

    from coursework1.model import Dataset2019, Dataset2018, Dataset2017, Dataset2016, Dataset2015

        # If there are no datasets, then add them
    dataset_2019 = db.session.query(Dataset2019).first()
    if not dataset_2019:
        print("Start adding dataset data to the database")
        dataset_file = Path(__file__).parent.joinpath("data", "dataset_prepared.csv")
        with open(dataset_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                # Adjust the following based on your dataset model structure
                d = Dataset2019(
                    location=row[0],
                    ps_enroll_2019=row[1],
                    ps_eligible_2019=row[2],
                    sc_enroll_2019=row[4],
                    sc_eligible_2019=row[5],
                )
                db.session.add(d)
            db.session.commit()

    dataset_2018 = db.session.query(Dataset2018).first()
    if not dataset_2018:
        print("Start adding dataset data to the database")
        dataset_file = Path(__file__).parent.joinpath("data", "dataset_prepared.csv")
        with open(dataset_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                # Adjust the following based on your dataset model structure
                d = Dataset2018(
                    location=row[0],
                    ps_enroll_2018=row[7],
                    ps_eligible_2018=row[8],
                    sc_enroll_2018=row[10],
                    sc_eligible_2018=row[11],
                )
                db.session.add(d)
            db.session.commit()

    dataset_2017 = db.session.query(Dataset2017).first()
    if not dataset_2017:
        print("Start adding dataset data to the database")
        dataset_file = Path(__file__).parent.joinpath("data", "dataset_prepared.csv")
        with open(dataset_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                # Adjust the following based on your dataset model structure
                d = Dataset2017(
                    location=row[0],
                    ps_enroll_2017=row[13],
                    ps_eligible_2017=row[14],
                    sc_enroll_2017=row[16],
                    sc_eligible_2017=row[17],
                )
                db.session.add(d)
            db.session.commit()

    dataset_2016 = db.session.query(Dataset2016).first()
    if not dataset_2016:
        print("Start adding dataset data to the database")
        dataset_file = Path(__file__).parent.joinpath("data", "dataset_prepared.csv")
        with open(dataset_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                # Adjust the following based on your dataset model structure
                d = Dataset2016(
                    location=row[0],
                    ps_enroll_2016=row[19],
                    ps_eligible_2016=row[20],
                    sc_enroll_2016=row[22],
                    sc_eligible_2016=row[23],
                )
                db.session.add(d)
            db.session.commit()

    dataset_2015 = db.session.query(Dataset2015).first()
    if not dataset_2015:
        print("Start adding dataset data to the database")
        dataset_file = Path(__file__).parent.joinpath("data", "dataset_prepared.csv")
        with open(dataset_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                # Adjust the following based on your dataset model structure
                d = Dataset2015(
                    location=row[0],
                    ps_enroll_2015=row[25],
                    ps_eligible_2015=row[26],
                    sc_enroll_2015=row[28],
                    sc_eligible_2015=row[29],
                )
                db.session.add(d)
            db.session.commit()

