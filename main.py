#!/bin/python3
from PIL import Image, ImageDraw, ImageFont
import sys
# TODO: add error checking for all of these functions


def print_help_message():
    #  TODO: improve help message
    help_message = """usage: [text] [location of image]\noutputs to output.jpeg"""
    print(help_message)
    exit()


def get_input():
    #  TODO: add an optional parameter to set the output location
    if len(sys.argv) > 0:
        if sys.argv[1] == "-h" or sys.argv[1] == "help":
            print_help_message()
        if len(sys.argv) > 2:
            return [sys.argv[1], sys.argv[2]]
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
    scaled_sub_image = unscaled_sub_image.resize((230, 230))  # TODO: improve this to work better with non-square images
    return scaled_sub_image  # now scaled to 230 by 230, this is about right for our background image


def paste_sub_image(base_image, scaled_sub_image):
    base_image.paste(scaled_sub_image, (300, 20))


def write_output_image(base_image):
    base_image.save("output.jpeg")


if __name__ == '__main__':
    inputs = get_input()
    text = inputs[0]
    sub_image_location = inputs[1]
    base_image = load_base_image("base_image.jpeg")
    write_name(base_image, text)
    scaled_sub_image = scale_sub_image(sub_image_location)
    paste_sub_image(base_image, scaled_sub_image)
    write_output_image(base_image)
