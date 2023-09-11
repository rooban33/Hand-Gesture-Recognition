import cv2
import numpy as np
import mediapipe as mp
import keyboard
import time
from tensorflow.keras.models import load_model

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
model_path = 'mp_hand_gesture'
model = load_model(model_path)

f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)
global cap 
cap = cv2.VideoCapture(0)

# Get the frame dimensions
ret, frame = cap.read()
x, y, c = frame.shape

use=0

while True:
    if cv2.waitKey(1) == ord('x'):
        break
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # print(result)
    
    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            # print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)
    if className=='fist' and use==1:
        use=0
    if use==0:
        if className =='rock':
            keyboard.press_and_release('up')
            use=1
        elif className =='thumbs up':
            keyboard.press_and_release('right')
            use=1
        elif className =='thumbs down':
            keyboard.press_and_release('left')
            use=1
        elif className =='stop' or className=='live long':
            keyboard.press_and_release('down')
            use=1

    # Show the final output
    cv2.imshow("Output", frame) 

# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()
