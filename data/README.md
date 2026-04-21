# ASL Recognition - Data Overview (Top 100 Signs)

This directory contains the dataset and metadata for the American Sign Language (ASL) recognition project, specifically filtered for the **Top 100 Signs** subset.

## Metadata Files
- **nslt_100.json**: The master configuration for the 100-sign subset.
  - Total IDs: 2,038
  - Format: `{"video_id": {"subset": "train/val/test", "action": [label, start, end]}}`
- **missing.txt**: Official list of video IDs that are unavailable in the source dataset (e.g., deleted from YouTube).
  - Note: 1,025 of the IDs in `nslt_100.json` are listed here and are not available locally.

## Data Directories
- **videos/**: Contains the raw `.mp4` video files.
  - Available videos: 1,013
  - Format: `video_id.mp4`
- **frames/**: Contains preprocessed frames extracted from the videos.
  - Total Processed: 1,013 videos
  *   **Frame Count**: 30 frames per video (where possible).
  *   **Format**: `data/frames/{video_id}/frame_{000-029}.jpg`

## Dataset Stats (Top 100 Subset)
- **Total Expected Videos**: 2,038
- **Successfully Preprocessed**: 1,013
- **Missing Videos (Official)**: 1,025
