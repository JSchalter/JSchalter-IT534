from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Open the XML file containing employee data
my_file = open("text_files/employee_data.xml", encoding="utf-8")
my_text = my_file.read()

# Remove non-ASCII characters from the file
encoded_string = my_text.encode("ascii", "ignore")
decode_string = encoded_string.decode()

# Create a BeautifulSoup object for parsing the XML
my_xml = BeautifulSoup(decode_string, "xml")

# Extract relevant data from the XML file
my_profiles = my_xml.find_all("profile_pic")
my_titles = my_xml.find_all("title")
my_phone_numbers = my_xml.find_all("phone")
my_names = my_xml.find_all("emp_name")

# Initialize empty lists to store extracted information
names = []
phone_numbers = []
profile_pics = []
titles = []

# Populate lists with data from XML tags
for name in my_names:
    names.append(name.get_text())
for title in my_titles:
    titles.append(title.get_text())
for phone_number in my_phone_numbers:
    phone_numbers.append(phone_number.get_text())
for my_profile in my_profiles:
    profile_pics.append(my_profile.get_text())

# Iterate through employee data and process images
for counter, value in enumerate(names):
    # Open the image file
    my_image = Image.open("images/" + profile_pics[counter])
    draw_text = ImageDraw.Draw(my_image)
    font = ImageFont.truetype("fonts/Syne-Regular.otf")

    # Add text to the image and save to the output_files folder
    draw_text.text((0, 0), names[counter] + "\n" + titles[counter] + "\n" + phone_numbers[counter] + "\n", (255, 0, 0), font)
    my_image.save("images/output_files/" + profile_pics[counter])
