from tkinter import*
from PIL import ImageTk, Image
from matplotlib import image
mansLogs=Tk()
mansLogs.title("atteli")
mansLogs.geometry("650x650")
mansLogs.configure(bg="beige")


def back(imgNumber):
  global myLabel,btnForward,btnBack
  myLabel.grid_forget() #aizmirst attēlu
  myLabel=Label(image=imageList[imgNumber-1])
  myLabel.grid(row=0,column=0,columnspan=3)
  btnBack=Button(mansLogs,text="<<",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",command=lambda:back(imgNumber-1))
  btnForward=Button(mansLogs,text=">>",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",command=lambda:forward(imgNumber-1))
  if imgNumber==1:
    btnBack=Button(mansLogs,text="<<",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",state=DISABLED)
  btnBack.grid(row=1,column=0)
  btnForward.grid(row=1,column=2)
  return 0

def forward(imgNumber):
  global myLabel,btnForward,btnBack
  myLabel.grid_forget() #aizmirst attēlu
  myLabel=Label(image=imageList[imgNumber+1])
  myLabel.grid(row=0,column=0,columnspan=3)
  btnBack=Button(mansLogs,text="<<",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",command=lambda:back(imgNumber+1))
  btnForward=Button(mansLogs,text=">>",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",command=lambda:forward(imgNumber+1))
  if imgNumber==5:
    btnForward=Button(mansLogs,text=">>",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",state=DISABLED)
  btnBack.grid(row=1,column=0)
  btnForward.grid(row=1,column=2)
  return 0


img1=ImageTk.PhotoImage(Image.open("1.jpg").resize((600,600),Image.ANTIALIAS))
img2=ImageTk.PhotoImage(Image.open("2.jpeg").resize((600,600),Image.ANTIALIAS))
img3=ImageTk.PhotoImage(Image.open("3.jpg").resize((600,600),Image.ANTIALIAS))
img4=ImageTk.PhotoImage(Image.open("4.jpg").resize((600,600),Image.ANTIALIAS))
img5=ImageTk.PhotoImage(Image.open("5.jpg").resize((600,600),Image.ANTIALIAS))
img6=ImageTk.PhotoImage(Image.open("6.jpg").resize((600,600),Image.ANTIALIAS))
img7=ImageTk.PhotoImage(Image.open("7.jpg").resize((600,600),Image.ANTIALIAS))

imageList=[img1,img2,img3,img4,img5,img6,img7]
myLabel=Label(image=img1)
myLabel.grid(row=0,column=0,columnspan=3)
btnBack=Button(mansLogs,text="<<",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",state=DISABLED,command=lambda:back(0))
btnQuit=Button(mansLogs,text="IZIET",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",command=mansLogs.quit)
btnForward=Button(mansLogs,text=">>",bg="dark khaki",fg="khaki",activebackground="NavajoWhite4",command=lambda:forward(0))

btnBack.grid(row=1,column=0)
btnQuit.grid(row=1,column=1)
btnForward.grid(row=1,column=2)


mansLogs.mainloop()