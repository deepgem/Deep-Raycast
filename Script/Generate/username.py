#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Username
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description 随机生成用户名组合
# @raycast.author materobot
# @raycast.authorURL https://raycast.com/materobot

import random
import sys

# 预定义的单词列表，避免使用 faker 库
WORDS = [
    "alpha", "beta", "gamma", "delta", "echo", "foxtrot", "golf", "hotel",
    "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa",
    "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey",
    "xray", "yankee", "zulu", "azure", "blaze", "coral", "drift", "ember",
    "frost", "grove", "haven", "ivory", "jade", "karma", "lunar", "mystic",
    "nova", "ocean", "prism", "quest", "ruby", "storm", "titan", "ultra",
    "vibe", "wave", "xenon", "youth", "zenith", "arrow", "brave", "crisp",
    "dawn", "eagle", "flame", "grace", "honor", "icon", "jelly", "knight",
    "light", "magic", "night", "orbit", "peace", "quick", "rapid", "shine",
    "torch", "unity", "value", "wild", "xerus", "young", "zero", "manner", "manta", "mantis", "manuscript", "manx",
    "map", "maple", "mapusaurus", "maraca", "marble", "march", "mare", "margin", "marigold", "marimba", "marionberry",
    "marjoram", "market", "marlin", "marmoset", "marmot", "marquess", "marquis", "mars", "marshmallow", "marsupial",
    "marten", "mascara", "mascarpone", "mask", "mass", "mastodon", "mat", "match", "math", "matrix", "maxilla", "may",
    "mayflower", "mayonnaise", "meadow", "meadowlark", "meal", "measure", "meat", "mechanic", "medallion", "medicine",
    "medusaceratops", "meerkat", "meeting", "megalosaurus", "megaraptor", "melody", "melon", "memory", "menu",
    "mercury", "message", "metacarpal", "metal", "metatarsal", "meteor", "meteorite", "meteoroid", "meteorology",
    "meter", "methane", "mice", "microceratops", "microraptor", "microwave", "middle", "midnight", "mile", "milk",
    "milkshake", "millennium", "mimosa", "mind", "mine", "minibus", "mink", "minnow", "minotaurasaurus", "mint",
    "minute", "mirror", "mist", "mistake", "mitten", "mixer", "mixture", "moat", "mochi", "mockingbird", "modem",
    "mojoceratops", "molasses", "mole", "molecule", "mollusk", "molybdenum", "monarch", "monday", "money", "mongoose",
    "monitor", "monkey", "month", "mood", "moon", "moonflower", "moonstone", "moose", "moral", "morning", "morocco",
    "mortarboard", "mosquito", "moss", "moth", "motion", "motor", "motorcycle", "motorist", "mountain", "mouse",
    "mousepad", "moustache", "mouth", "move", "movie", "mozzarella", "muenster", "mulberry", "mule", "mum", "munchkin",
    "muscari", "muscle", "muse", "museum", "mushroom", "music", "musician", "muskmelon", "muskox", "mustang", "mustard",
    "myrtle", "myth", "nail", "name", "nannyberry", "napkin", "naranja", "narcissus", "narwhal", "nasturtium", "nation",
    "nautilus"
]


def generate_username():
    # 随机选择一个单词
    word = random.choice(WORDS)
    # 生成4位随机数字，不包含3和4
    allowed_digits = ['0', '1', '2', '5', '6', '7', '8', '9']
    number = ''.join(random.choices(allowed_digits, k=4))
    # 组合用户名
    username = f"{word}{number}"
    return username


if __name__ == "__main__":
    username = generate_username()
    print(username)
    # 复制到剪贴板
    if sys.platform == "darwin":
        import subprocess

        subprocess.run(['pbcopy'], input=username.encode())
