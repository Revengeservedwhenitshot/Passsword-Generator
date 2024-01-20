import string
import random
from tkinter import *
from PIL import ImageTk,Image


root = Tk()

#--- IMAGE DECLARING
logo_image = ImageTk.PhotoImage(Image.open("D:\PYTHON\PASSWORD GENERATOR.png"))
lock_image = ImageTk.PhotoImage(Image.open("D:\PYTHON\Lock.png"))


#ESTABLIST MAIN WINDOW
root.title('PASSWORD')
root.iconbitmap('D:\PYTHON\icon.ico')
width_of_window = 800
height_of_window = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = int((screen_width/2)- (width_of_window/2))
y_coordinate = int((screen_height/2)- (height_of_window/2))

root.geometry(f'{width_of_window}x{height_of_window}+{x_coordinate}+{y_coordinate}')
root.resizable(width=False,height=False)
#==============================================================================
#CREATE NEW INNER WINDOW
class WindowChange(Frame):
	def __init__(self,the_window):
		super().__init__()
		self["height"]=500
		self["width"]=800
		self["bg"]='black'
		self["borderwidth"]=5

#CHARACTER SELECTION CODE/BUTTON
def generate_password():
	global generated_label
	inner_login_box.place_forget()
	generated_box.place(x=48,y=56)


	quant = int(length_entry.get())
	lowlist = [item for item in string.ascii_lowercase]
	upplist = [item for item in string.ascii_uppercase]
	numlist = [item for item in string.digits]
	spezlist = [item for item in string.punctuation]
	selection_list = []

	if lowvar.get()==1:
		for item in lowlist:
			selection_list.append(item)
	if uppvar.get()==1:
		for item in upplist:
			selection_list.append(item)
	if numvar.get()==1:
		for item in numlist:
			selection_list.append(item)
	if specvar.get()==1:
		for item in spezlist:
			selection_list.append(item)

	password = ''.join([random.choice(selection_list) for item in range(quant)])
	
	last_label = Label(generated_box,text='Your Randomly Selected Password Is:',font='Arial 26',bg='grey33',fg='white')
	last_label.place(x=50,y=50)

	generated_label = Label(generated_box,text=password,font='Arial 28 bold',bg='grey33',fg='gray7')
	generated_label.place(relx=.5,rely=.5,anchor="center")

	home_button = Button(generated_box,text='Create New',font='Arial 12 bold',width=10,height=2,bg='grey55',fg='white',command=create_new)
	home_button.place(relx=.42,rely=.80)

def create_new():
	global generated_label
	generated_label.place_forget()
	length_entry.delete(0,'end')
	lowercase_letters.deselect()
	uppercase_letters.deselect()
	numbers_chars.deselect()
	special_chars.deselect()
	generated_box.place_forget()
	inner_login_box.place(x=48,y=56)


#OUTER LAYER, TO STAY CONISTENT IN BOTH WINDOWS
login_screen = WindowChange(root)
login_screen.pack()

banner = Label(login_screen,image=logo_image,relief='raised',bg='khaki')
banner.place(x=75,y=0)

#--------------------------------------------------------------------------
#INNER LOGIN CONTAINER (PARAMETER SELECTION SCREEN)

inner_login_box = Frame(login_screen,height=400,width=700,bg='gray',relief='groove',borderwidth=12)
inner_login_box.place(x=48,y=56)

lock_Label = Label(inner_login_box,image=lock_image,bg='grey33')
lock_Label.place(x=415,y=60)

paramaters_label = Label(inner_login_box,text='STRONG PASSWORD OPTIONS',borderwidth=2,relief='solid',font="Arial 16 bold",bg='grey33',fg='white')
paramaters_label.place(x=35,y=60)

character_length_label = Label(inner_login_box,text='CHARACTER LENGTH',font='Arial 18 bold',bg='gray',fg='black')
character_length_label.place(x=80,y=110)

length_entry = Entry(inner_login_box,width=5)
length_entry.place(x=185,y=140)

lowvar = IntVar()
lowercase_letters = Checkbutton(inner_login_box,text='a-z',font="Arial 15 bold",bg='gray',variable=lowvar)
lowercase_letters.place(x=80,y=180)

uppvar = IntVar()
uppercase_letters = Checkbutton(inner_login_box,text='A-Z',font="Arial 15 bold",bg='grey',variable=uppvar)
uppercase_letters.place(x=220,y=180)

numvar = IntVar()
numbers_chars = Checkbutton(inner_login_box,text='0-9',font="Arial 15 bold",bg='grey',variable=numvar)
numbers_chars.place(x=80,y=230)

specvar=IntVar()
special_chars = Checkbutton(inner_login_box,text='Special character',font="Arial 15 bold",bg='gray',variable=specvar)
special_chars.place(x=220,y=230)

generate_button = Button(inner_login_box,text='GENERATE PASSWORD',font='Arial 20 bold',fg='navy blue',borderwidth=5,relief='raised',command=generate_password)
generate_button.place(x=40,y=280)

# SCREEN THAT COMES AFTER 'GENERATE PASSWORD' DECLARATION
generated_box = Frame(login_screen,height=400,width=700,bg='grey33',relief='groove',borderwidth=12)


root.mainloop()