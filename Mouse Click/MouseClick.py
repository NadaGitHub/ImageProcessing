import numpy as np
import cv2
from pynput.mouse import Listener
import PIL.ImageGrab

i=0
xh=[]
ys=[]
zv=[]
class ColorDetector(object):

    def __init__(self):  # Basic Colors - added +-25 tolerance ratio
        self.black_lower = np.array([0, 0, 0], dtype="uint8")
        self.black_upper = np.array([360, 90, 90], dtype="uint8")
        
        self.white_lower = np.array([225, 225, 225], dtype="uint8")
        self.white_upper = np.array([255, 255, 255], dtype="uint8")
        
        self.blue_lower = np.array([215, 100, 0], dtype="uint8")
        self.blue_upper = np.array([255, 255, 255], dtype="uint8")
        
        self.skyblue_lower = np.array([210, 130, 60], dtype="uint8")  
        self.skyblue_upper = np.array([255, 230, 160], dtype="uint8")
        
        self.green_lower = np.array([0, 200, 100], dtype="uint8")  
        self.green_upper = np.array([160, 255, 190], dtype="uint8")
        
        self.yellow_lower = np.array([25, 160, 230], dtype="uint8")
        self.yellow_upper = np.array([60, 190, 255], dtype="uint8")
        
        self.white_lower = np.array([210, 0, 240], dtype="uint8")
        self.white_upper = np.array([255, 30, 255], dtype="uint8")

        self.red_lower = np.array([0, 0, 230], dtype="uint8")
        self.red_upper = np.array([25, 255, 255], dtype="uint8")
        
        self.kernal = np.ones((5, 5), "uint8")
        
    def black_detection(self, image, hsv, image_det=True):

        if image_det == False:
            black_mask = cv2.inRange(hsv, self.black_lower, self.black_upper)
        else:
            black_mask = cv2.inRange(image, self.black_lower, self.black_upper)

        black_mask = cv2.dilate(black_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=black_mask)
        # Tracking the black Color
        contours,_ = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, "BLACK", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        return image
    def white_detection(self, image, hsv, image_det=True):

        if image_det == False:
            white_mask = cv2.inRange(hsv, self.white_lower, self.white_upper)
        else:
            white_mask = cv2.inRange(image, self.white_lower, self.white_upper)

        white_mask = cv2.dilate(white_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=white_mask)

        # Tracking the White Color
        contours,_ = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, "WHITE", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255))

        return image
    
    def skyblue_detection(self, image, hsv, image_det=True):
        
        if image_det == False:
            skyblue_mask = cv2.inRange(hsv, self.skyblue_lower, self.skyblue_upper)
        else:
            skyblue_mask = cv2.inRange(image, self.skyblue_lower, self.skyblue_upper)

        skyblue_mask = cv2.dilate(skyblue_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=skyblue_mask)
        # Tracking the skyblueColor
        contours,_ = cv2.findContours(skyblue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 20):
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, "skyblue", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        return image

    def blue_detection(self, image, hsv, image_det=True):

        if image_det == False:
            blue_mask = cv2.inRange(hsv, self.blue_lower, self.blue_upper)
        else:
            blue_mask = cv2.inRange(image, self.blue_lower, self.blue_upper)

        blue_mask = cv2.dilate(blue_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=blue_mask)

        # Tracking the Blue Color
        contours,_ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 20):
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, "blue", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
        return image
    def red_detection(self, image, hsv, image_det=True):

        if image_det == False:
            red_mask = cv2.inRange(hsv, self.red_lower, self.red_upper)
        else:
            red_mask = cv2.inRange(image, self.red_lower, self.red_upper)

        red_mask = cv2.dilate(red_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=red_mask)
        # Tracking the Red Color
        contours,_ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, "RED", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        return image
    
    def green_detection(self, image, hsv, image_det=True):

        if image_det == False:
            green_mask = cv2.inRange(hsv, self.green_lower, self.green_upper)
        else:
            green_mask = cv2.inRange(image, self.green_lower, self.green_upper)

        green_mask = cv2.dilate(green_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=green_mask)
        # Tracking the green Color
        contours,_ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, "GREEN", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        return image
    def yellow_detection(self, image, hsv, image_det=True):

        if image_det == False:
            yellow_mask = cv2.inRange(hsv, self.yellow_lower, self.yellow_upper)
        else:
            yellow_mask = cv2.inRange(image, self.yellow_lower, self.yellow_upper)

        yellow_mask = cv2.dilate(yellow_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=yellow_mask)
        # Tracking the yellow Color
        contours,_ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, "YELLOW", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        return image
    def ImageDetection(self, imagePath,pressed):
        image = cv2.imread(imagePath)
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        for n in range(len(xh)):
            if ((xh[n]>=0 and xh[n]<=360) and (ys[n]>=0 and ys[n]<=90) and (zv[n]>=0 and zv[n]<=90) ):
                print('black')
                image = self.black_detection(image, img_hsv, image_det=True)
            elif ((xh[n]>=215 and xh[n]<=255) and (ys[n]>=100 and ys[n]<=255) and (zv[n]>=0 and zv[n]<=255) ):
                print('blue')
                image = self.blue_detection(image, img_hsv, image_det=True)      
            elif ((xh[n]>=0 and xh[n]<=160) and (ys[n]>=200 and ys[n]<=255) and (zv[n]>=100 and zv[n]<=190) ):
                print('green')
                image = self.green_detection(image, img_hsv, image_det=True)
            elif ((xh[n]>=25 and xh[n]<=60) and (ys[n]>=160 and ys[n]<=190) and (zv[n]>=230 and zv[n]<=255) ):
                print('yellow')
                image = self.yellow_detection(image, img_hsv, image_det=True)
            elif ((xh[n]>=210 and xh[n]<=255) and (ys[n]>=0 and ys[n]<=30) and (zv[n]>=240 and zv[n]<=255) ):
                print('white')
                image = self.white_detection(image, img_hsv, image_det=True)
            elif ((xh[n]>=0 and xh[n]<=25) and (ys[n]>=0 and ys[n]<=255) and (zv[n]>=230 and zv[n]<=255) ):
                print('red')
                image = self.red_detection(image, img_hsv, image_det=True)
            else:
                print('other color')
                image = self.skyblue_detection(image, img_hsv, image_det=True)

        # show the images
        cv2.imshow("last", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


       
        
        
class Ui_ImageWindow(object):
    
    def imageDetection_onClick(self,imagePath):
        detector = ColorDetector()
        detector.ImageDetection(imagePath,0)

        
if __name__ == "__main__":
                
        image = cv2.imread('4.jpg')
        cv2.imshow("first", image)
        cv2.waitKey(1) & 0xFF
        def get_pixel_colour(i_x, i_y):
            return PIL.ImageGrab.grab().load()[i_x, i_y]
    
        def on_click(x, y, button, pressed):
            global i,xh,ys,zv
            if pressed:
                i = i + 1
                print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
                x,y,z = get_pixel_colour(x, y)
                print('RGB values: {} {} {}'.format(x,y,z))
                if i == 2:
                    listener.stop()
                color = np.uint8([[[x,y,z]]])
                hsv_color = cv2.cvtColor(color, cv2.COLOR_RGB2HSV)
                xh.append(hsv_color[0][0][0]*2)
                ys.append(hsv_color[0][0][1])
                zv.append(hsv_color[0][0][2])
                print('HSV values:',hsv_color[0][0][0]*2,hsv_color[0][0][1],hsv_color[0][0][2])
        with Listener(on_click=on_click) as listener:
            listener.join()
        iw = Ui_ImageWindow()
        iw.imageDetection_onClick('4.jpg')