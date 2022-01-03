import cv2
import numpy as np
import os
import copy

'''
用处：根据轮廓信息提取原图图像
time:2022/1/3
make by:成都小混混
'''



def find_max_region(img):


    img2 = copy.deepcopy(img)
    img3 = copy.deepcopy(img)
    img4 = copy.deepcopy(img)
    img5 = copy.deepcopy(img)

    # cv2.imshow('1', img)  # 原图
    # cv2.waitKey(0)

    #二值化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)  # opencv里面画轮廓是根据白色像素来画的，所以反转一下。
    # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    #查找轮廓信息
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img2, contours, -1, (0, 0, 255), 3)
    # cv2.imshow('2', img2)  # 初始轮廓
    # cv2.waitKey(0)

    #将轮廓大小排序并提取想要得轮廓
    area = map(cv2.contourArea, contours)
    area_list = list(area)
    list_l = area_list.copy()
    list_l.sort()
    post = area_list.index(list_l[-2])
    # cv2.drawContours(img4, contours, post, (0, 0, 255), 1)
    # cv2.imshow('4', img4)  # 只显示零件外轮廓
    # cv2.waitKey(0)

    #提取轮廓中图形
    cimg = np.zeros_like(img)
    cimg[:, :, :] = 255
    # cv2.drawContours(cimg, contours, post, color=(0, 0, 0), thickness=-1)
    # cv2.imshow('5', cimg)  # 将零件区域像素值设为(0, 0, 0)
    # cv2.waitKey(0)

    #提取轮廓中原图
    final = cv2.bitwise_or(img5, cimg)
    # cv2.imshow('6', final)  # 执行或操作后生成想要的图片
    # cv2.waitKey(0)



if __name__ == '__main__':

    # img = cv2.imread(r" ")
    # roi = find_max_region(img)
    images_path = "C:/Users/PL/Desktop/"
    image_names = os.listdir(images_path)
    for image_name in image_names:
        image_path = os.path.join(images_path,image_name)
        # print(image_path)
        img = cv2.imread(image_path)
        find_max_region(img)

