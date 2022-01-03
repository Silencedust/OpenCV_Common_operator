
import cv2

img = cv2.imread(r"C:\Users\PL\Desktop\out_dir\21-1210184901913__vec_image_52624_52534_0_0.png",o)
_, tmp_bin = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("img",tmp_bin)
cv2.waitKey(0)