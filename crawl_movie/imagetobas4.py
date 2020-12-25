import base64
import os
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
f = open("fileimg_2.txt",'w')
# for i in os.listdir("data"):
#     path_img =  "data/"+i
#     print(path_img)
base64_ = get_base64_encoded_image("no-img.png")
f.write(str(base64_))
f.close()
