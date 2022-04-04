# import cv2
# import os
import cv2
import numpy as np
from background import beijing

def Mask(image,image_mask):
    # print(image_mask.shape)
    # cv2.imwrite('jieguo1.png',image_mask)
    # print(image.shape)
    array = np.array(0)
    imageB = image_mask != array
    # mask = np.dstack((imageB, imageB, imageB)).astype('int32')
    # print(mask)
    # print(mask.shape)
    # print(imageB.shape)
    image[imageB] = 0
    # print(image.shape)
    return image

def Mask_person(image,image_mask):
    xishu = 0.8
    image = cv2.resize(image, (image_mask.shape[1], image_mask.shape[0]))
    img_c = xishu * image_mask + (1 - xishu) * image
    img_c = img_c.astype(np.uint8)
    img_c = np.clip(img_c, 0, 255)
    return img_c


def Mask_renxiang(image,image_mask):
    array = np.array(0)
    imageB = image_mask == array
    # mask = np.dstack((imageB, imageB, imageB))
    # mask = np.array([])
    # print(imageB)
    image[imageB] = 255
    # print(image.shape)
    # cv2.imwrite('jieguo1.png', image_mask)
    return image

def M_renxiang(image,image_mask,img_beijing=None):
    array = np.array(0)
    imageB = image_mask == array
    image[imageB] = 255
    imageC = image_mask != array
    alpha_c = np.array(imageC.astype('int32') * 255)
    B, G, R = cv2.split(image)
    # print(type(alpha_c))
    # print(alpha_c)
    # ima_bgra = cv2.merge((B, G, R, alpha_c))
    # cv2.imwrite('re.png',ima_bgra,[int(cv2.IMWRITE_PNG_COMPRESSION),9])
    if type(img_beijing) == type(None):
        return image
    else:
        img = beijing(image, img_beijing, imageC)
    return img

if __name__ == '__main__':

    s = np.zeros((3,4))
    print(s)
    b = None
    print(type(b)==type(None))
