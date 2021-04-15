import cv2 
import os 

# 读取视频的信息, 保存到对应的目录, 设定每个视频存n帧 
def video_read(video_path, save_path, n): 
    vc = cv2.VideoCapture(video_path) 

    # 获得视频的帧数 
    img_num = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
    # 采样间隔 
    sample_freq = int(img_num / n) 

    # 读帧
    for i in range(img_num): 
        _, frame = vc.read() 
        if i % sample_freq == 0: 
            img_name = str(int(i / sample_freq)) + '.png' 
            cur_save_path = os.path.join(save_path, img_name)
            cv2.imwrite(cur_save_path, frame)
    
    


if __name__ == "__main__":
    video_read('data/ORONbxQm7NM_000001_000011.mp4', 'data', 24)
