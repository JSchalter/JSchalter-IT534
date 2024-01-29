from PIL import Image
from PIL import ExifTags
from PIL import ImageFont
from PIL import ImageDraw

my_image = Image.open("clancy_stuart.jpg")

print(my_image.size)
exif_data = {}
for key, value in my_image._getexif().items():
    if key in ExifTags.TAGS:
        exif_data[ExifTags.TAGS[key]] = value
# print(exif_data)

draw_text = ImageDraw.Draw(my_image)

# Change text size, style, and color
font_size = 36  # Change the font size
font_style = ImageFont.truetype("Syne-Regular.otf", font_size)
text_color = (0, 255, 0)

draw_text.text((0, 0), "Sample Text", text_color, font_style)
my_image.save("sample-output_files.jpg")
