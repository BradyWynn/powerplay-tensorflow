
from bs4 import BeautifulSoup

with open(r'C:\ProgramData\robotics\TensorFlow\workspace\training_demo\images\train\7b061911-IMG_20220923_163153908.xml', 'r') as f:
	file = f.read() 

soup = BeautifulSoup(file, 'xml')
names = soup.find_all('xmin')
for name in names:
    print(name.text)