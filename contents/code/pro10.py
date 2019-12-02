#验证识别测试
import tesserocr
from PIL import Image

#打开图片
image = Image.open("./pic/2.png")

#识别验证码
result = tesserocr.image_to_text(image)

print(result)