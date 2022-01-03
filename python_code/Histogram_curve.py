import os
from numpy import *
import cv2
from matplotlib import pyplot as plt
import shutil

'''
use：生成直方图曲线
time:2022/1/3
make by:成都小混混
'''

def histeg(images,bins,type,judge):

    ret_dict ={
        "0":0,          #状态码
        "1":"false",     #是否完成
        "2":[]          #曲线图像
    }

    #检查result文件夹是否存在
    file_path = "./result"
    #去掉开头空格
    file_path = file_path.strip()
    #去掉结尾\\
    file_path = file_path.rstrip("\\")
    isExists = os.path.exists(file_path)


    #是否保存之前curve图
    if judge == "清空并保存":
        if isExists:
            shutil.rmtree(file_path)
            os.makedirs(file_path)
        else:
            os.makedirs(file_path)
    else:
        if isExists:
            pass
        else:
            os.makedirs(file_path)


    for i,image in enumerate(images):
        # cv2.imshow("img",image)
        # cv2.waitKey(0)

        #去缓存
        # plt.clf()

        if type=="灰度图像直方图":
        #灰度图像直方图
            img= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            hist, bin = histogram(img.flatten(), bins)
            image_name = str(i) + ".jpg"
            plt.plot(hist,color="red")
            curve_path = os.path.join(file_path,image_name)
            plt.savefig(file_path+"/"+image_name)
            curve = cv2.imread(curve_path)
            ret_dict["2"].append(curve)




        else:
            #彩色图像直方图
            hist_b = cv2.calcHist([image], [0], None, [256], [0, 255])
            hist_g = cv2.calcHist([image], [1], None, [256], [0, 255])
            hist_r = cv2.calcHist([image], [2], None, [256], [0, 255])
            plt.plot(hist_r,color="red")
            plt.plot(hist_b,color="blue")
            plt.plot(hist_g,color="green")

            image_name = str(i) + ".jpg"
            plt.savefig(file_path+"/"+image_name)
            # plt.show()
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

    ret = histeg(image,bins=256,type="灰度图像直方图",judge="清空并保存")




