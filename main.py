#!/bin/python3
from PIL import Image, ImageDraw, ImageFont
import sys
# TODO: add error checking for all of these functions


def print_help_message():
    #  TODO: improve help message
    help_message = """usage: [text] [location of image] [optional output filename]\noutputs to output.jpeg"""
    print(help_message)
    exit()


def get_input():
    if len(sys.argv) > 0:
        if sys.argv[1] == "-h" or sys.argv[1] == "help":
            print_help_message()
        if len(sys.argv) == 3:
            return [sys.argv[1], sys.argv[2], "output.jpeg"]
        if len(sys.argv) > 3:
            return [sys.argv[1], sys.argv[2], sys.argv[3]]
    else:
        print_help_message()


def load_base_image(base_image_location):
    base_image = Image.open(base_image_location)
    return base_image


def write_name(base_image, text):
    d1 = ImageDraw.Draw(base_image)
    font = ImageFont.truetype("arial.ttf", 40)
    # This requires the arial.ttf file to be readable in this directory. This is because fonts are weird.
    d1.text((168, 436), text, fill=(0, 0, 0), font=font)


def scale_sub_image(sub_image_location):
    try:
        unscaled_sub_image = Image.open(sub_image_location)
    except FileNotFoundError:
        print("file not found")
        print_help_message()
        exit()
    if unscaled_sub_image.size[0] > unscaled_sub_image.size[1]:
        # width is greater than height
        new_height = round((unscaled_sub_image.size[1] / unscaled_sub_image.size[0]) * 230)
        return unscaled_sub_image.resize((230, new_height))
    else:
        # height is greater than width
        new_width = round((unscaled_sub_image.size[0] / unscaled_sub_image.size[1]) * 230)
        return unscaled_sub_image.resize((new_width, 230))


def paste_sub_image(base_image, scaled_sub_image):
    base_image.paste(scaled_sub_image, (300, 20))


def write_output_image(base_image, output_file_name):
    base_image.save(output_file_name)


def create_image(text, sub_image_location="pika.jpeg", output_location="output.jpeg"):
    base_image = load_base_image("base_image.jpeg")
    write_name(base_image, text)
    scaled_sub_image = scale_sub_image(sub_image_location)
    paste_sub_image(base_image, scaled_sub_image)
    write_output_image(base_image, output_location)


if __name__ == '__main__':
    inputs = get_input()
    text = inputs[0]
    sub_image_location = inputs[1]
    output_file_name = inputs[2]
    create_image(text, sub_image_location, output_file_name)
