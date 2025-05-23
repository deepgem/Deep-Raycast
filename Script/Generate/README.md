# Raycast 随机生成工具

这个项目包含两个 Raycast Script Commands，用于生成随机的用户名和密码。

## 功能说明

### 1. 随机用户名生成器 (username.py)

- 生成格式：随机单词 + 4位数字
- 特点：
  - 使用预定义的单词列表（包含常用英文单词）
  - 4位数字不包含3和4
  - 自动复制到剪贴板
- 示例输出：`alpha1256`, `brave7890`

### 2. 随机密码生成器 (passwords.py)

- 生成18位复杂密码
- 密码要求：
  - 必须包含大写字母
  - 必须包含小写字母
  - 必须包含数字
  - 必须包含特殊字符（!@#$%^&*）
- 自动复制到剪贴板

### 3. 精选友好词汇列表 (word.json)
- 由 Glitch 团队维护，旨在为开发者提供一组经过精心筛选的英文单词列表。
- 这些词汇被广泛用于项目命名、团队名称等场景，强调友好、积极、富有想象力且易于拼写和记忆。
- 词汇项目地址：https://github.com/glitchdotcom/friendly-words

## 使用方法

1. 确保已安装 Raycast
2. 将脚本文件放入 Raycast Script Commands 目录
3. 在 Raycast 中：
   - 输入 `Username` 生成随机用户名
   - 输入 `Passwords` 生成随机密码

## 技术实现

- 使用 Python 3.12.9
- 依赖标准库：`random`, `string`, `subprocess`
- 针对 macOS 系统优化（使用 `pbcopy` 实现剪贴板功能）

