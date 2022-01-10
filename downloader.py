from PIL import Image
from urllib.request import urlopen
import os

PY_PATH = os.path.dirname(os.path.realpath(__file__))




tier_list = ["tier1a","tier1b","tier2","tier3a","tier3b","tier3c","tier4a","tier4b"]
squadmate_list = ["ashley","garrus","jack","legion","liara","miranda","tali","thane","urdnot","edi","grunt","jacob","james","javik","kaidan","kasumi","mordin","samara","zaeed"]
scene_list = ["citadel","collector-base","eden-prime","invaded","omega"]
morality_dict = {1:"Paragon", 2:"Neutral", 3:"Renegade" }



os.mkdir(os.path.join(PY_PATH, "side"), 0o666)
side = Image.open(urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/side/1.jpg"))
side.save(PY_PATH + "/side/side1.jpg", "JPEG")
side = Image.open(urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/side/2.jpg"))
side.save(PY_PATH + "/side/side2.jpg", "JPEG")
side = Image.open(urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/side/3.jpg"))
side.save(PY_PATH + "/side/side3.jpg", "JPEG")

title = Image.open(urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/tt-en-us.png"))
title.save(PY_PATH + "/title.png", "png")


os.mkdir(os.path.join(PY_PATH, "ship"), 0o666)
ship = Image.open(urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/ship/ship-1.png"))
ship.save(PY_PATH + "/ship/ship1.png", "png")
ship = Image.open(urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/ship/ship-2.png"))
ship.save(PY_PATH + "/ship/ship2.png", "png")
ship = Image.open(urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/ship/ship-3.png"))
ship.save(PY_PATH + "/ship/ship3.png", "png")


for tier in tier_list[0:3]:
    os.mkdir(os.path.join(PY_PATH, tier), 0o666)
    for name_s in squadmate_list[0:9]:
        for morality in dict.fromkeys(morality_dict):
            image = Image.open(
                urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/{}/{}-{}.png".format(tier, name_s, morality)))
            #image.show()
            image.save(PY_PATH + "/"+ tier + "/" + name_s + str(morality) + ".png" , "png")
            print(PY_PATH + " /"+ tier + name_s + str(morality))


for tier in tier_list[3:8]:
    os.mkdir(os.path.join(PY_PATH, tier), 0o666)
    for name_s in squadmate_list:
        for morality in dict.fromkeys(morality_dict):
            image = Image.open(
                urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/{}/{}-{}.png".format(tier, name_s, morality)))
            #image.show()
            image.save(PY_PATH + "/" + tier + "/" + name_s + str(morality) + ".png" , "png")
            print(PY_PATH + " /"+ tier + name_s + str(morality))

os.mkdir(os.path.join(PY_PATH, "scenes"), 0o666)
for scene in scene_list:
    for morality in dict.fromkeys(morality_dict):
        scene_image = Image.open(
            urlopen("https://masseffectcustomizer.com/_generated/images-1x/wallpaper/scene/{}-{}.png".format(scene, morality)))
        scene_image.save(PY_PATH + "/scenes/" + scene + str(morality) + ".png" , "png")