# Imports
import imgbbpy
from PIL import ImageGrab, Image
import pyperclip

# Save image
img = ImageGrab.grabclipboard()
if isinstance(img, Image.Image):
    img.save('img.png')

# Send photo
client = imgbbpy.SyncClient('API-KEY')  # Check README
image = client.upload(file='img.png')

# Print link and add to clipboard
URL = image.url
print(URL)
pyperclip.copy(URL)
print('URL add to clipboard')

# Does not allow the program to close
input()
