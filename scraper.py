import os
import requests
import argparse, sys
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(0)

parser.add_argument('url', help="The KissManga url you want to pull the images from. Required.")

parser.add_argument("-n","--name", help="The name you want the output files to be. E.g. for bleach_1.jpg, you would supply `--name=bleach`. Defaults to `page`", default="page")

parser.add_argument("-o", "--output_dir",help="The directory you want the files to be created in. If the directory does not exist, it will create it. Defaults to current directory")
args = parser.parse_args()

url = args.url
name = args.name
output_dir = args.output_dir
if output_dir is None:
    output_dir = os.getcwd()

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

images = soup.find(id="centerDivVideo").find_all("img")
counter = 0
sources = []
for img in images:
    sources.append(img.get('src'))

for src in sources:
    r = requests.get(src)
    if r.status_code == 200:
        filename = f"{name}_{counter}.jpg"
        path = os.path.join(output_dir,filename)
        with open(path, 'wb') as f:
            for chunk in r:
                f.write(chunk)

        counter += 1
