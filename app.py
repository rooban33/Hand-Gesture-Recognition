# app.py (Flask application)
from flask import Flask, render_template, request, jsonify
import subprocess
import threading

app = Flask(__name__)
stop_recognition = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_gesture_recognition', methods=['POST'])
def start_gesture_recognition():
    global subprocess_obj
    subprocess_obj = subprocess.Popen(['python', 'project.py'])
    return jsonify({'message': 'Gesture recognition started'})

@app.route('/stop_gesture_recognition', methods=['POST'])
def stop_gesture_recognition():
    
    global subprocess_obj
    if subprocess_obj:
        # Terminate the subprocess
        subprocess_obj.terminate()
        subprocess_obj = None  # Clear the subprocess object
        return jsonify({'message': 'Gesture recognition stopping...'})
    else:
        return jsonify({'message': 'Gesture recognition not running'})
    
if __name__ == '__main__':
    app.run(debug=False)
