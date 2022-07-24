from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import  numpy as np

class Train :
    def __init__(self, root) :
        self.root=root
        self.root.geometry("1530x790+0+0")
        self. root.title("face Recogniton System ")
        
        btn_train = Button(root, text="Train" , command=self.train_classifier)
        btn_train.place(x=200, y=200)
        
        
    def train_classifier ( self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir) ]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert ("L") #Gray scale image
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split(".")[1])
                                                         
            faces.append(imageNp)
            ids.append (id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey (1) == 13
        ids=np.array(ids)
        
        classiFier = cv2.face.LBPHFaceRecognizer_create()
        classiFier.train(faces, ids)
        classiFier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Training completed.")
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop ()