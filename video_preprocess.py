import cv2 
import os 

# 读取视频的信息, 保存到对应的目录 
def video_read(video_path, save_path): 
    vc = cv2.VideoCapture(video_path) 

    # 获得视频的帧数 
    img_num = vc.get(cv2.CAP_PROP_FRAME_COUNT) 
    
    # 读帧
    print(img_num)




if __name__ == "__main__":
    video_read('data/ORONbxQm7NM_000001_000011.mp4', 'data')
