import cv2
import os
import numpy as np
from tqdm import tqdm

def extract_frames(video_path, output_folder, num_frames=30):
    """Extract a fixed number of frames from a video file."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if total_frames <= 0:
        print(f"Warning: Could not read frames from {video_path}")
        cap.release()
        return False

    # Calculate indices for frames to extract
    indices = np.linspace(0, total_frames - 1, num_frames, dtype=int)
    
    count = 0
    success_count = 0
    for i in range(total_frames):
        ret = cap.grab()
        if not ret:
            break
        
        if i in indices:
            ret, frame = cap.retrieve()
            if ret:
                frame_path = os.path.join(output_folder, f"frame_{success_count:03d}.jpg")
                cv2.imwrite(frame_path, frame)
                success_count += 1
        
        if success_count >= num_frames:
            break

    cap.release()
    return success_count == num_frames

def process_all_videos(video_dir, frames_dir, num_frames=30):
    """Process all videos in the directory and extract frames."""
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)

    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.avi'))]
    print(f"Found {len(video_files)} videos to process.")

    for video_file in tqdm(video_files, desc="Extracting frames"):
        video_id = os.path.splitext(video_file)[0]
        video_path = os.path.join(video_dir, video_file)
        output_folder = os.path.join(frames_dir, video_id)
        
        # Skip if already processed
        if os.path.exists(output_folder) and len(os.listdir(output_folder)) >= num_frames:
            continue
            
        extract_frames(video_path, output_folder, num_frames)

if __name__ == "__main__":
    VIDEO_DIR = 'data/videos'
    FRAMES_DIR = 'data/frames'
    process_all_videos(VIDEO_DIR, FRAMES_DIR, num_frames=30)
