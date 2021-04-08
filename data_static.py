import os 
from PIL import Image 
from PIL import ImageSequence 
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True 

from collections import Counter 

# cur_path = os.getcwd()
gif_path = '/apdcephfs/share_47076/zekangli/NIPS2021/AutoGif/gifs'
gif_name_list = os.listdir(gif_path)

frame_list = [] 
frame_counter = Counter() 

for cur_file in gif_name_list: 
    file_path = os.path.join(gif_path, cur_file) 
    try:
        img = Image.open(file_path) 
    except:
        print(file_path)
    frame_num = 0 
    for frame in ImageSequence.Iterator(img):
        frame_num += 1 
    frame_list.append(frame_num) 

frame_counter.update(frame_list) 

print('total num: ', len(frame_list))
print(frame_counter) 



