try:
    import cv2 as cv
except:
    print("Module error!")
    exit(1)

class Marker:
    def __init__(self):
        self.winName="OutputImage"
        self.wait=1
        self.xList=[]
        self.yList=[]
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getIMG(self):
        return self.imgIn

    def display(self):
        # print("Displaying")
        cv.imshow(self.winName,self.img)
        if cv.waitKey(self.wait) & 0xFF == 27: #Press Escape Key to terminate window
            cv.destroyAllWindows()
            return 1
        return 0

    def drawCircle(self,event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDOWN:
            # print("Marking")

            self.xList.append(x)
            self.yList.append(y)

            font = cv.FONT_HERSHEY_PLAIN  
            org = (x+5, y+5)                # org
            fontScale = 1                   # fontScale   
            color = (255, 0, 0)             # Blue color in BGR
            thickness = 2                   # Line thickness of 2 px
            cv.putText(self.img,"(%d,%d)"%(x,y),org,font,fontScale,color,thickness)

            color = (0, 0, 255)             # Red color in BGR
            center = (x, y)                 # Center of circle
            radius = 1                      # Radius length of circle
            cv.circle(self.img,center,radius,color)

            color=(0,255,0)                 # Color for outer circle
            cv.circle(self.img,center,5,color)
    def finalize(self):
        choice=1
        if len(self.xList) > 1:
            print('Choose:')
            for i in range(len(self.xList)):
                print((i+1),'X:',self.xList[i],'Y:',self.yList[i])
            if self.display():
                self.wait=1
            choice=int(input('Enter final choice: '))

        self.x=self.xList[choice-1]
        self.y=self.yList[choice-1]

    def readClick(self):
        cv.namedWindow(self.winName)
        cv.setMouseCallback(self.winName,self.drawCircle)
        while(1):
            # print("Looping")
            if self.display():
                self.wait=0
                break 
        self.finalize()        
            
    def loadImage(self):
        filepath=input("Drag image>> ")
        self.img=cv.imread(filepath)
        self.imgIn=self.img.copy()
        # self.display()
        self.readClick()
    def run(self):
        self.loadImage()

if __name__=='__main__':
    print("Running test...")
    test_obj_1=Marker()
    test_obj_1.run()
