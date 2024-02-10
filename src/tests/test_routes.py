# note: these tests will be done for the 2019 dataset for simplicity
# the rest of the routes for the different datasets are the same and would be tested in the same way
def test_get_dataset_2019_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /dataset_2019
    THEN check the response is 200 OK
    """
    # Make a request to the /dataset_2019 route
    response = client.get('/dataset_2019')
    # Check that the response status code is 200
    assert response.status_code == 200

def test_get_dataset_2019_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data for dataset_2019
    WHEN a request is made to /dataset_2019
    THEN response should contain JSON
    AND a dataset for Barnet in 2019 should be in the JSON
    """
    # The dataset for Barnet in 2019
    barnet_dataset_2019 = {
      "id": 3,
      "location": "Barnet",
      "ps_eligible_2019": 4047,
      "ps_enroll_2019": 32368,
      "sc_eligible_2019": 3297,
      "sc_enroll_2019": 26481
    }
    # Make a request to the /dataset_2019 route
    response = client.get('/dataset_2019')
    # Check that the response contains JSON
    assert response.headers['Content-Type'] == 'application/json'
    # Check that the response contains the dataset for Barnet in 2019
    assert barnet_dataset_2019 in response.json['datasets']
    
def test_get_specific_dataset_2019(client):
    """
    GIVEN a Flask test client
    AND the 5th entry is Brent
    WHEN a request is made to /dataset_2019/5
    THEN the response json should match that for Brent
    AND the response status code should be 200
    """
    # The dataset for Brent in 2019
    brent_json = {
        "dataset": {
            "id": 5,
            "location": "Brent",
            "ps_eligible_2019": 3167,
            "ps_enroll_2019": 27902,
            "sc_eligible_2019": 2500,
            "sc_enroll_2019": 19846
        }
    }
    # Make a request to the /dataset_2019/5 route 
    response = client.get('/dataset_2019/5')
    # Check that the response contains JSON
    assert response.headers["Content-Type"] == "application/json"
    # Check that the response status code is 200
    assert response.status_code == 200
    # Check that the response contains the dataset for Brent in 2019
    assert response.json == brent_json

def test_get_dataset_2019_not_exists(client):
    """
    GIVEN a flask test client 
    WHEN a request is made for a dataset that does not exist
    THEN the response status code should be 404 Not Found
    """
    # Make a request to the /dataset_2019/100 route
    response = client.get('/dataset_2019/100')
    # Check that the response status code is 404
    assert response.status_code == 404

def test_post_dataset_2019(client):
    """
    GIVEN a Flask test client
    AND a valid JSON for a new dataset
    WHEN a POST request is made to /dataset_2019
    THEN a new dataset should be added to the database
    AND the response status code should be 201
    """
    # JSON to create a new dataset
    dataset_json = {
        "id": 46,
        "location": "Test",
        "ps_eligible_2019": 100,
        "ps_enroll_2019": 345,
        "sc_eligible_2019": 6780,
        "sc_enroll_2019": 8990
    }
    # Pass the JSON in the HTTP POST request
    response = client.post('/dataset_2019', json=dataset_json, content_type='application/json')
    # Check that the response status code is 201
    assert response.status_code == 201

def test_dataset_post_error(client):
    """
    GIVEN a Flask test client
    AND JSON for a new dataset that is missing a required field ("dataset")
    WHEN a post request is made to /dataset_2019
    THEN the response status code should be 400 Bad Request
    """
    # JSON to create a new dataset
    missing_dataset_json = {
        "ps_eligible_2019": 100,
        "ps_enroll_2019": 1000,
        "sc_eligible_2019": 100,
        "sc_enroll_2019": 1000
    }
    # Pass the JSON in the HTTP POST request
    response = client.post('/dataset_2019', json=missing_dataset_json)
    # Check that the response status code is 400
    assert response.status_code == 400

def test_patch_dataset_2019(client, new_dataset):
    """
    GIVEN an existing dataset
    AND a Flask test client
    WHEN an UPDATE request is made to /dataset_2019/45 with a new location
    THEN the response status code should be 200
    AND the response should include the message 'Dataset updated'
    """
    # The id of the new dataset
    dataset_id = new_dataset.id
    # The new location to update the dataset with
    new_dataset_info = {'ps_enroll_2019': 1500}
    # Make a request to the /dataset_2019/45 route with the new location
    response = client.patch(f'/dataset_2019/{dataset_id}', json=new_dataset_info)
    # Check that the response contains the message 'Dataset updated'
    assert response.json['message'] == 'Dataset updated'
    # Check that the response status code is 200
    assert response.status_code == 200

def test_delete_dataset_2019(client, new_dataset):
    """
    GIVEN an existing dataset
    AND a Flask test client
    WHEN a DELETE request is made to /dataset_2019/45
    THEN the response status code should be 200
    AND the response content should include the message 'Data deleted successfully from the 2019 database. ID: 45'
    """
    # The id of the new dataset
    dataset_id = new_dataset.id
    # Make a request to the /dataset_2019/45 route
    response = client.delete(f'/dataset_2019/{dataset_id}')
    # Check that the response contains the message 'Data deleted successfully from the 2019 database. ID: 45'
    expected_message = f"Data deleted successfully from the 2019 database. ID: {dataset_id}"
    assert response.json['message'] == expected_message
    # Check that the response status code is 200
    assert response.status_code == 200
    
