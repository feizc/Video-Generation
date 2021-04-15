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


# 根据图片位置list(有顺序)生成视频
def video_generate(img_path_list, save_path, fps):
    # 确定图片的大小 
    img_t = cv2.imread(img_path_list[0]) 
    # print(img_t.shape) 
    height, width, channel = img_t.shape 
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    videowriter = cv2.VideoWriter(save_path, fourcc, fps, (width, height)) 

    for img_path in img_path_list: 
        img = cv2.imread(img_path) 
        videowriter.write(img) 
    
    videowriter.release()



if __name__ == "__main__":
    # video_read('data/1.mp4', 'data', 24) 
    img_path = 'data' 
    img_name_list = os.listdir(img_path) 
    img_name_list = [os.path.join(img_path, name) for name in img_name_list if 'png' in name]
    # print(img_name_list)
    video_generate(img_name_list, 'data/2.mp4', 5)
