import os
from numpy import *
import cv2


def histeg(images):

    ret_dict ={
        "0":0,          #状态码
        "1":"false",     #是否完成
        "2":[]          #曲线图像
    }
    # 获取直方图p(r)
    for i,image in enumerate(images):

        # 灰度图像直方图均衡化
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        result = cv2.equalizeHist(gray)
        # cv2.imshow("dst",dst)
        # cv2.waitKey(0)

        #彩色图像直方图均衡化
        # (b,g,r) = cv2.split(image)
        # bH = cv2.equalizeHist(b)
        # gH = cv2.equalizeHist(g)
        # rH = cv2.equalizeHist(r)
        # result = cv2.merge((bH,gH,rH))
        # cv2.imshow("dst",result)
        # cv2.waitKey(0)

        #YUV直方图均衡化
        # image_YUV = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
        # channelsYUV = cv2.split(image_YUV)
        # channelsYUV[0] = cv2.equalizeHist(channelsYUV[0])
        # channels = cv2.merge(channelsYUV)
        # result = cv2.cvtColor(channels,cv2.COLOR_YCrCb2BGR)
        # cv2.imshow("dst",result)
        # cv2.waitKey(0)

        ret_dict["2"].append({"image":result})


    return ret_dict

if __name__ == '__main__':

    # img = cv2.imread(r'C:\Users\PL\Desktop\full\0\31_04_16_18_13_04_326043.jpg')
    # image = [img]

    images_path = "C:/Users/PL/Desktop/989"
    image_names = os.listdir(images_path)
    image = []
    for image_name in image_names:
        image_path = os.path.join(images_path,image_name)
        # print(image_path)
        img = cv2.imread(image_path)
        image.append(img)
        # cv2.imshow("img",img)
        # cv2.waitKey(0)

    ret = histeg(image)




