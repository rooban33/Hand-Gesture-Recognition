# Hand-Gesture-Recognition

This project is a gesture recognition application developed using Python, Flask, OpenCV, MediaPipe, and TensorFlow Keras. It allows users to control computer actions using hand gestures captured from a webcam.

## Prerequisites

- Python 3.x installed on your system
- Required Python libraries can be installed using `pip install -r requirements.txt`

## Getting Started

1. Clone the repository to your local machine:

    git clone <repository_url>
    

2. Install the required packages:

    pip install -r requirements.txt

3. Run the Flask application:

    python app.py

4. Access the application in your web browser at `http://localhost:5000`.

## Usage

- Open the application in your web browser.
- Click on the "Start Gesture Recognition" button to initiate gesture recognition.
- Perform gestures in front of your webcam, and the corresponding actions will be simulated on the computer.
- To stop gesture recognition, click on the "Stop Gesture Recognition" button.

## Gestures and Actions

- **Rock Gesture:** Move cursor up
- **Thumbs Up Gesture:** Move cursor right
- **Thumbs Down Gesture:** Move cursor left
- **Stop Gesture or Live Long Gesture:** Move cursor down
- **Fist Gesture:** No action

## Additional Notes

- Make sure your webcam is properly connected and functioning.
- Ensure proper lighting conditions for accurate gesture recognition.
- Press 'x' in the webcam window to exit the application.

## Dependencies

- Flask
- OpenCV
- MediaPipe
- TensorFlow
