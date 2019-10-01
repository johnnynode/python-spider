import tesserocr
from PIL import Image

image = Image.open("./pic/2.png")
# 1) 灰度处理 (将图像转化为灰色)
image = image.convert("L")

# 2) 二值化处理 (将图像转化为黑白色)
threshold = 128
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')

# 将图像转化为文本
result = tesserocr.image_to_text(image)

print(result)