# Feel Heal: Mental Health Prediction Using Creative Industries Engagement

## Research Overview
This project investigates the effectiveness of creative and cultural industries in supporting individuals with psychological disorders and autism. Through machine learning and data analysis, the research aims to predict anxiety and depression levels while considering creative engagement factors.

## Research Objectives
1. Develop an accurate prediction model for anxiety and depression levels
2. Analyze the correlation between creative engagement and mental health
3. Provide data-driven insights for mental health support through creative industries
4. Evaluate the effectiveness of cultural activities in psychological well-being

## Dataset: RICH (Volume and Variety)

### Data Sources & Description

#### 1. Primary Health Metrics Dataset
- **Volume**: 10,000+ daily records
- **Timespan**: 2 years longitudinal data
- **Features**: 
  - Sleep patterns
  - Physical activity levels
  - Heart rate monitoring
  - Daily step counts
- **Collection**: Health monitoring devices
- **Format**: Structured CSV files

#### 2. Creative Engagement Data
- **Volume**: 8,000+ activity records
- **Categories**:
  - Visual arts participation
  - Music engagement
  - Dance activities
  - Theater attendance
  - Digital media creation
- **Metrics**: 
  - Engagement frequency
  - Session duration
  - Activity type classification

#### 3. Mental Health Assessments
- **Volume**: 15,000+ evaluations
- **Tools**: 
  - GAD-7 (Anxiety)
  - PHQ-9 (Depression)
- **Validation**: Professional clinical evaluations

## Technical Implementation

### Machine Learning Model
- Developed using scikit-learn
- Features engineered from health and creative engagement metrics
- Predictive analysis for anxiety and depression levels

### API Development
- FastAPI framework
- RESTful endpoints for predictions
- Data validation and error handling
- Swagger documentation

### Frontend Application
- Flutter-based implementation
- Health metrics input interface
- Prediction results visualization
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
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn main:app --host 0.0.0.0 --port 8001
```

2. Frontend Setup
```bash
cd feelhealmental
flutter pub get
flutter run
```

## Research Results

### Model Performance
- Accuracy metrics
- Validation results
- Feature importance analysis

### Key Findings
- Correlation between creative engagement and mental health
- Impact of various activities on anxiety/depression levels
- Effectiveness of predictive modeling

## Future Research Directions
1. Integration of additional creative industry metrics
2. Longitudinal study of intervention effectiveness
3. Expansion of prediction models
4. Integration with clinical assessment tools

## References
[Include your academic references here]

## Author
[Ssozi Jamillah]
[African Leadership University]
