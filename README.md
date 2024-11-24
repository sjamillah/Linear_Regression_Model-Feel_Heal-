# Feel Heal - Mental Health Prediction App

[![Watch the demo](https://img.youtube.com/vi/YOUR_YOUTUBE_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_YOUTUBE_VIDEO_ID)

## 🚀 Live Demo
- Mobile App
- API Documentation: [API Docs](your-api-url/docs)
- Design Prototype: [Figma Design](https://www.figma.com/design/8KZoT9tvQNFQPdTGCoUyk2/Feel-%26-Heal?node-id=0-1&t=kQJv3Sp3UJQPkGFa-1)

## 📝 Description
Feel Heal is a mental health prediction application that helps users monitor and assess their mental well-being based on various lifestyle and health metrics. Using machine learning, the app provides personalized insights about potential anxiety and depression risks.

## ✨ Features
- **Health Metrics Analysis**: Track daily activities, sleep patterns, and social interactions
- **Risk Assessment**: Get personalized anxiety and depression risk evaluations
- **Confidence Scores**: Understand the reliability of predictions
- **Contributing Factors**: Identify lifestyle elements affecting mental health
- **Personalized Recommendations**: Receive tailored suggestions for improvement

## 🛠️ Technical Stack
### Frontend
- Flutter/Dart
- Material Design
- State Management: [Your State Management Solution]

### Backend
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Joblib

## 📋 API Documentation
Our API provides comprehensive endpoints for mental health prediction:

### Base URL
```
https://your-api-url.com
```

### Endpoints

#### Health Check
```http
GET /health
```

#### Predict Mental Health
```http
POST /predict
```

Request Body Example:
```json
{
    "age": 30,
    "sleep_quality": 7.5,
    "daily_steps": 8000,
    "calories_burned": 2200.5,
    "physical_activity_level": 1,
    "heart_rate": 70,
    "social_interaction": 3,
    "medication_usage": 1,
    "sleep_duration": 7.5
}
```

For detailed API documentation, visit our [Swagger UI](your-api-url/docs) or [ReDoc](your-api-url/redoc).

## 🎨 Design
Our user interface was carefully crafted to provide a comfortable and intuitive experience:

- [View Figma Prototype](your-figma-url)
- [Design System Documentation](your-design-docs-url)

### Design Features
- Accessible color schemes
- Intuitive navigation
- Responsive layouts
- Clear data visualization

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Flutter 3.0+
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/feel-heal.git
cd feel-heal
```

2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

3. Frontend Setup
```bash
cd frontend
flutter pub get
flutter run
```

## 📱 Mobile App Features
- Real-time health metrics tracking
- Intuitive data input
- Visualization of prediction results
- Progress tracking
- Personalized recommendations

## 💡 Future Improvements
- [ ] Advanced data analytics
- [ ] Social support features
- [ ] Integration with health devices
- [ ] Expanded mental health resources
- [ ] Community features

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributors
- sjamillah

## 📞 Support
For support, email [support@feelheal.com](mailto:support@feelheal.com) or join our [Discord community](discord-invite-link).

## 🙏 Acknowledgments
- Mental Health Resources
- Design Inspiration
- Open Source Communities
- [List any other acknowledgments]

---

Made with ❤️ by Jamillah Ssozi
