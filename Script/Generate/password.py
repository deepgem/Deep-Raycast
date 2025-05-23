#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Passwords
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description 随机生成18位复杂密码
# @raycast.author materobot
# @raycast.authorURL https://raycast.com/materobot

import random
import string
import subprocess

def generate_password(length=18):
    # 预定义所有字符，避免重复连接
    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    # 直接生成随机密码
    password = ''.join(random.choices(chars, k=length))

    # 确保包含所有类型字符（更高效的方式）
    types = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*"
    ]

    # 检查是否包含所有类型，如果不包含则替换
    password_list = list(password)
    for i, char_type in enumerate(types):
        if not any(c in char_type for c in password_list):
            password_list[i] = random.choice(char_type)

    password = ''.join(password_list)
    return password

if __name__ == "__main__":
    password = generate_password()
    print(password)

    # 优化剪贴板操作 - 直接传递字符串而不编码
    subprocess.run(['pbcopy'], input=password, text=True, check=False)
