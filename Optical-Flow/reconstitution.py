# import cv2
# import numpy as np
# import glob

frameSize = (256, 256)
# save_path = '/Users/clair/Desktop/output_video.mp4'
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter(save_path,fourcc, 60.0, frameSize)
      
# for filename in glob.glob('D:/prediction/*.jpg'):
#     img = cv2.imread(filename)
#     out.write(img)

# out.release()


import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('C:/Users/clair/Desktop/THESIS/CODE_v2/E-RAFT-main/saved/mvsec_45hz_OK/visualizations/gt/*.png'):#'C:/Users/clair/Desktop/Depth-Event/data/test_sequence_00_town10/semantic/frames/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('C:/Users/clair/Desktop/THESIS/CODE_v2/E-RAFT-main/saved/mvsec_45hz_OK/visualizations/gt.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 15, frameSize)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()