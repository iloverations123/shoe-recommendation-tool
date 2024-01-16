from rembg import remove
import os


def process_images_in_directory(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            remove_background(input_path, output_path)


def remove_background(input_path, output_path):
    with open(input_path, "rb") as input_file:
        input_data = input_file.read()
    
    output_data = remove(input_data)

    with open(output_path, "wb") as output_file:
        output_file.write(output_data)

input_image_path = "C:/Users/benel/Downloads/shoes/images/raw"
output_image_path = "C:/Users/benel/Downloads/shoes/images/processed"

process_images_in_directory(input_image_path, output_image_path)



