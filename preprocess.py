import cv2
import os
from mtcnn import MTCNN
from tqdm import tqdm

# --- Configuration ---
# IMPORTANT: Update these paths to match your folder structure

# This should be the path to your folder of downloaded videos
VIDEO_ROOT = "E:/manipulated_sequences"

# This should point to the folder you just created
OUTPUT_PATH = "../Face-Dataset/preprocessed_faces"

REAL_FACES_PATH = os.path.join(OUTPUT_PATH, "real")
FAKE_FACES_PATH = os.path.join(OUTPUT_PATH, "fake")
FRAME_RATE = 30 # Process one frame every 30 frames (approx. 1 per second)

# --- Setup ---
# Initialize the MTCNN face detector
detector = MTCNN()

# Create output directories if they don't exist
os.makedirs(REAL_FACES_PATH, exist_ok=True)
os.makedirs(FAKE_FACES_PATH, exist_ok=True)

def process_video(video_path, output_dir):
    """
    Extracts, detects, and crops faces from a single video file.
    """
    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_face_count = 0
    
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break # End of video

        # Skip if frame is corrupted, unreadable, OR empty
        if frame is None or frame.size == 0:
            continue

        # Process one frame every FRAME_RATE frames
        if frame_count % FRAME_RATE == 0:
            # --- START OF THE TRY...EXCEPT BLOCK ---
            try:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = detector.detect_faces(frame_rgb)

                # Save the first detected face
                if results:
                    x1, y1, width, height = results[0]['box']
                    x1, y1 = abs(x1), abs(y1)
                    x2, y2 = x1 + width, y1 + height
                    face = frame[y1:y2, x1:x2]
                    
                    # Construct a unique filename
                    video_filename = os.path.basename(video_path).split('.')[0]
                    save_path = os.path.join(output_dir, f"{video_filename}_frame{frame_count}.jpg")
                    
                    # Resize face to a standard size, e.g., 224x224
                    resized_face = cv2.resize(face, (224, 224))
                    cv2.imwrite(save_path, resized_face)
                    saved_face_count += 1
            except Exception as e:
                # Catch any error during processing and just continue
                # This will prevent crashes from corrupted frames.
                continue
            # --- END OF THE TRY...EXCEPT BLOCK ---
        
        frame_count += 1
        
    video_capture.release()
    return saved_face_count


# --- Main Processing Loop ---
# Using the exact folder names from your screenshots.
folders_to_process = {
    # --- REAL Videos ---
    os.path.join(VIDEO_ROOT, "Deepfakes/original_sequences/actors/c23/videos"): REAL_FACES_PATH,
    os.path.join(VIDEO_ROOT, "Deepfakes/original_sequences/youtube/c23/videos"): REAL_FACES_PATH,

    # --- FAKE Videos ---
    os.path.join(VIDEO_ROOT, "Deepfakes/manipulated_sequences/DeepFakeDetection/c23/videos"): FAKE_FACES_PATH,
    os.path.join(VIDEO_ROOT, "Deepfakes/manipulated_sequences/Deepfakes/c23/videos"): FAKE_FACES_PATH,
}


print("--- Starting Preprocessing ---")
for video_folder, output_folder in folders_to_process.items():
    if not os.path.exists(video_folder):
        print(f"Warning: Folder not found, skipping: {video_folder}")
        continue
        
    print(f"\nProcessing folder: {video_folder}")
    video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]
    
    for video_name in tqdm(video_files, desc=f"Extracting faces"):
        video_path = os.path.join(video_folder, video_name)
        process_video(video_path, output_folder)

print("\n--- Preprocessing Complete ---")
print(f"Real faces saved to: {REAL_FACES_PATH}")
print(f"Fake faces saved to: {FAKE_FACES_PATH}")