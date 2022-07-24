import threading
import email
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import  numpy as np

class Face_Recognizer:
    def __init__(self, root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self. root.title("face Recogniton System ")
        
        btn_train = Button(root, text="Face Recognizer", command=self.face_recog )
        btn_train.place(x=200, y=200)
        
        
    def face_recog(self):
        def draw_boundray(img, classifier, scale_factor, min_neighbours, color, text, classiFier) :
            gray_image=0
            features=[]
            fetched_emails=[]
            try:
                gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image, scale_factor, min_neighbours)
            except Exception as e:
                print(e)
            
            coord=[]
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255,0),3)
                id, prediction=classiFier.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100* (1-prediction/300)))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hawkeye")
                my_cursor = conn.cursor()
                
                my_cursor.execute("SELECT name from employee WHERE emp_id="+str(id))
                fetch_name=my_cursor.fetchone()
                fetch_name='+'.join(fetch_name)
                
                my_cursor.execute("SELECT email from employee WHERE emp_id="+str(id))
                fetch_email=my_cursor.fetchone()

                
                # def func():
                #     if  fetch_email in fetched_emails == True:
                #         pass
                #     else:
                #         fetched_emails.append(fetch_email)
                #         print(fetch_email)
                #         func.__code__ = (lambda:None).__code__
                
                # func()
                if confidence> 77:
                    cv2.putText(img, f"Name : {fetch_name}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0,0),3)
                else:
                    cv2.rectangle (img ,(x, y), (x+w, y+h), (0,0, 255), 3)
                    cv2. putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0),3)
                coord=[x,y,w,h]
                    
            return coord
        
        def recognize (img, classiFier, faceCascade) :
            coord=draw_boundray(img, faceCascade, 1.1, 10,(255, 255, 255), "Face",classiFier)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        classiFier=cv2.face.LBPHFaceRecognizer_create()
        classiFier.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret, frame=video_cap.read()
            frame=recognize(frame, classiFier, faceCascade)
        
            cv2.imshow( "Welcome To face Recognition", frame)
            if cv2.waitKey(1)==13 :
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognizer(root)
    root.mainloop ()