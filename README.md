# Data Mosher

This project allows you to process video files, apply a data moshing glitch art effect, and export the processed result as a new video. The program supports extracting frames from video files, applies a data moshing effect to the frames and then compiling them back into a new video.

The following instructions will guide you through the installation and usage of this software.
Features

    Extract frames from video files.
    Compile transformed frames back into a video.
    Customizable output dimensions, frame rate, glitch types, and more.

## Requirements
    python = "3.13"
    opencv-python = "^4.10.0.84"
    pillow = "^11.0.0"

## Installation
    git clone https://github.com/miabobia/data_mosher.git

### Install the dependencies using Poetry:
    poetry install

## Usage
Run the script main.py to process your video files. The program requires an input directory with .mp4 video files, and it will generate an output directory containing the processed video files and frames.
Command Line Arguments

You can pass several options to customize the processing. Below are the available arguments:
Argument	Type	Default Value	Description
--input-dir	str	(Required)	Path to the directory containing .mp4 video files to process.
--output-dir	str	./output	Path to the directory where processed files (frames, videos) will be saved.
--output-video	str	video	The name for the output video file (without extension). The output will be [output-video].mp4.
--dimensions	str	1920x1080	Output video dimensions in WIDTHxHEIGHT format.

## Example Usage

python main.py --input-dir /path/to/your/videos --output-dir /path/to/output --output-video my_glitched_video --dimensions 1280x720 --fps 60 --mosh-rate 50

## Output

The program will:

    Extract frames from all .mp4 files in the input directory.
    Data mosh all the extracted frames
    Save the processed frames to the output-dir under the transformed_frames directory.
    Compile the transformed frames back into a video and save it with the provided name in the specified output directory.

The final video will be named [output-video].mp4, and it will be located in the output-dir specified.

## Troubleshooting

    Error: "Input directory does not exist": Ensure that the input directory exists and is correctly specified.
    Error: "Invalid dimensions": Check that you have entered valid dimensions in the format WIDTHxHEIGHT, where both width and height are integers.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
