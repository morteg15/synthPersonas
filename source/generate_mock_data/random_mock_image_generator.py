#create 100 mock profile images that are a random color and have a random number of circles
# pip install pillow

from PIL import Image, ImageDraw
import random

def generate_image():
    img = Image.new(mode="RGB", size=(400, 400), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img)
    for i in range(random.randint(1, 10)):
        x0 = random.randint(0, 400)
        y0 = random.randint(0, 400)
        x1 = random.randint(x0, 400)
        y1 = random.randint(y0, 400)
        draw.ellipse((x0, y0, x1, y1), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return img

if __name__ == "__main__":
    for i in range(100):
        img = generate_image()
        img.save(f"data/profilepictures/profilepicture_{i}.jpg")
