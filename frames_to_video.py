import cv2
import os
from argparse import Namespace


def compile_frames(args: Namespace):
    transformed_frames = [f'{args.transformed_frames}/{frame}' for frame in os.listdir(args.transformed_frames)]
    img = list(map(cv2.imread, [f for f in transformed_frames]))

    # ensure there are transformed images
    if not img:
        print("No images found!")
        return
    
    height, width, _ = img[0].shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(f'{args.output_video}.mp4', fourcc, args.fps, (width, height))

    for frame in img:
        video.write(frame)
    
    cv2.destroyAllWindows()
    video.release()