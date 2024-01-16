from colorthief import ColorThief
import matplotlib.pyplot as plt
from io import BytesIO
import requests
from PIL import Image
import io
# OK INCORPORATE THIS TO THE SHOE COLOUR ANALYZER

# Replace with your color representation and API endpoint



class ColorConverter:

    def __init__(self, list_of_shoes_urls):
        self.list_of_shoes_urls = list_of_shoes_urls

    def get_individual_colour(self, rgb_value):
        color_representation = f"rgb=rgb{rgb_value}"
        api_endpoint = "https://www.thecolorapi.com/id"

        # Make the request
        response = requests.get(f"{api_endpoint}?{color_representation}")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            color_info = response.json()
            print(color_info)

        else:
            print(f"Error: {response.status_code}")

    # Example: Extracting color name
        color_name = color_info["name"]["value"], (color_info['rgb']["r"], color_info['rgb']["g"], color_info['rgb']["b"])

        return color_name

    def get_all_colours(self):
            response = requests.get(self.list_of_shoes_urls)

            if response.status_code == 200:
                image_content = BytesIO(response.content)
                ct = ColorThief(image_content)
                dominant_color = ct.get_color(quality=1)
                #plt.imshow([[dominant_color]])
                #plt.show()

                palette = ct.get_palette(color_count=4)
                #plt.imshow([palette])
                #plt.show()

                list_of_colours = []

                for colour in palette:
                    shoe_colour = self.get_individual_colour(colour)
                    list_of_colours.append(shoe_colour)
            
        
                return list_of_colours
            
class File_ColorConverter:
    def __init__(self, file_content):
        self.file_content = file_content

    def get_most_prevalent_colors(self):
        # Create a BytesIO object to treat file_content as a file
        color_thief = ColorThief(io.BytesIO(self.file_content))

        # Get the palette (list of dominant colors)
        palette = color_thief.get_palette(color_count=4)

        return palette

