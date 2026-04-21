import zipfile
import json
import os

zip_path = 'data/videos/data.zip'
extract_path = 'data'
subset_file = 'nslt_100.json'

def selective_extract():
    if not os.path.exists(zip_path):
        print(f"Error: {zip_path} not found.")
        return

    with zipfile.ZipFile(zip_path, 'r') as z:
        # Step 1: Extract the subset JSON if it fits in memory/root
        print(f"Extracting {subset_file}...")
        z.extract(subset_file, extract_path)
        
        subset_json_path = os.path.join(extract_path, subset_file)
        with open(subset_json_path, 'r') as f:
            subset_data = json.load(f)
        
        video_ids = set(subset_data.keys())
        print(f"Found {len(video_ids)} video IDs in {subset_file}.")
        
        # Step 2: Filter videos in zip
        all_files = z.namelist()
        videos_to_extract = [f for f in all_files if f.startswith('videos/') and f.split('/')[-1].split('.')[0] in video_ids]
        
        print(f"Extracting {len(videos_to_extract)} videos matching the subset...")
        
        extracted_count = 0
        for video_file in videos_to_extract:
            z.extract(video_file, extract_path)
            extracted_count += 1
            if extracted_count % 100 == 0:
                print(f"Extracted {extracted_count}/{len(videos_to_extract)}...")
        
        print(f"Successfully extracted {extracted_count} videos to {extract_path}/videos/")

if __name__ == "__main__":
    selective_extract()
