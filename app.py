from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

btn_state = True



def changeTheme():
	global btn_state
	if btn_state:
		root.config(background='#303841')
		theme_btn.config(bg='#303841')
		theme_btn.config(image=img1)
		lbl1.config(bg='#303841', text='Dark Mode')
		#messagebox.showinfo('Done', 'Dark Mode Activated!')
		btn_state = False
	else:
		root.config(background='white')
		theme_btn.config(bg='white')
		theme_btn.config(image=img2)
		lbl1.config(bg='white', text='Light Mode')
		#messagebox.showinfo('Done', 'Light Mode Activated!')
		btn_state = True


#main ui
root = Tk()
root.title('Theme Changer')
root.geometry('850x650+330+200')
#img = PhotoImage(file='logo.png')
#root.iconphoto(False, img)
root.resizable(0, 0)
root.config(bg='white')

#Images
img1 = Image.open('light.png')
img1 = img1.resize((70, 70))
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open('dark.png')
img2 = img2.resize((70, 70))
img2 = ImageTk.PhotoImage(img2)



theme_btn = Button(root, image=img2, fg='white', bg='white', font=('Calibri', 25), bd=0, command=changeTheme)
theme_btn.pack(pady=80)


lbl1 = Label(root, text='Light Mode', font=('Calibri', 60), fg='#39dfd7', bg='white')
lbl1.pack(pady=40)


root.mainloop()