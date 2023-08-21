# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 23:42:52 2023

@author: SOUKARSHA
"""
import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

# detect hand
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # convert to rgb
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # process rgb frame using hand_detector
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # draw landmarks on hand in the frame
            drawing_utils.draw_landmarks(frame, hand)
            # get the landmarks list for the hand
            landmarks = hand.landmark
            # enumerate over the landmarks list .. this will return index (id),
            # value (landmark) pair
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                # create a yellow circle on the tip of the first finger
                if id == 8:
                    cv2.circle(img=frame, center=(x, y),
                               radius=10,  color=(0, 255, 255))
                    index_x = (screen_width/frame_width)*x
                    index_y = (screen_height/frame_height)*y
                    pyautogui.moveTo(index_x, index_y)
                # create a yellow circle on the tip of the thumb finger
                if id == 4:
                    cv2.circle(img=frame, center=(x, y),
                               radius=10,  color=(0, 255, 255))
                    thumb_x = (screen_width/frame_width)*x
                    thumb_y = (screen_height/frame_height)*y

                    if(abs(index_y-thumb_y) < 20):
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse', frame)

    key = cv2.waitKey(1)
    if key == 113:
        break

cap.release()
cv2.destroyAllWindows()
