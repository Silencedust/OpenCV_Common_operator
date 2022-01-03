import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
import images

'''
use：filter滤波器
time:2022/1/3
make by:成都小混混
'''

def image_filters(image):
    # 预定义的图像增强滤波器
    img_origes = image

    #filter()函数传入的图片格式为<class 'PIL.JpegImagePlugin.JpegImageFile'>，不能是numpy
    #将array格式转化为image
    img = Image.fromarray(np.uint8(img_origes))


    #模糊滤波           处理之后的图像会整体变得模糊
    img_blur = img.filter(ImageFilter.BLUR)
    #轮廓滤波           将图像中的轮廓信息全部提取出来
    img_contour = img.filter(ImageFilter.CONTOUR)
    #细节增强滤波         使得图像中细节更加明显
    img_detail = img.filter(ImageFilter.DETAIL)
    #边缘增强滤波         突出、加强和改善图像中不同灰度区域之间的边界和轮廓的图像增强方法
    img_edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE)
    #深度边缘增强滤波      使得图像中边缘部分更加明显
    img_edge_enhance_more = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    #浮雕滤波            使图像呈现出浮雕效果
    img_emboss = img.filter(ImageFilter.EMBOSS)
    #寻找边缘信息滤波      找出图像中的边缘信息
    img_find_edges = img.filter(ImageFilter.FIND_EDGES)
    #平滑滤波             突出图像的宽大区域、低频成分、主干部分或抑制图像噪声和干扰高频成分，使图像亮度平缓渐变，减小突变梯度，改善图像质量)
    img_smooth = img.filter(ImageFilter.SMOOTH)
    #深度平滑滤波          使得图像变得更加平滑
    img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    #锐化滤波             补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰
    img_sharpen = img.filter(ImageFilter.SHARPEN)
    #最小值滤波            在每个像素点为中心的5x5区域25个像素点中选择最小的像素作为新的值
    img_min = img.filter(ImageFilter.MinFilter(3))
    #最大值滤波            在每个像素点为中心的5x5区域25个像素点中选择最大的像素作为新的值
    img_max = img.filter(ImageFilter.MaxFilter(3))
    #等级滤波器            对于输入图像的每个像素点，等级滤波器根据像素值，在（size，size）的区域中对所有像素点进行排序，然后拷贝对应等级的值存储到输出图像中
    img_rank = img.filter(ImageFilter.RankFilter(5,24))
    #卷积滤波
    img_kernel = img.filter(ImageFilter.Kernel((3,3),(1,1,1,0,0,0,2,0,2)))

    return

if __name__ == '__main__':
    #打开为numpy格式
    image = cv2.imread("../images/filter.png")
    image_filters(image)

    # #打开为PIL数据格式
    # image = Image.open("../../images/filter.png")
    # image_filters(image)