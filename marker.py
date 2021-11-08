try:
    import cv2 as cv
except:
    print("Module error!")
    exit(1)

class Marker:
    def __init__(self):
        self.winName="OutputImage"
    def display(self):
        print(self.winName)
        cv.imshow(self.winName,self.img)
        if cv.waitKey(1)==26:
            cv.destroyAllWindows()
            exit(0)
    def drawCircle(self,event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.putText(self.img,"coordinates (%d,%d)"%(x,y),(60,60),2,1,(0,255,0))

    def readClick(self):
        cv.setMouseCallback(self.winName,self.drawCircle)
        while(1):
            cv.imshow(self.winName,self.img)
            if cv.waitKey(10) & 0xFF == 27:   #Press Escape Key to terminate window
                break
            cv.destroyAllWindows()  

    def loadImage(self):
        filepath=input("Drag image>> ")
        self.img=cv.imread(filepath)
        # self.display()
        cv.namedWindow(self.winName)
        self.readClick()

if __name__=='__main__':
    print("Running test...")
    test_obj_1=Marker()
    test_obj_1.loadImage()
