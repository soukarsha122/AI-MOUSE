# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:33:13 2023

@author: SOUKARSHA
"""
import cv2
import mediapipe as mp
import pyautogui

camera = cv2.VideoCapture(0)
# detect refined landmarks
my_face = mp.solutions.face_mesh.FaceMesh(refine_landmarks=(True))
screen_width, screen_height = pyautogui.size()

while True:
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)
    # convert to rgb
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = my_face.process(frame)
    landmarks_points = output.multi_face_landmarks
    frame_height, frame_width, _ = frame.shape

    if landmarks_points:
        landmarks = landmarks_points[0].landmark

        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x*frame_width)
            y = int(landmark.y*frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = int(landmark.x*screen_width)
                screen_y = int(landmark.y*screen_height)
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x*frame_width)
            y = int(landmark.y*frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.009:
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow("Eye Mouse", frame)
    key_pressed = cv2.waitKey(1)
    if key_pressed == 113:
        break

camera.release()
cv2.destroyAllWindows()
