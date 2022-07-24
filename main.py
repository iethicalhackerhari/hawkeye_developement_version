from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from employee import Employee
from train import Train
from face_recognizer import Face_Recognizer
import os

class Face_Recognition_System :
    def __init__(self, root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self. root.title("face Recogniton System ")
        
        # Background Image
        bg_img=Image.open(r"C:\Users\VIVOBOOK 14\Downloads\HawkEye-logo.png")
        bg_img=bg_img.resize ( (530, 410), resample=Image.LANCZOS )
        self.photoimg=ImageTk.PhotoImage(bg_img)
        
        
        bg_lbl=Label (self. root, image=self.photoimg)
        bg_lbl.place(x=500, y=210, width=530, height=410)
        
        # Title
        title = Label(self.root, text="Automatic Breach Detection System", font=(20))
        title.place(x=0,y=0, width=1530, height=40)
 
        # Employee Button
        emp_img=Image.open(r".\Assets\person.jpg")
        emp_img=emp_img.resize( (180, 180),  resample=Image.LANCZOS )
        self.photoimg1=ImageTk.PhotoImage(emp_img)
        
        emp__btn = Button( self.root,command=self.employee_details, image=self.photoimg1)
        emp__btn.place(x=200,y=100, width=180, height=180)
        emp_1=Button( self.root,command=self.employee_details, text="Employee Details", cursor="hand2", font=("times new roman", 15, "bold"))
        emp_1.place (x=200, y=260, width=180, height=40)
        
        # Face Recognition Button
        fr_img=Image.open(r".\Assets\face_recognition.jpg")
        fr_img=fr_img.resize( (180, 180),  resample=Image.LANCZOS )
        self.photoimg2=ImageTk.PhotoImage(fr_img)
        
        fr__btn = Button(self.root,command=self.recognize, image=self.photoimg2)
        fr__btn.place(x=600,y=100, width=180, height=180)
        fr_1=Button(self.root, text="Face Recognisation", command=self.recognize,cursor="hand2", font=("times new roman", 15, "bold"))
        fr_1.place (x=600, y=260, width=180, height=40)
        
        # Train Button
        train_img=Image.open(r".\Assets\person.jpg")
        train_img=train_img.resize( (180, 180),  resample=Image.LANCZOS )
        self.photoimg3=ImageTk.PhotoImage(train_img)
        
        train__btn = Button(self.root,command=self.train_dataset, image=self.photoimg3)
        train__btn.place(x=1000,y=100, width=180, height=180)
        train_1=Button(self.root,command=self.train_dataset, text="Train", cursor="hand2", font=("times new roman", 15, "bold"))
        train_1.place (x=1000, y=260, width=180, height=40)
        
        # Photos Button
        photos_img=Image.open(r".\Assets\photos.webp")
        photos_img=photos_img.resize( (180, 180),  resample=Image.LANCZOS )
        self.photoimg4=ImageTk.PhotoImage(photos_img)
        
        photos__btn = Button(self.root, image=self.photoimg4)
        photos__btn.place(x=200,y=320, width=180, height=180)
        photos_1=Button(self.root,command=self.open_photos, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"))
        photos_1.place (x=200, y=480, width=180, height=40)

        
 
    def employee_details (self) :
        self.new_window=Toplevel( self. root)
        self.app=Employee(self. new_window)
    
    def train_dataset (self) :
        self.new_window=Toplevel( self. root)
        self.app=Train(self. new_window)  
 

    def recognize (self) :
        self.new_window=Toplevel( self. root)
        self.app=Face_Recognizer(self. new_window) 
 
 
    def open_photos(self):
      os.startfile('data')  
 
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop ()