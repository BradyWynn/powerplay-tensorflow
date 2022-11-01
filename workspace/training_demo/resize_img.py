import cv2 as cv
# import required module
import os
# assign directory
directory = r'C:\ProgramData\robotics\TensorFlow\workspace\training_demo\images\train'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if f.endswith('jpg'):
        img = cv.imread(f)
        img = cv.resize(img, (300, 300))
        cv.imwrite(filename, img)
        # cv.imshow("window", img)
        # cv.waitKey(0) 
        # cv.destroyAllWindows() 