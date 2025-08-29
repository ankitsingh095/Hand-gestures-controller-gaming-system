![Demo](demo.gif)

# Hand Gesture-Controlled Gaming System

**Tech**: Python, OpenCV, MediaPipe, PyAutoGUI, Pygame, Tkinter

Compact project demonstrating real-time hand gesture detection with MediaPipe and mapping gestures to keypresses.


# Hand Gesture-Controlled Gaming System

**Tech**: Python, OpenCV, MediaPipe, PyAutoGUI, Pygame, Tkinter

A compact project demonstrating real-time hand gesture detection (MediaPipe) and mapping recognized gestures to simulated keypresses to control a small game. Good for showcasing computer vision + simple HCI.

## Features
- Real-time webcam-based hand gesture recognition.
- Map simple gestures (open palm, fist, thumb-left, thumb-right) to keyboard keys.
- Small Pygame demo that responds to the simulated keys.
- Minimal GUI to start/stop recognition and switch mappings.

## Setup (Windows / Linux / Mac)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Usage
1. Run the demo game:
```bash
python game.py
```



2. In another terminal, start the gesture controller:
```bash
python main.py
```

Quit the gesture window with **q**.






# Hand gestures-controller gaming system
Hand Gesture-Controlled Gaming System using Python, OpenCV, and MediaPipe — play games with your hands instead of a keyboard.
