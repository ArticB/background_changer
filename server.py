import urllib
from urllib.parse import parse_qs
import requests
import ctypes
import time
import os
from os import path
from dotenv import load_dotenv
import json
from pathlib import Path
load_dotenv()

KEY = os.getenv("KEY")
headers = {"Authorization": "Client-ID " + KEY}

url = ""
json_object = {}
parse = ""
filename = ""
image_file = ""
bg_path = "./background"
json_file = "image.json"

def create_bg_folder():
    if(path.exists(bg_path) is False):
        try:
            os.mkdir(bg_path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
    else:
        print("Exists")


def save_image():    
    json_data = load_json()
    url = json_data["urls"]["full"]
    parse = urllib.parse.urlparse(url)
    filename = "." + parse_qs(parse.query)["fm"][0]
    image_file = parse.path + filename
    urllib.request.urlretrieve(url, bg_path + image_file)


def get_data():
    r = requests.get(
        "https://api.unsplash.com/photos/random?query=wallpaper&orientation=landscape",
        headers=headers,
    )
    json_write = lambda json_file: open(json_file, 'w').write(json.dumps(r.json()))
    json_write(json_file)



def load_json():
    with open(json_file, "r") as openfile:
        json_object = json.load(openfile)
    return json_object


def change_background_image():
    """http://www.jasinskionline.com/windowsapi/ref/s/systemparametersinfo.html
    """    

    ctypes.windll.user32.SystemParametersInfoW(20, 0, get_full_path(), 0)
    pass

def get_full_path():
    json_data = load_json()
    url = json_data["urls"]["full"]
    parse = urllib.parse.urlparse(url)
    filename = "." + parse_qs(parse.query)["fm"][0]
    image_file = parse.path + filename
    return os.path.dirname(os.path.realpath(bg_path)) + "\\background\\" + image_file[1:]

create_bg_folder()
