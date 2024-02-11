# Testing
All tests for the REST API used pytest and flask test client. 

I only tested routes that are related to the 2019 Dataset as testing all routes for every dataset is unncessary. They all have identical models, routes and schemas, therefore testing only the 2019 Dataset should be sufficient enough to know they all work.

### GET /dataset_2019
1. test_get_dataset_2019_status_code - Checks status code
2. test_get_dataset_2019_json - Checks response contains expected JSON

### GET /dataset_2019/<id>
1. test_get_specific_dataset_2019 - Checks response matches expected dataset 
2. test_get_dataset_2019_not_exists - Checks 404 returned for non-existent id

### POST /dataset_2019
1. test_post_dataset_2019 - Checks new dataset added and 201 returned
2. test_dataset_2019_post_error - Checks 400 returned for invalid data

### PATCH
1. test_patch_dataset_2019 - Checks dataset updated and 200 returned
2. test_patch_dataset_2019_not_exists - Checks 404 returned for updating a non-existent dataset

## DELETE
1. test_delete_dataset_2019 - Checks dataset deleted and 200 returned
2. test_delete_dataset_2019 - Checks 404 returned for deleting a non-existent dataset

![alt text](image.png)


