"""
Record a short demo of the game + gesture control and convert to GIF.
- Press 'q' to stop recording.
- Generates demo.mp4 and demo.gif
"""

import cv2
import imageio

def record_demo():
    cap = cv2.VideoCapture(0)  # capture webcam
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("demo.mp4", fourcc, 20.0, (640, 480))
    
    print("🎥 Recording started. Press 'q' to stop.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        out.write(frame)
        cv2.imshow("Recording...", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("✅ Saved demo.mp4")

    # Convert to GIF
    print("Converting to demo.gif ...")
    reader = imageio.get_reader("demo.mp4")
    fps = reader.get_meta_data()["fps"]
    writer = imageio.get_writer("demo.gif", fps=fps)
    for frame in reader:
        writer.append_data(frame)
    writer.close()
    print("✅ Saved demo.gif")

if __name__ == "__main__":
    record_demo()
