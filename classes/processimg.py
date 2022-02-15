from PIL import Image, ImageFont, ImageDraw

class ProcessImg:

    def __init__(self, name = "My name", filename = "nature.jpeg"):
        self.name = name
        self.filename = filename
    
    def process_image(self):
        try:
            my_image = Image.open(self.filename)

            # ~ title_font = ImageFont.load_default()  # Fuente por defecto
            # ~ title_font = ImageFont.truetype('fonts/playfair-display/PlayfairDisplay-Black.ttf', 40)
            title_font = ImageFont.truetype('fonts/satisfy/Satisfy-Regular.ttf', 40)

            title_text = self.name

            image_editable = ImageDraw.Draw(my_image)

            image_editable.text((410,390), title_text, (255, 255, 255), font=title_font)

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
