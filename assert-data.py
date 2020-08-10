#%%
import os

# %%
imgdir = "./dataset/imagenet/train/"

# %%
not_image_list = []
for cur,_,files in os.walk(imgdir):
    for file in files:
        if file.endswith(".JPEG"):
            classname = file.split('_')[0]
            # if image in correct classification splot
            assert cur.split('/')[-1] == classname
        else:
            not_image_list.append(file)

# %%
assert len(not_image_list) == 1003
