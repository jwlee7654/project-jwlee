###
# pip install opencv-python
# pip install numpy

# pip install matplotlib
###

import cv2

vidcap = cv2.VideoCapture('C:/Users/AID Lab/nvr_rec/TwoPersons.mp4')

count = 0

while(vidcap.isOpened()):
    ret, image = vidcap.read()

    # image = cv2.resize(image, (1280, 720))
    
    if(int(vidcap.get(1)) % 24 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1)))) 
        
        # 추출된 이미지가 저장되는 경로
        cv2.imwrite("C:/Users/AID Lab/frames/two persons/frame%d.png" % count, image) 
        # print('Saved frame%d.jpg' % count) 
        
        count += 1

vidcap.release()