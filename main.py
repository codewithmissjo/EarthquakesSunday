import pandas as pd
from PIL import Image, ImageDraw

url = "eq-2024-v1.csv"
#url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2024-01-01&endtime=2025-01-01&orderby=magnitude&limit=100"
'''
Insert your description and query from earlier!
'''
df = pd.read_csv(url, sep="|")

print("Project starts")
img = Image.open("plate_carree_projection.png")
width, height = img.size
midx = width//2 + 1
midy = height//2 - 1

# create a draw object
draw = ImageDraw.Draw(img)
draw.rectangle([midx - 194, 8, midx + 190, 24], fill="white", outline="black", width=2)
draw.text([midx - 194, 8], "Map of all earthquakes with magnitude of 8 or higher since 1900", fill="red")

# coord top left, coord bottom right, start angle, end angle
#draw.pieslice(((midx - 16, midy - 16),(midx + 16, midy + 16)),240, 300,fill="blue")

for index, item in df.iterrows():
    print(item)
    x = midx + item["Longitude"] / 10 * 32.25
    y = midy - item["Latitude"] / 10 * 32.25
    draw.pieslice((x - 16, y - 16, x + 16, y + 16), 240, 300, fill="red")

def test():
    for lo in range(-180, 180, 10):
        for la in range(-90, 90, 10):
            x = midx + lo / 10 * 32.35
            y = midy + la / 10 * 32.35
            draw.pieslice((x - 10, y - 10, x + 10, y + 10), 240, 300, fill="blue")


# use one or more loops to draw 5 shapes in 5 different locations

img.save("test-3.png")
print("Project done")