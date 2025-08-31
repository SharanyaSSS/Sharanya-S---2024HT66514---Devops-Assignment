from ACEest_Fitnesss import app 

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness!" in response.data

