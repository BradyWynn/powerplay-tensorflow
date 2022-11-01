import cv2 as cv
import xml.etree.ElementTree as ET
import os

directory = r'C:\ProgramData\Tensorflow\powerplay-tensorflow\workspace\training_demo\images\test'
 
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if f.endswith('xml'):

        mytree = ET.parse(f)
        myroot = mytree.getroot()

        for widths in myroot.iter('width'):
            width = widths.text
            widths.text = str(300)
        for heights in myroot.iter('height'):
            height = heights.text
            heights.text = str(300)

        xcomp = 300 / float(width)
        ycomp = 300 / float(height)

        print(xcomp)
        print(ycomp)
        
        for xmins in myroot.iter('xmin'):
            xmins.text = str(int(float(xmins.text) * xcomp))
        for xmaxs in myroot.iter('xmax'):
            xmaxs.text = str(int(float(xmaxs.text) * xcomp))
        for ymins in myroot.iter('ymin'):
            ymins.text = str(int(float(ymins.text) * ycomp))
        for ymaxs in myroot.iter('ymax'):
            ymaxs.text = str(int(float(ymaxs.text) * ycomp))

        mytree.write(filename)
        # break

# img = cv.imread(r'C:\ProgramData\Tensorflow\powerplay-tensorflow\workspace\training_demo\images\train\0008709e-98.jpg')
# buh = cv.rectangle(img, (174, 84), (198, 147), (0, 0, 0), 1)

# cv.imshow("joe biden", buh)
# cv.waitKey(0) 
# cv.destroyAllWindows() 