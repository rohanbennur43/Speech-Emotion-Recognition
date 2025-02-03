# Speech Emotion Recognition System

## Overview
This project is a Speech Emotion Recognition (SER) system developed during a research internship at Krushagramati Analytics. It leverages deep learning techniques to classify emotions from speech data, utilizing models such as Long Short-Term Memory (LSTM), Convolutional Neural Networks (CNN), and Capsule Networks. The system is designed to address hierarchical feature handling and enhance model generalization.

## Features
- **Deep Learning Models**: Implements LSTM, CNN, and Capsule Networks for feature extraction and classification.
- **Scalability & Performance**: Optimized for efficient computation with TensorFlow.
- **Backend**: Developed using Python Flask for API handling and model inference.
- **Frontend**: User-friendly interface built with React.js for real-time interaction.
- **Hierarchical Feature Handling**: Improves accuracy by capturing complex speech patterns.

## Technologies Used
- **Programming Languages**: Python, JavaScript
- **Deep Learning Framework**: TensorFlow
- **Backend Framework**: Flask (Python)
- **Frontend Framework**: React.js
- **Audio Processing**: Librosa, Numpy
- **Data Storage**: MongoDB (optional for storing inference results)

## Installation & Setup
### Prerequisites
Ensure the following dependencies are installed:
- Python 3.x
- TensorFlow
- Flask
- Librosa
- NumPy

## Usage
1. Upload an audio file through the React-based UI.
2. The backend processes the file and extracts features using deep learning models.
3. The predicted emotion is displayed on the frontend.

## Model Training
- The dataset is preprocessed using Librosa for feature extraction.
- Deep learning models are trained using TensorFlow with appropriate hyperparameter tuning.
- Capsule Networks are used to improve hierarchical feature learning.

## Future Enhancements
- Integration with real-time speech input.
- Improved accuracy using transformers.
- Deployment on cloud platforms for wider accessibility.

## Contributors
- **Rohan Bennur** - Research Intern, Krushagramati Analytics

## License
This project is licensed under the MIT License - see the LICENSE file for details.

