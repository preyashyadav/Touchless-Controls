import cv2
import numpy as np

# define the hand gesture recognition function
def recognize_gesture(frame, hand_cascade):
    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect the hand in the frame using the hand cascade classifier
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)

    # check if a hand is detected
    if len(hands) > 0:
        # get the first detected hand
        (x, y, w, h) = hands[0]

        # draw a rectangle around the detected hand
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # perform a specific task based on the hand gesture
        if w > h:
            # horizontal hand gesture, perform task 1
            perform_task_1()
        else:
            # vertical hand gesture, perform task 2
            perform_task_2()

    # return the frame with the detected hand
    return frame

# define the function to perform task 1
def perform_task_1():
    # code to perform task 1
    pass

# define the function to perform task 2
def perform_task_2():
    # code to perform task 2
    pass

# initialize the hand cascade classifier
hand_cascade = cv2.CascadeClassifier('hand_cascade.xml')

# initialize the video capture object
cap = cv2.VideoCapture(0)

# start the video stream and detect hand gestures
while True:
    # read a frame from the video stream
    ret, frame = cap.read()

    # check if the frame was read successfully
    if not ret:
        break

    # detect the hand gesture and perform the corresponding task
    frame = recognize_gesture(frame, hand_cascade)

    # display the frame with the detected hand gesture
    cv2.imshow('Hand Gesture Detection', frame)

    # check for the 'q' key to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
