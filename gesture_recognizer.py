import math

def _dist(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

def fingers_up(landmarks):
    tips = [4, 8, 12, 16, 20]
    pip = [3, 6, 10, 14, 18]
    res = []
    for t, p in zip(tips, pip):
        res.append(landmarks[t].y < landmarks[p].y)
    return res

def detect_gesture(landmarks):
    up = fingers_up(landmarks)
    if all(up[1:]) and up[0]:
        return 'open_palm'
    if not any(up):
        return 'fist'
    wrist = landmarks[0]
    thumb_tip = landmarks[4]
    if thumb_tip.x < wrist.x - 0.05:
        return 'thumb_left'
    if thumb_tip.x > wrist.x + 0.05:
        return 'thumb_right'
    return None
