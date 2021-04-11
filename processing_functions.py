from PIL import Image
import numpy

# brightness function accepts the image, the image array as a list and the change in brightness
def brightness(img, imgArray, change_factor):
    # if image is 8-bit black and white image
    if img.mode == 'L': 
        for i in range(len(imgArray)):
            for j in range(len(imgArray[i])):
                l = imgArray[i][j] + change_factor
                if l > 255:
                    imgArray[i][j] = 255
                elif l < 0:
                    imgArray[i][j] = 0
                else:
                    imgArray[i][j] = l

    # if image is RGB image    
    if img.mode == 'RGB': 
        for i in range(len(imgArray)):
            for j in range(len(imgArray[i])):
                for k in range(len(imgArray[i][j])):
                    l = imgArray[i][j][k] + change_factor
                    if l > 255:
                        imgArray[i][j][k] = 255
                    elif l < 0:
                        imgArray[i][j][k] = 0
                    else:
                        imgArray[i][j][k] = l

def contrast(imgArray):
    maxi = 0
    mini = 255

    # finds the maximum and minimum pixel value in the image
    for i in range(len(imgArray)):
        for j in range(len(imgArray[i])):
            if imgArray[i][j] > maxi:
                maxi = imgArray[i][j]
            elif imgArray[i][j] < mini:
                mini = imgArray[i][j]
            else:
                continue

    # iterate over the image array and change their value by using  
    # Pn = (Po - mini) * m + mini
    m = (255 - mini) / (maxi - mini)

    for i in range(len(imgArray)):
        for j in range (len(imgArray[i])):
            imgArray[i][j] = int((imgArray[i][j] - mini) * m + mini)

