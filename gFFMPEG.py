import os
from  tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Canvas
import ntpath
import subprocess

root=Tk()
root.title('gFFMPEG')
root.attributes("-fullscreen",True)
root.configure(bg='#009688')

t = Text(root,bg='#37474F',fg='white',height='10',width='50')
t.place(x=20,y=310)
def merge():
   file_path=filedialog.askopenfilenames(parent=root,title='Choose files')
   files = root.tk.splitlist(file_path)
   t.insert(END,'Selected Files are:\n')   
   for x in files:
     t.insert(END, x + '\n')
   z=t1.get()
   file1 = open("list.txt","a") 
   for i in files:
     file1.write("file "+"'"+i+"'\n")
   file1.close()
   w=extensions.get()
   zw=z+w
   subprocess.call('ffmpeg -f concat -safe 0 -i list.txt -c copy %s' % (zw))
   #os.system('ffmpeg -f concat -safe 0 -i list.txt -c copy '+z+w)
   os.system('del /f list.txt')
   os.system(z+w)

def remAudio():
   file_path=filedialog.askopenfilename(parent=root,title='Choose files')
   t.insert(END,'Selected Files are:\n')   
   t.insert(END, file_path + '\n')
   z=os.path.splitext(ntpath.basename(file_path))[0]
   z1=os.path.splitext(ntpath.basename(file_path))[1]
   
   os.system('ffmpeg -i '+file_path+' -c copy -an '+z+'_noaudio'+z1)
   os.system(z+'_noaudio'+z1)
   
def exits():
   root.quit()  


lb0=Label(root,text='gFFMPEG | GUI for ffmpeg',bg='#009688',fg='white',font=('Arial Bold',20))
lb0.place(x=20, y=10)
  
lbl=Label(root,text='1) Enter Output file name and press the button to select files and merge: \n\t',bg='#009688',fg='black',font=('Arial Bold',10))
lbl.place(x=20, y=50)
t1=Entry(root,width=25)
t1.place(x=30,y=87)
lb=Label(root,text='Select Extension:',bg='#009688',fg='black',font=('Arial Bold',9))
lb.place(x=20, y=120)
extensions=StringVar(root)
choices = { '.mp4','.mkv','.ts'}
extensions.set('.mp4') # set the default option
popupMenu = OptionMenu(root, extensions, *choices)
popupMenu.config(bg='#37474F',fg='white')
popupMenu["menu"].config(bg='#37474F',fg='white')
popupMenu.place(x=25,y=150)


btn = Button(root, text="Select & Merge",bg='#37474F',fg='white',command=merge)
btn.place(x=25, y=190)
#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
btn1 = Button(root, text="X",bg='#37474F',fg='white',command=exits,padx=10,pady=10)
btn1.place(relx = 1, x =-2, y = 2, anchor = NE)

lbl2=Label(root,text='2) Enter Output file name and press the button to select file and REMOVE AUDIO \n\t',bg='#009688',fg='black',font=('Arial Bold',10))
lbl2.place(x=20, y=230)
btn1 = Button(root, text="Select & Remove Audio",bg='#37474F',fg='white',command=remAudio)
btn1.place(x=25, y=260)




root.mainloop()

