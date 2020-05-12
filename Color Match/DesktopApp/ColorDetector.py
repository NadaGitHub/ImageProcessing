import numpy as np
import cv2

###audio###
from pygame import mixer
import pygame
import os
import time
from gtts import gTTS
###########

class ColorDetector(object):

    def __init__(self):  
        self.black_lower = np.array([0, 0, 0], dtype="uint8")
        self.black_upper = np.array([25, 25, 25], dtype="uint8")

        self.white_lower = np.array([225, 225, 225], dtype="uint8")
        self.white_upper = np.array([255, 255, 255], dtype="uint8")

        self.red_lower = np.array([0, 0, 230], dtype="uint8")
        self.red_upper = np.array([25, 25, 255], dtype="uint8")

        self.lime_lower = np.array([0, 230, 0], dtype="uint8")
        self.lime_upper = np.array([25, 255, 25], dtype="uint8")

        self.blue_lower = np.array([230, 0, 0], dtype="uint8")
        self.blue_upper = np.array([255, 25, 25], dtype="uint8")

        self.yellow_lower = np.array([0, 230, 230], dtype="uint8")
        self.yellow_upper = np.array([25, 255, 255], dtype="uint8")

        self.cyan_lower = np.array([230, 230, 0], dtype="uint8")
        self.cyan_upper = np.array([255, 255, 25], dtype="uint8")

        self.magenda_lower = np.array([230, 0, 230], dtype="uint8")
        self.magenda_upper = np.array([255, 25, 255], dtype="uint8")

        self.silver_lower = np.array([167, 167, 167], dtype="uint8")  
        self.silver_upper = np.array([217, 217, 217], dtype="uint8")

        self.gray_lower = np.array([103, 103, 103], dtype="uint8") 
        self.gray_upper = np.array([153, 153, 153], dtype="uint8")

        self.maroon_lower = np.array([0, 0, 103], dtype="uint8")  
        self.maroon_upper = np.array([25, 25, 153], dtype="uint8")

        self.olive_lower = np.array([0, 103, 103], dtype="uint8")  
        self.olive_upper = np.array([25, 153, 153], dtype="uint8")

        self.green_lower = np.array([0, 103, 0], dtype="uint8")  
        self.green_upper = np.array([25, 153, 25], dtype="uint8")

        self.purple_lower = np.array([103, 0, 103], dtype="uint8")  
        self.purple_upper = np.array([153, 25, 153], dtype="uint8")

        self.teal_lower = np.array([103, 103, 0], dtype="uint8")  
        self.teal_upper = np.array([153, 153, 25], dtype="uint8")

        self.navy_lower = np.array([103, 0, 0], dtype="uint8")  
        self.navy_upper = np.array([153, 25, 25], dtype="uint8")

        self.skyblue_lower = np.array([210, 130, 60], dtype="uint8")  
        self.skyblue_upper = np.array([255, 230, 160], dtype="uint8")

        self.kernal = np.ones((5, 5), "uint8")

    def black_detection(self, image, hsv, image_det=True):
        if image_det == False:
            black_mask = cv2.inRange(hsv, self.black_lower, self.black_upper)
        else:
            black_mask = cv2.inRange(image, self.black_lower, self.black_upper)

        black_mask = cv2.dilate(black_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=black_mask)
        
        contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                 x, y, w, h = cv2.boundingRect(contour)
                 #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                 #cv2.putText(image, "BLACK", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
         
        ### To make audio ###
        """
        mytext = 'BLACK'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("BLACK.mp3")
        os.system("BLACK.mp3")
        """
        ### To play audio ###      
        pygame.mixer.init()
        pygame.mixer.music.load('BLACK.mp3')
        pygame.mixer.music.queue('BLACK.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue
        
        

        return image

    def white_detection(self, image, hsv, image_det=True):

        if image_det == False:
            white_mask = cv2.inRange(hsv, self.white_lower, self.white_upper)
        else:
            white_mask = cv2.inRange(image, self.white_lower, self.white_upper)

        white_mask = cv2.dilate(white_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=white_mask)

        contours, hierarchy = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "WHITE", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255, 255, 255))

        ### To make audio ###
        """
        mytext = 'WHITE'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("WHITE.mp3")
        os.system("WHITE.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('WHITE.mp3')
        pygame.mixer.music.queue('WHITE.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue
        return image

    def red_detection(self, image, hsv, image_det=True):

        if image_det == False:
            red_mask = cv2.inRange(hsv, self.red_lower, self.red_upper)
        else:
            red_mask = cv2.inRange(image, self.red_lower, self.red_upper)

        red_mask = cv2.dilate(red_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=red_mask)
        
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "RED", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'RED'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("RED.mp3")
        os.system("RED.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('RED.mp3')
        pygame.mixer.music.queue('RED.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def lime_detection(self, image, hsv, image_det=True):

        if image_det == False:
            lime_mask = cv2.inRange(hsv, self.lime_lower, self.lime_upper)
        else:
            lime_mask = cv2.inRange(image, self.lime_lower, self.lime_upper)

        lime_mask = cv2.dilate(lime_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=lime_mask)
       
        contours, hierarchy = cv2.findContours(lime_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "LIME", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'LIME'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("LIME.mp3")
        os.system("LIME.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('LIME.mp3')
        pygame.mixer.music.queue('LIME.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue


        return image

    def blue_detection(self, image, hsv, image_det=True):

        if image_det == False:
            blue_mask = cv2.inRange(hsv, self.blue_lower, self.blue_upper)
        else:
            blue_mask = cv2.inRange(image, self.blue_lower, self.blue_upper)

        blue_mask = cv2.dilate(blue_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=blue_mask)

        
        contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "BLUE", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 0, 0))


        ### To make audio ###
        """
        mytext = 'BLUE'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("BLUE.mp3")
        os.system("BLUE.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('BLUE.mp3')
        pygame.mixer.music.queue('BLUE.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue


        return image

    def yellow_detection(self, image, hsv, image_det=True):

        if image_det == False:
            yellow_mask = cv2.inRange(hsv, self.yellow_lower, self.yellow_upper)
        else:
            yellow_mask = cv2.inRange(image, self.yellow_lower, self.yellow_upper)

        yellow_mask = cv2.dilate(yellow_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=yellow_mask)
        
        contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "YELLOW", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'YELLOW'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("YELLOW.mp3")
        os.system("YELLOW.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('YELLOW.mp3')
        pygame.mixer.music.queue('YELLOW.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def cyan_detection(self, image, hsv, image_det=True):

        if image_det == False:
            cyan_mask = cv2.inRange(hsv, self.cyan_lower, self.cyan_upper)
        else:
            cyan_mask = cv2.inRange(image, self.cyan_lower, self.cyan_upper)

        cyan_mask = cv2.dilate(cyan_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=cyan_mask)
        
        contours, hierarchy = cv2.findContours(cyan_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "CYAN/AQUA", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
        ### To make audio ###
        """
        mytext = 'CYAN'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("CYAN.mp3")
        os.system("CYAN.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('CYAN.mp3')
        pygame.mixer.music.queue('CYAN.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue


        return image

    def magenda_detection(self, image, hsv, image_det=True):

        if image_det == False:
            magenda_mask = cv2.inRange(hsv, self.magenda_lower, self.magenda_upper)
        else:
            magenda_mask = cv2.inRange(image, self.magenda_lower, self.magenda_upper)

        magenda_mask = cv2.dilate(magenda_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=magenda_mask)
        
        contours, hierarchy = cv2.findContours(magenda_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "MAGENDA/FUCHSIA", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'MAGENDA'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("MAGENDA.mp3")
        os.system("MAGENDA.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('MAGENDA.mp3')
        pygame.mixer.music.queue('MAGENDA.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def silver_detection(self, image, hsv, image_det=True):

        if image_det == False:
            silver_mask = cv2.inRange(hsv, self.silver_lower, self.silver_upper)
        else:
            silver_mask = cv2.inRange(image, self.silver_lower, self.silver_upper)

        silver_mask = cv2.dilate(silver_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=silver_mask)
        
        contours, hierarchy = cv2.findContours(silver_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "SILVER", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'SILVER'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("SILVER.mp3")
        os.system("SILVER.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('SILVER.mp3')
        pygame.mixer.music.queue('SILVER.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def gray_detection(self, image, hsv, image_det=True):

        if image_det == False:
            gray_mask = cv2.inRange(hsv, self.gray_lower, self.gray_upper)
        else:
            gray_mask = cv2.inRange(image, self.gray_lower, self.gray_upper)

        gray_mask = cv2.dilate(gray_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=gray_mask)
        
        contours, hierarchy = cv2.findContours(gray_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "GRAY", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
        ### To make audio ###
        """
        mytext = 'GRAY'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("GRAY.mp3")
        os.system("GRAY.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('GRAY.mp3')
        pygame.mixer.music.queue('GRAY.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def maroon_detection(self, image, hsv, image_det=True):

        if image_det == False:
            maroon_mask = cv2.inRange(hsv, self.maroon_lower, self.maroon_upper)
        else:
            maroon_mask = cv2.inRange(image, self.maroon_lower, self.maroon_upper)

        maroon_mask = cv2.dilate(maroon_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=maroon_mask)
        
        contours, hierarchy = cv2.findContours(maroon_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "MAROON", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'MAROON'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("MAROON.mp3")
        os.system("MAROON.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('MAROON.mp3')
        pygame.mixer.music.queue('MAROON.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def olive_detection(self, image, hsv, image_det=True):

        if image_det == False:
            olive_mask = cv2.inRange(hsv, self.olive_lower, self.olive_upper)
        else:
            olive_mask = cv2.inRange(image, self.olive_lower, self.olive_upper)

        olive_mask = cv2.dilate(olive_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=olive_mask)
        
        contours, hierarchy = cv2.findContours(olive_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "OLIVE", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))
        
        ### To make audio ###
        """
        mytext = 'OLIVE'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("OLIVE.mp3")
        os.system("OLIVE.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('OLIVE.mp3')
        pygame.mixer.music.queue('OLIVE.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def green_detection(self, image, hsv, image_det=True):

        if image_det == False:
            green_mask = cv2.inRange(hsv, self.green_lower, self.green_upper)
        else:
            green_mask = cv2.inRange(image, self.green_lower, self.green_upper)

        green_mask = cv2.dilate(green_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=green_mask)
        
        contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 200):
                x, y, w, h = cv2.boundingRect(contour)
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "GREEN", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'GREEN'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("GREEN.mp3")
        os.system("GREEN.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('GREEN.mp3')
        pygame.mixer.music.queue('GREEN.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue
        
        return image

    def purple_detection(self, image, hsv, image_det=True):

        if image_det == False:
            purple_mask = cv2.inRange(hsv, self.purple_lower, self.purple_upper)
        else:
            purple_mask = cv2.inRange(image, self.purple_lower, self.purple_upper)

        purple_mask = cv2.dilate(purple_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=purple_mask)
        
        contours, hierarchy = cv2.findContours(purple_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "PURPLE", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'PURPLE'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("PURPLE.mp3")
        os.system("PURPLE.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('PURPLE.mp3')
        pygame.mixer.music.queue('PURPLE.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue


        return image

    def teal_detection(self, image, hsv, image_det=True):

        if image_det == False:
            teal_mask = cv2.inRange(hsv, self.teal_lower, self.teal_upper)
        else:
            teal_mask = cv2.inRange(image, self.teal_lower, self.teal_upper)

        teal_mask = cv2.dilate(teal_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=teal_mask)
        
        contours, hierarchy = cv2.findContours(teal_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "TEAL", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'TEAL'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("TEAL.mp3")
        os.system("TEAL.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('TEAL.mp3')
        pygame.mixer.music.queue('TEAL.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def navy_detection(self, image, hsv, image_det=True):

        if image_det == False:
            navy_mask = cv2.inRange(hsv, self.navy_lower, self.navy_upper)
        else:
            navy_mask = cv2.inRange(image, self.navy_lower, self.navy_upper)

        navy_mask = cv2.dilate(navy_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=navy_mask)
       
        contours, hierarchy = cv2.findContours(navy_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "NAVY", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'NAVY'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("NAVY.mp3")
        os.system("NAVY.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('NAVY.mp3')
        pygame.mixer.music.queue('NAVY.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def skyblue_detection(self, image, hsv, image_det=True):

        if image_det == False:
            skyblue_mask = cv2.inRange(hsv, self.skyblue_lower, self.skyblue_upper)
        else:
            skyblue_mask = cv2.inRange(image, self.skyblue_lower, self.skyblue_upper)

        skyblue_mask = cv2.dilate(skyblue_mask, self.kernal)
        output = cv2.bitwise_and(image, image, mask=skyblue_mask)
        
        contours, hierarchy = cv2.findContours(skyblue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                #image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.putText(image, "skyblue", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255))

        ### To make audio ###
        """
        mytext = 'skyblue'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("skyblue.mp3")
        os.system("skyblue.mp3")
        """
        ### To play audio ###
        pygame.mixer.init()
        pygame.mixer.music.load('skyblue.mp3')
        pygame.mixer.music.queue('skyblue.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def Match_detection(self, image, hsv, image_det=True):
        
        pygame.mixer.init()
        pygame.mixer.music.load('Match.mp3')
        pygame.mixer.music.queue('Match.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def Not_Match_detection(self, image, hsv, image_det=True):
        
        pygame.mixer.init()
        pygame.mixer.music.load('Not Match.mp3')
        pygame.mixer.music.queue('Not Match.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

        return image

    def BLACK_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Black matchs with White  Green  Yellow  Red.mp3')
        pygame.mixer.music.queue('Black matchs with White  Green  Yellow  Red.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image

    def WHITE_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('White matchs with  Black  Red  Blue.mp3')
        pygame.mixer.music.queue('White matchs with  Black  Red  Blue.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image

    def RED_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Red matchs with Black  Yellow  Blue  Green  Cyan  Silver  Olive  Purple.mp3')
        pygame.mixer.music.queue('Red matchs with Black  Yellow  Blue  Green  Cyan  Silver  Olive  Purple.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image

    def LIME_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Lime matchs with Yellow  Green.mp3')
        pygame.mixer.music.queue('Lime matchs with Yellow  Green.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image

    def BLUE_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Blue matchs with  White  Red  Green  Gray  Magenda  Silver  Purple.mp3')
        pygame.mixer.music.queue('Blue matchs with  White  Red  Green  Gray  Magenda  Silver  Purple.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image

     
    def YELLOW_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Yellow matchs with Lime  Red  Black  Gray  Cyan  Green.mp3')
        pygame.mixer.music.queue('Yellow matchs with Lime  Red  Black  Gray  Cyan  Green.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def CYAN_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Cyan matchs with Yellow  Red  White  Gray.mp3')
        pygame.mixer.music.queue('Cyan matchs with Yellow  Red  White  Gray.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def MAGENDA_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Magenda matchs with Green  Blue  Purple.mp3')
        pygame.mixer.music.queue('Magenda matchs with Green  Blue  Purple.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
    
    def SILVER_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Sliver matchs with Green  Blue  Purple  Red.mp3')
        pygame.mixer.music.queue('Sliver matchs with Green  Blue  Purple  Red.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def GRAY_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Gray matchs with Yellow  Blue  Cyan  Maroon  Olive  Skyblue.mp3')
        pygame.mixer.music.queue('Gray matchs with Yellow  Blue  Cyan  Maroon  Olive  Skyblue.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def MAROON_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Maroon matchs with White  Gray  Teal  Olive.mp3')
        pygame.mixer.music.queue('Maroon matchs with White  Gray  Teal  Olive.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def OLIVE_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Olive matchs with Red  Gray  Maroon  Purple Navy.mp3')
        pygame.mixer.music.queue('Olive matchs with Red  Gray  Maroon  Purple Navy.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def GREEN_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Green matchs with Black Lime  Blue  Yellow  Magenda  Silver Skyblue.mp3')
        pygame.mixer.music.queue('Green matchs with Black Lime  Blue  Yellow  Magenda  Silver Skyblue.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def PURPLE_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Purple matchs with Black  Lime  Blue  Yellow  Magenda  Silver.mp3')
        pygame.mixer.music.queue('Purple matchs with Black  Lime  Blue  Yellow  Magenda  Silver.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def TEAL_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Teal matchs with Maroon  Navy.mp3')
        pygame.mixer.music.queue('Teal matchs with Maroon  Navy.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
     
    def NAVY_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Navy matchs with Teal  Olive.mp3')
        pygame.mixer.music.queue('Navy matchs with Teal  Olive.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
        
    def SKYBLUE_MATCHS(self, image, hsv, image_det=True):
        pygame.mixer.init()
        pygame.mixer.music.load('Skyblue matchs with Black  Gray  Purple.mp3')
        pygame.mixer.music.queue('Skyblue matchs with Black  Gray  Purple.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                   continue

        return image
    

    def ImageDetection(self, imagePath, Black=False, White=False, Red=False, Lime=False, Blue=False,
                       Yellow=False, Cyan=False, Magenda=False, Silver=False, Gray=False, Maroon=False,
                       Olive=False, Green=False, Purple=False, Teal=False, Navy=False, Skyblue=False, All=False,Match=False):
        image = cv2.imread(imagePath)
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        if Black == True or All == True:
            image = self.black_detection(image, img_hsv, image_det=True)
            image = self.BLACK_MATCHS(image, img_hsv, image_det=True)
        if White == True or All == True:
            image = self.white_detection(image, img_hsv, image_det=True)
            image = self.WHITE_MATCHS(image, img_hsv, image_det=True)
        if Red == True or All == True:
            image = self.red_detection(image, img_hsv, image_det=True)
            image = self.RED_MATCHS(image, img_hsv, image_det=True)
            
        if Lime == True or All == True:
            image = self.lime_detection(image, img_hsv, image_det=True)
            image = self.LIME_MATCHS(image, img_hsv, image_det=True)
        if Blue == True or All == True:
            image = self.blue_detection(image, img_hsv, image_det=True)
            image = self.BLUE_MATCHS(image, img_hsv, image_det=True)
        if Yellow == True or All == True:
            image = self.yellow_detection(image, img_hsv, image_det=True)
            image = self.YELLOW_MATCHS(image, img_hsv, image_det=True)
        if Cyan == True or All == True:
            image = self.cyan_detection(image, img_hsv, image_det=True)
            image = self.CYAN_MATCHS(image, img_hsv, image_det=True)
        if Magenda == True or All == True:
            image = self.magenda_detection(image, img_hsv, image_det=True)
            image = self.MAGENDA_MATCHS(image, img_hsv, image_det=True)
        if Silver == True or All == True:
            image = self.silver_detection(image, img_hsv, image_det=True)
            image = self.SILVER_MATCHS(image, img_hsv, image_det=True)
        if Gray == True or All == True:
            image = self.gray_detection(image, img_hsv, image_det=True)
            image = self.GRAY_MATCHS(image, img_hsv, image_det=True)
        if Maroon == True or All == True:
            image = self.maroon_detection(image, img_hsv, image_det=True)
            image = self.MAROON_MATCHS(image, img_hsv, image_det=True)
        if Olive == True or All == True:
            image = self.olive_detection(image, img_hsv, image_det=True)
            image = self.OLIVE_MATCHS(image, img_hsv, image_det=True)
        if Green == True or All == True:
            image = self.green_detection(image, img_hsv, image_det=True)
            image = self.GREEN_MATCHS(image, img_hsv, image_det=True)
        if Purple == True or All == True:
            image = self.purple_detection(image, img_hsv, image_det=True)
            image = self.PURPLE_MATCHS(image, img_hsv, image_det=True)
        if Teal == True or All == True:
            image = self.teal_detection(image, img_hsv, image_det=True)
            image = self.TEAL_MATCHS(image, img_hsv, image_det=True)
        if Navy == True or All == True:
            image = self.navy_detection(image, img_hsv, image_det=True)
            image = self.NAVY_MATCHS(image, img_hsv, image_det=True)
        if Skyblue == True or All == True:
            image = self.skyblue_detection(image, img_hsv, image_det=True)
            image = self.SKYBLUE_MATCHS_MATCHS(image, img_hsv, image_det=True)


        
        #################### Matching ####################
        if Black == True : 
            if White == True or Green == True or Yellow == True or Red == True or Skyblue == True :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)         
            elif Purple == True  or Navy == True or Teal == True or Olive == True or Maroon == True or Gray == True or Silver == True or Magenda == True or Cyan == True or Blue == True or Lime == True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif White == True : 
            if Black == True or Red == True or Blue == True or Cyan == True or Maroon == True  :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif Purple == True or Skyblue == True or Navy == True or Teal == True or Olive == True or Gray == True or Silver == True or Magenda == True  or Green == True or Lime == True or Yellow == True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Red == True : 
            if Black == True or Yellow == True or Blue == True or Green == True or Cyan == True or Silver == True or Olive == True or Purple == True:
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)      
            elif  Skyblue == True or Navy == True or Teal == True  or Maroon == True or Gray == True  or Magenda == True   or Lime == True  :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Lime == True : 
            if  Yellow == True  or Green == True :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)      
            elif Purple == True or Skyblue == True or Navy == True or Teal == True or Olive == True or Maroon == True or Gray == True or Silver == True or Magenda == True or Cyan == True  or Lime == True  :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Blue == True : 
            if  White == True  or Red == True or Green == True  or Gray == True or Magenda == True or Silver == True or Purple == True :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif Skyblue == True or Navy == True or Teal == True or Olive == True or Maroon == True or Black == True   or Cyan == True  or Lime == True or Yellow == True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Yellow == True : 
            if  Lime == True  or Red == True or Black == True  or Gray == True or Cyan == True  or Green == True:
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif Purple == True or Skyblue == True or Navy == True or Teal == True or Olive == True or Maroon == True or Silver == True or Magenda == True   or Blue == True or White == True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Cyan == True : 
            if  Yellow == True  or Red == True or White == True  or Gray == True  :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)        
            elif Purple == True or Skyblue == True or Navy == True or Teal == True or Olive == True or Maroon == True or Green == True or Silver == True or Magenda == True or Cyan == True  or Blue == True or Lime == True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Magenda == True : 
            if  Green == True  or Blue == True or Purple == True   :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)      
            elif  Skyblue == True or Navy == True or Teal == True or Olive == True or Maroon == True or Silver == True or Cyan == True  or Lime == True or Gray == True or Yellow == True or Black == True or White == True or Red == True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Silver == True : 
            if  Green == True  or Blue == True or Purple == True  or Red == True  :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif  Skyblue == True or Navy == True or Teal == True or Olive == True or Maroon == True  or Cyan == True  or Lime == True or Gray == True or Yellow == True or Black == True or White == True or Magenda== True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Gray == True : 
            if  Yellow == True  or Blue == True or Cyan == True or Maroon == True or Olive == True or Skyblue == True:
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)      
            elif  Navy == True or Teal == True or Lime == True  or Black == True or White == True or Magenda== True or Red== True or Silver== True or Green== True or Purple== True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Maroon == True : 
            if  White == True  or Gray == True or Teal == True or Olive == True :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif  Skyblue == True or Navy == True or Purple== True  or Green == True   or Lime == True  or Black == True or Red == True or Blue== True or Yellow== True or Silver== True or Cyan== True or Magenda== True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Olive == True : 
            if  Red == True  or Gray == True or Maroon == True or Purple== True or Navy== True :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif  Skyblue == True or Teal == True or Green == True   or Lime == True  or Black == True or White == True or Blue== True or Yellow== True or Silver== True or Cyan== True or Magenda== True or Yellow== True:
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Green == True : 
            if  Black== True  or Lime == True or Blue == True or Yellow== True or Magenda== True or Silver== True or Skyblue == True :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif   Teal == True or Navy== True   or Purple == True  or Olive == True or Maroon == True or Gray== True or Cyan== True or Red== True or White== True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Purple == True : 
            if  Black== True  or Lime == True or Blue == True or Yellow== True or Magenda== True or Silver== True :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)      
            elif  Skyblue == True or Teal == True or Navy== True   or Green == True  or Maroon == True or Gray== True or Cyan== True or Yellow== True or Lime== True or Black== True or White== True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Teal == True : 
            if  Maroon== True  or Navy == True  :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif  Skyblue == True or Green == True or Olive== True   or Purple == True  or Maroon == True or Gray== True or Silver== True or Magenda== True or Cyan== True or Black== True or White== True or Red== True or Blue== True or Lime== True or Yellow== True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Navy == True : 
            if  Teal== True  or Olive== True  :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)        
            elif  Skyblue == True or Green == True or Purple == True  or Maroon == True or Gray== True or Silver== True or Magenda== True or Cyan== True or Black== True or White== True or Red== True or Blue== True or Lime== True or Yellow== True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        elif Skyblue == True : 
            if  Black== True  or Gray== True or Purple== True  :
                Match == True
                image = self.Match_detection(image, img_hsv, image_det=True)       
            elif  Navy== True or Green == True or Purple == True  or Maroon == True or Gray== True or Silver== True or Magenda== True or Cyan== True or Black== True or White== True or Red== True or Blue== True or Lime== True or Yellow== True or Olive== True :
                Match == True
                image = self.Not_Match_detection(image, img_hsv, image_det=True)

        # show 
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

   

           


