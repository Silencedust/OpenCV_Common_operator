import cv2
import numpy as np
import os
import copy



def find_max_region(img):



    # gray = cv2.cvtColor(mask_sel,cv2.COLOR_BGR2GRAY)
    #
    # ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    #
    # cv2.imshow("thresh",thresh)
    # cv2.waitKey(0)
    #
    #
    # pixel_255 = len(thresh[thresh == 255])
    # pixel_0   = len(thresh[thresh == 0 ])
    #
    # scale = pixel_255/pixel_0
    # print(scale)

    img2 = copy.deepcopy(img)
    img3 = copy.deepcopy(img)
    img4 = copy.deepcopy(img)
    img5 = copy.deepcopy(img)

    cv2.imshow('1', img)  # 原图
    cv2.waitKey(0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)  # opencv里面画轮廓是根据白色像素来画的，所以反转一下。
    # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img2, contours, -1, (0, 0, 255), 3)
    cv2.imshow('2', img2)  # 初始轮廓
    cv2.waitKey(0)

    area = map(cv2.contourArea, contours)
    area_list = list(area)
    # print(area_list)

    list_l  = area_list.copy()
    list_l.sort()
    # area_max = max(area_list)
    # print(area_max)
    post = area_list.index(list_l[-2])

    # print(post)
    # post = area_list.index(area_max)


    cv2.drawContours(img4, contours, post, (0, 0, 255), 1)

    cv2.imshow('4', img4)  # 只显示零件外轮廓
    cv2.waitKey(0)

    cimg = np.zeros_like(img)
    cimg[:, :, :] = 255
    cv2.drawContours(cimg, contours, post, color=(0, 0, 0), thickness=-1)
    cv2.imshow('5', cimg)  # 将零件区域像素值设为(0, 0, 0)
    cv2.waitKey(0)

    final = cv2.bitwise_or(img5, cimg)

    cv2.imshow('6', final)  # 执行或操作后生成想要的图片
    cv2.waitKey(0)


    hsv = cv2.cvtColor(final, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([26, 10, 46])
    high_hsv = np.array([50, 255, 255])
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)

    pixel_255 = len(mask[mask == 255])

    if pixel_255>500:
        print("黄胶带")
    print("pixel_255",pixel_255)
    cv2.imshow("test", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






if __name__ == '__main__':

    # img = cv2.imread(r"C:\Users\PL\Desktop\test\LIANGPIN_12109_1_12-21-18-40-26.png")
    # roi = find_max_region(img)
    images_path = "C:/Users/PL/Desktop/1223_queliao/0/YASHANG"
    image_names = os.listdir(images_path)
    for image_name in image_names:
        image_path = os.path.join(images_path,image_name)
        # print(image_path)
        img = cv2.imread(image_path)
        find_max_region(img)

