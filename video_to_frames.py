import cv2 
import os 
from typing import List
from argparse import Namespace

def clean_output_dir(output_dir: str):
	file_list = os.listdir(output_dir)
	file_count = len(file_list)

	for filename in file_list:
		file_path = os.path.join(output_dir, filename)		
		if os.path.isfile(file_path):
			os.remove(file_path)

	return file_count

def extract_frames_from_video(video_path: str, index: int, args: Namespace):
	print(f'extracting frames from: {video_path}')
	cam = cv2.VideoCapture(video_path) 
	current_frame = 0

	while True:
		ret, frame = cam.read()

		if not ret: break

		video_width, video_height = args.dimensions
		resized_frame = cv2.resize(src=frame, dsize=(video_width, video_height), interpolation=cv2.INTER_AREA)
		name = f'{args.extracted_frames}/{index}-frame-{current_frame}.jpg'
		cv2.imwrite(name, resized_frame)
		current_frame += 1

	cam.release() 
	cv2.destroyAllWindows()

def extract_frames_from_directory(args: Namespace) -> List[str]:
	print(f'deleted {clean_output_dir(args.extracted_frames)} files from {args.extracted_frames}')
	print(f'deleted {clean_output_dir(args.transformed_frames)} files from {args.transformed_frames}')

	for index, video in enumerate(os.listdir(args.input_dir)):
		extract_frames_from_video(f'{args.input_dir}/{video}', index, args)