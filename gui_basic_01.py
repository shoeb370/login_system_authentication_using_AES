from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("USER LOGIN SYSTEM USING AES OTP")
root.configure(bg="#000000")
#---------------------------Login part design pop up window-----------------------------
def login_win():
	def check_user_pass():
		e1 = user_id_entry.get()
		print(e1)

		
	#-----------login window design----------------------
	win = Toplevel()
	win.title("LOGIN AREA")
	win.geometry("500x500")
	win.configure(bg="#191919")
	#----------- login title design----------------
	Label(win, text="LOGIN DETAIL", bg="#191919", 
		fg="white", font="Helvetica 16 bold").grid(row=0, column=1)
	#-----------------------login label--------------------------------
	user_id = Label(win, text = 'Enter the user id: ',  bg="#191919", 
		fg = 'white',font="Helvetica 12 bold").grid(row = 1, column=0)
	user_id_entry = Entry(win, bg = 'white', fg = 'black',
		font="Helvetica 12 bold")
	user_id_entry.grid(row = 1, column=1)
	password =Label(win, text = 'Enter the password: ',  bg="#191919", 
		fg = 'white',font="Helvetica 12 bold").grid(row = 2, column=0)
	password_entry = Entry(win, bg = 'white', fg = 'black',
		font="Helvetica 12 bold", show = "*")
	password_entry.grid(row = 2, column=1)
	#-----------------------submit--------------------------------------
	
	submit = Button(win, text = "SUBMIT", bg ="#3b5998", fg = 'white',
		font = "Helvetica", command = check_user_pass).grid(row = 3, column=1)
	


def signup_wind():
	win = Toplevel()
	win.title("SIGN UP AREA")
	win.geometry("500x500")
	win.configure(bg="#191919")
	Label(win, text="ENTER USER DETAIL", bg="#191919", 
		fg="white", font="Helvetica 16 bold").grid(row=0, column=1)
	name = Label(win, text = 'Enter your fullname: ',  bg="#191919", 
		fg = 'white',font="Helvetica 12 bold").grid(row = 1, column=0)
	name_entry = Entry(win, bg = 'white', fg = 'black',
		font="Helvetica 12 bold").grid(row = 1, column=1)
	user_id = Label(win, text = 'Enter your id: ',  bg="#191919", 
		fg = 'white',font="Helvetica 12 bold").grid(row = 2, column=0)
	user_id_entry = Entry(win, bg = 'white', fg = 'black',
		font="Helvetica 12 bold").grid(row = 2, column=1)
	password = Label(win, text = 'Enter the password: ',  bg="#191919", 
		fg = 'white',font="Helvetica 12 bold").grid(row = 3, column=0)
	password_entry = Entry(win, bg = 'white', fg = 'black',
		font="Helvetica 12 bold").grid(row = 3, column=1)
	phone = Label(win, text = 'Enter your phone: ',  bg="#191919", 
		fg = 'white',font="Helvetica 12 bold").grid(row = 4, column=0)
	phone_entry = Entry(win, bg = 'white', fg = 'black',
		font="Helvetica 12 bold").grid(row = 4, column=1)
	email = Label(win, text = 'Enter your email id: ',  bg="#191919", 
		fg = 'white',font="Helvetica 12 bold").grid(row = 5, column=0)
	email_entry = Entry(win, bg = 'white', fg = 'black',
		font="Helvetica 12 bold").grid(row = 5, column=1)



#-----------------------after clicking login button (Main windows)-----------------
Label(root, text="WELCOME TO SYSTEM", bg="#000000", 
		fg="white", font="Helvetica 16 bold").grid(row=0, column=1)
login_btn = Button(root, text = "LOGIN", bg = "#191919", fg ="white",
font = "Helvetica_Neue",command = login_win )
login_btn.grid(row = 1, column = 1)
signup_btn = Button(root, text = "SIGN UP", bg = "#191919", fg ="white",
font = "Helvetica_Neue",command = signup_wind )
signup_btn.grid(row = 1, column = 2)
root.mainloop()
