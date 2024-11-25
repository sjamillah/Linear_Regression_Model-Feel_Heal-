# Feel Heal: Mental Health Prediction System

## Project Overview
Feel Heal is a machine learning-based system designed to predict anxiety and depression levels using various health and lifestyle metrics. The system analyzes sleep patterns, physical activity, and other health indicators to provide early risk assessments for mental health conditions.

## Mission Statement
To create an accessible and accurate prediction system that helps identify potential mental health risks through the analysis of daily health metrics and lifestyle patterns.

## Project Aims
1. Develop an accurate prediction model for anxiety and depression risk levels
2. Identify key health indicators that correlate with mental health conditions
3. Create a user-friendly interface for health metric input and risk assessment
4. Provide data-driven insights for mental health monitoring

### Demo Video
[![Feel Heal Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

## Dataset Information

### Source
The Health and Sleep Statistics dataset was obtained from Kaggle:
[Health and Sleep Statistics Dataset](https://www.kaggle.com/datasets/hanaksoy/health-and-sleep-statistics)

### Dataset Description
A comprehensive health and sleep statistics dataset containing 100 records with various health metrics and lifestyle indicators.

#### Dataset Features:
1. **Demographic Information**
   - User ID
   - Age (Range: 22-50 years)
   - Gender (m/f)

2. **Sleep Metrics**
   - Sleep Quality (Scale: 1-10)
   - Bedtime (Time format: HH:MM)
   - Wake-up Time (Time format: HH:MM)

3. **Physical Activity Metrics**
   - Daily Steps (Range: 3000-11000)
   - Calories Burned (Range: 2000-2900)
   - Physical Activity Level (Categories: low, medium, high)

4. **Health Indicators**
   - Dietary Habits (Categories: healthy, medium, unhealthy)
   - Sleep Disorders (Binary: yes/no)
   - Medication Usage (Binary: yes/no)

### Dataset Statistics
```python
Total Records: 100
Features: 12
Missing Values: None
```

### Data Distribution
### Data Distribution Analysis

1. **Gender Distribution**
   - Female: 50 records (50%)
   - Male: 50 records (50%)

2. **Age Distribution**
   - Range: 22-50 years
   - Mean Age: ~35.5 years
   - Age Groups:
     * 20-30 years: ~35%
     * 31-40 years: ~35%
     * 41-50 years: ~30%

3. **Sleep Quality Distribution**
   - Range: 4-9 (on a scale of 1-10)
   - Distribution:
     * High Quality (8-9): ~40%
     * Medium Quality (6-7): ~30%
     * Low Quality (4-5): ~30%

4. **Physical Activity Level**
   - Low: 30 records (30%)
     * Average steps: ~3,000-4,000
     * Average calories: ~2,000-2,100
   - Medium: 40 records (40%)
     * Average steps: ~5,000-8,000
     * Average calories: ~2,200-2,400
   - High: 30 records (30%)
     * Average steps: ~8,500-11,000
     * Average calories: ~2,500-2,900

5. **Other Key Metrics**
   - Sleep Disorders: 
     * Yes: ~25%
     * No: ~75%
   - Medication Usage:
     * Yes: ~30%
     * No: ~70%
   - Dietary Habits:
     * Healthy: ~35%
     * Medium: ~25%
     * Unhealthy: ~40%

6. **Sleep Schedule**
   - Bedtime Range: 22:00-01:30
   - Wake-up Time Range: 06:00-07:30
   - Average Sleep Duration: ~7 hours

## Technical Implementation

### Machine Learning Model
- Developed using scikit-learn
- Feature engineering from health metrics
- Predictive analysis for anxiety and depression levels
- Model validation and testing

### API Development
- FastAPI framework
- RESTful endpoints
- Input validation
- Error handling
- Swagger documentation

### Frontend Application
- Flutter-based mobile application
- Health metrics input interface
- Risk assessment visualization
- User-friendly design

## API Documentation

### Base URL
```http
https://your-api-url
```

### Prediction Endpoint
```http
POST /predict

Request Body:
{
    "age": int,
    "sleep_quality": float,
    "daily_steps": int,
    "calories_burned": float,
    "physical_activity_level": int,
    "heart_rate": int,
    "social_interaction": int,
    "medication_usage": int,
    "sleep_duration": float
}
```

## Project Setup

### Prerequisites
- Python 3.9+
- Flutter SDK
- Required Python packages in requirements.txt

### Installation

1. Backend Setup
```bash
# Create virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn main:app --host 0.0.0.0 --port 8001
```

2. Frontend Setup
```bash
cd frontend
flutter pub get
flutter run
```

## Results

### Model Performance
- Prediction accuracy
- Validation metrics
- Feature importance rankings

### Key Findings
- Correlation between health metrics and mental health risks
- Important predictive factors
- Model reliability assessment

## Future Developments
1. Enhancement of prediction accuracy
2. Integration of additional health metrics
3. Real-time monitoring capabilities
4. Extended validation studies

## Author
[Jamillah Ssozi]
[African Leadership University]
