# Testing
All tests for the REST API used pytest and flask test client. 

I only tested routes that are related to the 2019 Dataset as testing all routes for every dataset is unncessary. They all have identical models, routes and schemas, therefore testing only the 2019 Dataset should be sufficient enough to know they all work.

## How each route is tested twice:

### Get /dataset_2019
1. test_get_dataset_2019_status_code - Checks status code
2. test_get_dataset_2019_json - Checks response contains expected JSON

### Get /dataset_2019/<id>
1. test_get_specific_dataset_2019 - Checks response matches expected dataset 
2. test_get_dataset_2019_not_exists - Checks 404 returned for non-existent id
