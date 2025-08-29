import json
import cv2
import mediapipe as mp
import pyautogui
from gesture_recognizer import detect_gesture
from gui import ControlGUI

class GestureController:
    def __init__(self, mapping_file='mapping.json'):
        with open(mapping_file, 'r') as f:
            self.mapping = json.load(f)
        self.running = False
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6)
        self.mp_draw = mp.solutions.drawing_utils

    def start(self):
        self.running = True
        self.cap = cv2.VideoCapture(0)
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)
            gesture = None
            if results.multi_hand_landmarks:
                handLms = results.multi_hand_landmarks[0]
                lm_list = [lm for lm in handLms.landmark]
                gesture = detect_gesture(lm_list)
                self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)
            cv2.putText(frame, f'Gesture: {gesture}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Hand Gesture Controller', frame)
            if gesture and gesture in self.mapping:
                key = self.mapping[gesture]
                pyautogui.press(key)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.running = False

if __name__ == '__main__':
    gui = ControlGUI()
    controller = GestureController()
    gui.start(controller)
