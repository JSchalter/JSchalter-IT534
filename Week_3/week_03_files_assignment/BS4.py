from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

"""
Import necessary packages: BeautifulSoup from bs4, and Image, ImageFont, ImageDraw from PIL.
"""
my_file = open("text_files/employee_data.xml", encoding="utf-8")
my_text = my_file.read()

"""
Open and read the XML file, encoding it to utf-8.
"""
encoded_string = my_text.encode("ascii", "ignore")
decode_string = encoded_string.decode()

"""
Encode and decode the string to remove non-ASCII characters.
"""
my_xml = BeautifulSoup(decode_string, "xml")

"""
Create a BeautifulSoup instance with the decoded XML string.
"""

my_profiles = my_xml.find_all("profile_pic")
my_titles = my_xml.find_all("title")
my_phone_numbers = my_xml.find_all("phone")
my_names = my_xml.find_all("emp_name")

names = []
phone_numbers = []
profile_pics = []
titles = []

"""
Retrieve data from XML tags and store them in lists.
"""

for name in my_names:
    names.append(name.get_text())
for title in my_titles:
    titles.append(title.get_text())
for phone_number in my_phone_numbers:
    phone_numbers.append(phone_number.get_text())
for my_profile in my_profiles:
    profile_pics.append(my_profile.get_text())

"""
Iterate through XML data and populate lists.
"""

for counter, value in enumerate(names):
    my_image = Image.open("images/" + profile_pics[counter])
    draw_text = ImageDraw.Draw(my_image)
    font = ImageFont.truetype("fonts/Syne-Regular.otf")

    """
    Open each image, draw text using specified font, and save the modified image.
    """
    draw_text.text((0, 0), names[counter] + "\n" + titles[counter] + "\n" + phone_numbers[counter] + "\n", (255, 0, 0), font)
    my_image.save("images/output_files/" + profile_pics[counter])
