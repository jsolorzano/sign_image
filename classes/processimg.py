import requests
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw

class ProcessImg:

    def __init__(self, name = "My name", filename = "nature.jpeg"):
        self.name = name
        self.filename = filename
        self.url_file = 'https://www.proveyourworth.net/level3/img/proof.jpg'
    
    def file_exists(self):
        try:
            fileName = self.filename
            fileObj = Path(fileName)
            if fileObj.is_file():
                return True
            else:
                return False

        except Exception as err:
            print(err)
    
    def get_image(self):
        try:
            f = open(self.filename,'wb')
            response = requests.get(self.url_file)
            f.write(response.content)
            f.close()
            
            print("download successful")

        except Exception as err:
            print(err)
    
    def process_image(self):
        try:
            if not self.file_exists():
                self.get_image()

            my_image = Image.open(self.filename)

            # ~ title_font = ImageFont.load_default()  # Fuente por defecto
            # ~ title_font = ImageFont.truetype('fonts/playfair-display/PlayfairDisplay-Black.ttf', 40)
            title_font = ImageFont.truetype('fonts/satisfy/Satisfy-Regular.ttf', 40)

            title_text = self.name

            image_editable = ImageDraw.Draw(my_image)

            image_editable.text((300,220), title_text, (255, 255, 255), font=title_font)

            my_image.save("result.jpg")

            return True

        except Exception as err:
            print(err)
    
    def show_image(self):
        try:
            my_image = Image.open(self.filename)

            my_image.show()

        except Exception as err:
            print(err)
