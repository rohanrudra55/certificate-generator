try:
    from PIL import ImageFont, ImageDraw, Image  
    import cv2  
    import numpy as np  
    import os
    import csv
    from marker import Marker  
except:
    print("Module error!")
    exit(1)

class Generate:
    def __init__(self):
        # self.outputN = "Cirtificate"
        self.name = 'Rohan Rudra'
        self.font1 = ImageFont.load_default()
        self.font2 = ImageFont.load_default()
        self.color1 = (255 ,0 ,0)
        self.color2 = (0 ,255 ,0)
        self.outputpath = './'

    def setimage(self,image):
        imgRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  
        # Pass the image to PIL  
        self.pilimg=Image.fromarray(imgRGB)
        self.draw = ImageDraw.Draw(self.pilimg)

    def write(self,coordinates):
        self.draw.text((int(coordinates[0]), int(coordinates[1])) ,self.name ,self.color1 ,self.font1)
        final = cv2.cvtColor(np.array(self.pilimg), cv2.COLOR_RGB2BGR)  
        cv2.imwrite(self.outputpath+self.name+'.png', final)
    
    def run(self,coordinates):
        self.write(coordinates)

if __name__ == '__main__':
    marker_obj=Marker()
    generate_obj=Generate()
    marker_obj.run()
    coordinates=[]
    coordinates.append(marker_obj.getX())
    coordinates.append(marker_obj.getY())

    generate_obj.setimage(marker_obj.getIMG())
    generate_obj.run(coordinates)

     



