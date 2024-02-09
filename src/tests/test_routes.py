# note: these tests will be done for the 2019 dataset for simplicity
# the rest of the routes for the different datasets are the same and would be tested in the same way
def test_get_dataset_2019_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /dataset_2019
    THEN check the response is 200 OK
    """
    response = client.get('/dataset_2019')
    assert response.status_code == 200

def test_get_dataset_2019_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data for dataset_2019
    WHEN a request is made to /dataset_2019
    THEN response should contain json
    AND a dataset for Barent in 2019 should be in the JSON
    """
    response = client.get('/dataset_2019')
    assert response.headers['Content-Type'] == 'application/json'
    barent_dataset_2019 = {
        "location": "Barent",
        "ps_enroll_2019": 32368,
        "ps_eligible_2019": 4047,
        "sc_enroll_2019": 32368,
        "sc_eligible_2019": 3297

    }
    assert barent_dataset_2019 in response.json

def test_get_specific_dataset_2019(client):
    """
    GIVEN a Flask test client
    AND the 5th entry is Brent
    WHEN a request is made to /dataset_2019/5
    THEN the response json should match that for Brent
    AND the response status code should be 200
    """
    brent_json = {
        "location": "Brent",
        "ps_enroll_2019": 27902,
        "ps_eligible_2019": 3167,
        "sc_enroll_2019": 19846,
        "sc_eligible_2019": 2500

    }
    response = client.get('/dataset_2019/5')
    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert response.json == brent_json

    def test_get_dataset_2019_not_exists(client):
        """
        GIVEN a flask test client 
        WHEN a request is made for a dataset that does not exist
        THEN the response status code should be 404 Not Found
        """
        response = client.get('/dataset_2019/100')
        assert response.status_code == 404