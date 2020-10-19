import os
from PIL import Image

path = 'C:\\Users\\fedeb\\session2a-image\\raw\\'
processed = 'C:\\Users\\fedeb\\session2a-image\\processed'
os.mkdir(processed)
dirs = os.listdir(path)

newsize1 = (400, 300)
newsize2 = (300, 400)
for item in dirs:
    img = Image.open(path+item)
    w, h = img.size
    if w > h:
        new_w = (4 / 3) * h
        cut_img = img.crop((0, 0, new_w, h))
        img_rsz = cut_img.thumbnail(newsize1)
    if h > w:
        new_h = (4 / 3) * w
        cut_img = img.crop((0, 0, w, new_h))
        img_rsz = cut_img.thumbnail(newsize2)
    cut_img.save(os.path.join(processed, item + '.jpg'))
