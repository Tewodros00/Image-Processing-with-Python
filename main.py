from processing_functions import *

def main():
    print("Image processing tool")
    print("1. Brightness\n2. Contrast\n")
    choice = int(input("Which one do you want: "))

    file = input("Enter the name of the file with it's extension: ")
    img = Image.open(file)
    imgArray = numpy.array(img)

    if choice == 1:
        change_factor = eval(input("By how much do you want to increase the brightness(negative numbers to decrease): "))
        brightness(img, imgArray, change_factor)
    elif choice == 2:
        if img.mode != 'L':
            print("Sorry! can only change the contrast of Black and White images for now")
            return
        contrast(imgArray)
    
    new_image = Image.fromarray(imgArray)
    new_image.save("new_" + file)

main()   