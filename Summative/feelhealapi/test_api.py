from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Mental Health Prediction API"}

def test_predict_valid_data():
    test_data = {
        "age": 30,
        "sleep_quality": 7.0,
        "daily_steps": 8000,
        "calories_burned": 2200.0,
        "physical_activity_level": 1,
        "heart_rate": 70,
        "social_interaction": 3,
        "medication_usage": 1,
        "sleep_duration": 7.0
    }
    
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["status"] == "success"
    assert data["message"] == "Prediction completed successfully"
    assert "data" in data
    
    prediction = data["data"]
    assert "anxiety_level" in prediction
    assert "depression_level" in prediction
    assert "contributing_factors" in prediction

def test_predict_invalid_data():
    # Test with invalid age
    invalid_data = {
        "age": 15,  # Age below minimum
        "sleep_quality": 7.0,
        "daily_steps": 8000,
        "calories_burned": 2200.0,
        "physical_activity_level": 1,
        "heart_rate": 70,
        "social_interaction": 3,
        "medication_usage": 1,
        "sleep_duration": 7.0
    }
    
    response = client.post("/predict", json=invalid_data)
    assert response.status_code == 422  # Validation error

def test_predict_missing_data():
    incomplete_data = {
        "age": 30,
        "sleep_quality": 7.0
        # Missing other required fields
    }
    
    response = client.post("/predict", json=incomplete_data)
    assert response.status_code == 422  # Validation error

def test_predict_out_of_range_values():
    out_of_range_data = {
        "age": 30,
        "sleep_quality": 11.0,  # Above maximum allowed value
        "daily_steps": 8000,
        "calories_burned": 2200.0,
        "physical_activity_level": 1,
        "heart_rate": 70,
        "social_interaction": 3,
        "medication_usage": 1,
        "sleep_duration": 7.0
    }
    
    response = client.post("/predict", json=out_of_range_data)
    assert response.status_code == 422  # Validation error
