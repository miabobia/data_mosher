from PIL import Image
import os
from argparse import Namespace

def compare_color(color_a: tuple, color_b: tuple, threshold: int = 215) -> bool:
    # compares two colors
    # if the comparison is less than the threshold returns true because they are similar
    return abs(sum(color_a) - sum(color_b)) <= threshold

def mosh(saved_frame: Image, new_frame: Image) -> Image:
    pixels = new_frame.load()
    saved_pixels = saved_frame.load()
    for i in range(new_frame.size[0]):
        for j in range(new_frame.size[1]):
            if compare_color(pixels[i, j], saved_pixels[i, j]):
                pixels[i, j] = saved_pixels[i, j]

    return new_frame

def transform_frames(args: Namespace) -> None:
    
    extracted_frames = [f'{args.extracted_frames}/{frame}' for frame in os.listdir(args.extracted_frames)]
    total_frames = len(extracted_frames)
    saved_frame = ''

    for index, frame in enumerate(extracted_frames):
        im = Image.open(frame) # new image
        if index % args.mosh_rate == 0:
            saved_frame = im
        elif saved_frame:
            im = mosh(saved_frame, im)

        im.save(f'{args.transformed_frames}/frame-{index}.jpg')