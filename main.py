import argparse
import os
from pathlib import Path
from video_to_frames import extract_frames_from_directory
import frames_to_video
import frame_transformer
from typing import Tuple


def validate_dir_files(path_str: str) -> bool:
    for file in os.listdir(path_str):
        if len(file) < 4 or file[len(file)-4:] != '.mp4':
            return False
    return True

def validate_fps(fps: int) -> bool:
    # ensure fps is greater than zero
    # currently no maximum fps limit
    return fps > 0

def validate_dimensions(dimensions: Tuple[int]) -> bool:
    # ensure dimensions are greater than zero and integers
    # currently no maximum dimension sizes
    return (
        dimensions[0] > 0 and
        dimensions[1] > 0 and
        int(dimensions[0]) == dimensions[0] and
        int(dimensions[1]) == dimensions[1]
        )

def resolve_path(path_str: str) -> bool:
    path = Path(path_str).resolve()
    return path

def parse_args():
    parser = argparse.ArgumentParser(
        description='Video glitch effect processor',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Required arguments
    parser.add_argument(
        '--input-dir',
        type=str,
        required=True,
        help='Directory containing input video files'
    )
    
    # Optional arguments
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./output',
        help='Directory for processed output files'
    )

    parser.add_argument(
        '--output-video',
        type=str,
        default='video',
        help='Name for output video [output-video].mp4'
    )

    parser.add_argument(
        '--dimensions',
        type=str,
        default='1920x1080',
        help='Output dimensions in format WIDTHxHEIGHT'
    )
    
    parser.add_argument(
        '--glitch-type',
        type=int,
        choices=[1, 2, 3],
        default=1,
        help='Type of glitch effect to apply (1, 2, or 3)'
    )
    
    parser.add_argument(
        '--fps',
        type=int,
        default=60,
        help='Output video frame rate'
    )

    parser.add_argument(
        '--mosh-rate',
        type=int,
        default=5,
        help='rate at which data moshing occurs'
    )

    args = parser.parse_args()

    # Resolve paths to absolute paths
    args.input_dir = resolve_path(args.input_dir)
    args.output_dir = resolve_path(args.output_dir)

    # raise error if:

    # dimensions are in invalid format
    try:
        width, height = map(int, args.dimensions.split('x'))
        args.dimensions = (width, height)
    except ValueError:
        raise ValueError(f'Invalid dimensions: {args.dimensions}. Dimensions must be integers in the format "WIDTHxHEIGHT"')

    # dimensions aren't greater than 0
    if not validate_dimensions(args.dimensions):
        raise ValueError(f"Dimensions must be greater than 0: {args.dimensions}")

    # input directory doesn't exist or is empty
    if not args.input_dir.is_dir():
        raise ValueError(f"Input directory does not exist: {args.input_dir}")
    
    # input directory is empty
    if not os.listdir(args.input_dir):
        raise ValueError(f"Input directory is empty: {args.input_dir}")
    
    # input directory has non mp4 files contained
    if not validate_dir_files(args.input_dir):
        raise ValueError(f"Input contains an invalid file(s): {args.input_dir}")

    # fps is greater than zero
    if not validate_fps(args.fps):
        raise ValueError(f"FPS is not greater than 0: {args.fps}")

    # mosh-rate is greater than zero
    if not validate_fps(args.mosh_rate):
        raise ValueError(f"FPS is not greater than 0: {args.mosh_rate}")

    # create output directory if doesn't exist
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    Path(f'{args.output_dir}/extracted_frames').mkdir(parents=True, exist_ok=True)
    Path(f'{args.output_dir}/transformed_frames').mkdir(parents=True, exist_ok=True)

    args.extracted_frames = f'{args.output_dir}/extracted_frames'
    args.transformed_frames = f'{args.output_dir}/transformed_frames'

    return args

def main():
    # parse arguments and ensure args are in correct format
    args = parse_args()

    print(f"Processing videos from: {args.input_dir}")
    print(f"Saving output to: {args.output_dir}")
    print(f"Saving extracted frames to output to: {args.extracted_frames}")
    print(f"Saving transformed frames to: {args.transformed_frames}")
    print(f"Output dimensions: {args.dimensions}")
    print(f"Using glitch type: {args.glitch_type}")
    print(f"Output FPS: {args.fps}")
    print(f"Output Video Name: {args.output_video}")
    print(f"Data mosh rate: {args.mosh_rate}")

    extract_frames_from_directory(args)
    frame_transformer.transform_frames(args)
    frames_to_video.compile_frames(args)

    # frame_transformer.main(args.output_dir, [5, 8, 100, 500], 't_frames')
    
    # # Your video processing code here...
    # if not DEBUG:
    #     # so i dont have to extract frames every time i test
    #     video_data = []

    #     for index, vid in enumerate(VIDEOS):
    #         clear_flag = False
    #         if index == 0:
    #             clear_flag = True
    #         video_to_frames.export(vid, FRAMES_DIR, index, V_WIDTH, V_HEIGHT, clear_flag)
    #         # video_data.append(FRAMES_DIR)
    #         print(f'{index} processing')

    # frame_transformer.main(FRAMES_DIR, [5, 8, 100, 500], TRANS_FRAMES_DIR)


    # frames_to_video.export(TRANS_FRAMES_DIR, STANDARD_FPS)

if __name__ == '__main__':
    main()

    # python uv package manager