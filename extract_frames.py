# Placeholder for extract_frames.py
import cv2
import os

def extract_frames(video_path, output_dir='frames', interval_sec=1):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    count = 0
    frame_id = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % int(fps * interval_sec) == 0:
            frame_file = os.path.join(output_dir, f"frame_{frame_id}.jpg")
            cv2.imwrite(frame_file, frame)
            frame_id += 1
        count += 1
    cap.release()