from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from tkcalendar import Calendar



connection = mysql.connector.connect( host = "localhost" , user = "root" , password = "" , database = "Exam" )
cursor = connection.cursor()
class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		self._frame = None
		self.title(" Exam Management ")
		self.switch(Menu)
		self.geometry('700x700')
		self.config(bg = "light blue")

	def switch(self, frame_class,list=[]):
		"""Destroys current frame and replaces it with a chosen by the user"""
		new_frame = frame_class(self,list)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()
		################################################################################################################################################################
class Menu(Frame):
	"""Main menu"""
	def __init__(self, master,role):
		
		Frame.__init__(self, master)
		

		self.config(bg = "light blue")
		"""Frame widgets"""
		label = Label(self, font = ('elephant',(30)),text = "Exam Management !\n", bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 20)

		button = Button(self, text = "Login as Administrator",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Login,["administrator"]))
		button.pack(padx = 10, pady = 10)
		button2 = Button(self, text = "Login as Student",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Login,["student"]))
		button2.pack(padx = 10, pady = 10)
		button6 = Button(self, text = "Login as Professor ",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Login,["professor"]) )
		button6.pack(padx = 10, pady = 10)	
		button3 = Button(self, text = "Exit",font = ('Times new roman',(30)),bg = "white", width = 20, command = self.close)
		button3.pack(padx = 10, pady = 10)
		
	def close(self):
		"""Close the app"""
		self.destroy()
		exit()

class Login(Frame):
	def __init__(self, master,list):
		role = list[0]
		
		
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		def on_click():
			"""Checking data and writing the results"""
			user = entryUser.get()
			user_pass = entryPass.get()
			entryUser.delete(0,END)
			entryPass.delete(0,END)
			try :
				query = f"Select pass from {role} where id = \"{user}\""
				cursor.execute(query)
				result = cursor.fetchall()
				if result == []:
					messagebox.showerror("Error", "Please enter correct data!")
				else:
					password = result[0][0]
					if password == user_pass:
						
						if role == "student":
							master.switch(Student,[user])
						elif role == "administrator":
							master.switch(Administrator,[user])
						elif role == "professor":
							master.switch(Professor,[user])
					else :
						messagebox.showerror("Error", "Please enter correct data!")
			except:
				messagebox.showerror("Error", "Please enter correct data!")
			
				
		def forgot_on_click():
			master.switch(Forgot1,[role])

		"""Frame widgets"""
		label = Label(self, text ="Enter the Details  ",font = ('Elephant',(20)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		# user input, product
		label2 = Label(self, text = "Username: ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack()
		entryUser = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryUser.pack(padx = 10, pady =10)
		
		label3 = Label(self, text = "Password: ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack()
		entryPass = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryPass.pack(padx = 10, pady =5)
		
		forget = Button(self, text = "Forgot password",font = ('times new roman',(20)), width = 15, command = forgot_on_click)
		forget.pack(padx = 10, pady = 25)
		
		login = Button(self, text = "Login",font = ('times new roman',(25)), width = 8, command = on_click)
		login.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Menu))
		self.button.pack(padx = 10, pady = 10)
		################################################################################################################################################################
		
class Forgot1(Frame):
	def __init__(self, master,list):
		
		role = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		def on_click():
		
			user = entryuser.get()
			dob = DOB.get_date()
			try :
				query = f"Select DOB from {role} where id = \"{user}\""
				cursor.execute(query)
				result = cursor.fetchall()
				
				
				
				if result == []:
					
					messagebox.showerror("Error", "Please enter correct data!")
				else:
					if result[0][0] == dob :
						master.switch(Forgot2,[role,user])
						
					else :
						messagebox.showerror("Error", "Please enter correct data!")
			except :
				messagebox.showerror("Error", "This User is not Included!")
			
		label = Label(self, text ="Reset the Password  ",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		
		label1 = Label(self, text ="Enter the UserId ",font = ('Elephant',(20)), bg = "light blue", fg = "black")
		label1.pack()
		
		entryuser = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryuser.pack()
		entryuser.configure(state ='normal')
		label2 = Label(self, text ="Select Birth Date ",font = ('Elephant',(20)), bg = "light blue", fg = "black")
		label2.pack()
		DOB = Calendar(self,selectmode = 'day' , year = 2001 , month = 5 , day = 22 )
		DOB.pack(pady = 20)
		submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 8, command = on_click)
		submit.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Menu))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
class Forgot2(Frame):
	def __init__(self, master,list):
		role = list[0]
		user = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		def on_click():
			password1= entrypass.get()
			password2 = entrypass1.get()
			
			if password1 == "":
				messagebox.showerror("Error", "Password cannot be NULL!")
			elif password1 != password2:
				messagebox.showerror("Error", "Both password didnt match!")
			else :
				try:
					query = f"UPDATE {role} Set pass = \"{password1}\" where id = \"{user}\" "
					cursor.execute(query)
					connection.commit()
					messagebox.showinfo( "Status" , "Password Resetted ")
					entrypass1.delete(0,END)
					entrypass.delete(0,END)
				except:
					messagebox.showerror("Error", "Retry Again!")
				

		label = Label(self, text ="Reset the Password  ",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		
		label5 = Label(self, text ="Enter the New Password",font = ('Elephant',(20)), bg = "light blue", fg = "black")
		label5.pack()
		entrypass = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entrypass.pack()
		
		label6 = Label(self, text ="Enter the New Password Again ",font = ('Elephant',(20)), bg = "light blue", fg = "black")
		label6.pack()
		entrypass1 = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entrypass1.pack()
		
		submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 8, command = on_click)
		submit.pack(padx = 10, pady = 10)
		
		
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 12, command = lambda: master.switch(Menu))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
	
		
		###################################################################################################################################################################
class Student(Frame):
	def __init__(self, master,list):
		
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		
		
		
		query = f"Select * from student where id = \"{user}\""
		cursor.execute(query)
		result = cursor.fetchall()
		message = f" \n\nStudent ID : {result[0][0]} \nStudent name : {result[0][1]} \nStudent Email : {result[0][2]} \nStudent_Department : {result[0][3]} \nDate of Birth : {result[0][4]} \nGender : {result[0][5]}"
		
		department = result[0][3]
		SEM = result[0][7]
		
		
		
		def enrolll():
			
			query = f"Select * from fees where s_id = \"{user}\" and semester = \"{SEM}\""
			cursor.execute(query)
			result = cursor.fetchall()
			if result[0][-2] == 0:
				messagebox.showinfo("Info" ,"Fees is to be Remaining")
				return 
				
			query = f"Select id , name , credits , prof_id from course,teaches where course.id = teaches.course_id and dep = \"{department}\" and semester = \"{SEM}\""
			cursor.execute(query)
			result = cursor.fetchall()
			final = []
			course = []
			for list in result:
				c_id = list[0]
				
				query = f"Select * from enrolled where course_id = \"{c_id}\" and s_id = \"{user}\" and sem = {SEM} "
				cursor.execute(query)
				res = cursor.fetchall()
				if len(res) == 0:
					message = f"{list[0]}: {list[1]}  Credits:{list[2]} Proff:{list[3]} Sem:{SEM} "
					final.append(message)
					course.append(list[0])
			if len(final) == 0:
				messagebox.showinfo("Info" , "No new course has been added")
			else:
				master.switch(Enroll,[user,final,course,SEM])
				
		def feeed():
			query = f"Select flag from student where id = \"{user}\" "
			cursor.execute(query)
			result = cursor.fetchall()
			if result[0][0] == "0":
				messagebox.showinfo("Info" ,"Not Enabled by Administrator")
				return 
			query = f"Select course_id from enrolled where s_id = \"{user}\" and sem = {SEM} "
			cursor.execute(query)
			result = cursor.fetchall()
			if len(result) == 0:
				messagebox.showinfo("Info","You have not enrolled any course ")
			else:
				master.switch(Feedback,[user,result,SEM])
				
		label = Label(self, text ="Student Details  ",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		details.pack(padx = 10 , pady = 10, anchor = 'w')
		
		details.configure(state ='normal')
		details.insert(END,message)
		details.configure(state ='disabled')
		
		Edit = Button(self, text = "Edit Profile ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_Profile,["student",user]))
		Edit.pack(padx = 30, pady = 10,side = LEFT)
		academics = Button(self, text = "Academics ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Academics,[user,SEM]))
		academics.pack(padx = 10, pady = 10,side = LEFT)
		
		Fees = Button(self, text = "Fees",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(FEES,[user,SEM]))
		Fees.pack(padx = 10, pady = 10,side = LEFT)
		
		feedback = Button(self, text = "Feedback",font = ('Times new roman',(20)), width = 15, command = feeed)
		feedback.pack(padx = 30, pady = 10, side = LEFT)
		
		New_Exam = Button(self, text = "Enroll",font = ('Times new roman',(20)), width = 15, command = enrolll)
		New_Exam.pack(padx = 10, pady = 10, side = LEFT)
		
		self.button = Button(self, text = "Logout",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Menu))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
		
class Edit_Profile(Frame):
	def __init__(self, master,list):
		role = list[0]
		user = list[1]
		
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		def on_click():
			name = entryName.get()
			dob = DOB.get_date()
			email = EmailEntry.get()
			if role == "administrator":
				pass
			else:
				Dep = DepEntry.get()
			Pass = PassEntry.get()
			
			try :
				if role == "administrator":
					query = f"UPDATE {role} Set name = \"{name}\" , email = \"{email}\" ,pass = \"{Pass}\",DOB = \"{dob}\" where id = \"{user}\" "
				else:
					query = f"UPDATE {role} Set name = \"{name}\" , email = \"{email}\" , dep = \"{Dep}\" ,pass = \"{Pass}\",DOB = \"{dob}\" where id = \"{user}\" "
				cursor.execute(query)
				connection.commit()
				messagebox.showinfo( "Status" , " Changes are Saved !")
			except:
				messagebox.showerror("Error", f"{Error}")
				
		def next():
			if role == "student":
				master.switch(Student,[user])
			elif role == "professor":
				master.switch(Professor,[user])
			elif role == "administrator":
				master.switch(Administrator,[user])
				
		query = f"Select * from {role} where id = \"{user}\""
		cursor.execute(query)
		result = cursor.fetchall()
		
		
		label = Label(self, text =f"{role} Details  ",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 20)
		
		label2 = Label(self, text = f"User ID : {user}",font = ('times new roman',(20)), bg = "light blue", fg = "black")
		label2.pack(padx = 10, pady = 20)
		
		label3 = Label(self, text = "Name : ",font = ('times new roman',(20)), bg = "light blue", fg = "black")
		label3.pack()
		entryName = Entry(self, width = 30,font = ('times new roman',(20)), bg = "white")
		entryName.pack()
		entryName.insert(0,result[0][1])
		
		
		label4 = Label(self, text = "Email : ",font = ('times new roman',(20)), bg = "light blue", fg = "black")
		label4.pack()
		EmailEntry = Entry(self, width = 30,font = ('times new roman',(20)), bg = "white")
		EmailEntry.pack()
		EmailEntry.insert(0,result[0][2])
		
		if role == "student":
			label9 = Label(self, text = f"Semester : ",font = ('times new roman',(20)), bg = "light blue", fg = "black")
			label9.pack()
			sem = Entry(self, width = 30,font = ('times new roman',(20)), bg = "white")
			sem.pack()
			sem.configure(state = "normal")
			sem.insert(0,result[0][7])
			sem.configure(state = "disabled")
		
		if role == "administrator":
			pass
		else:
		
			label5 = Label(self, text = "Department : ",font = ('times new roman',(20)), bg = "light blue", fg = "black")
			label5.pack()
			DepEntry = Entry(self, width = 30,font = ('times new roman',(20)), bg = "white")
			DepEntry.pack()
			DepEntry.configure(state = "normal")
			DepEntry.insert(0,result[0][3])
			DepEntry.configure(state = "disabled")
		
		if role == "administrator":
			dob = result[0][3].split("/")
		else :
			dob = result[0][4].split("/")
		label7 = Label(self, text = "DOB : ",font = ('times new roman',(20)), bg = "light blue", fg = "black")
		label7.pack()
		DOB = Calendar(self,selectmode = 'day' , year = int(dob[2]) , month = int(dob[1]) , day = int(dob[0]) )
		DOB.pack(pady = 20)
		
		label6 = Label(self, text = "Password : ",font = ('times new roman',(20)), bg = "light blue", fg = "black")
		label6.pack()
		PassEntry = Entry(self, width = 30,font = ('times new roman',(20)), bg = "white")
		PassEntry.pack()
		if role == "administrator":
			PassEntry.insert(0,result[0][5])
		else:
			PassEntry.insert(0,result[0][6])
		
		
		submit = Button(self, text = "Save the chnages",font = ('times new roman',(20)), width = 20, command = on_click)
		submit.pack(padx = 10, pady = 10)
		

		self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = next)
		self.button.pack(padx = 50, pady = 50, side = BOTTOM) 
		#####################################################################################################################################################################################
		
class Professor(Frame):
	def __init__(self, master,list):
		
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		query = f"Select * from professor where id = \"{user}\""
		cursor.execute(query)
		result = cursor.fetchall()
		message = f"\n\nProfessor ID : {result[0][0]} \nProfessor name : {result[0][1]} \n Email : {result[0][2]} \nDepartment : {result[0][3]} \nDate of Birth : {result[0][4]} \nGender : {result[0][5]}"
		query = f"Select course_id , semester from teaches where prof_id = \"{user}\" "
		cursor.execute(query)
		result = cursor.fetchall()
		
		def on_click_att():
			if len(result) == 0:
				messagebox.showinfo("Info" ,"You don't have any Course under you ")
			else:
				master.switch(Add_Attendance,[user,result])
			
		def on_click_mar():
			final = []
			for tem in result:
				query = f"Select exam_id from exam where course_id = \"{tem[0]}\" and sem = \"{tem[1]}\" "
				cursor.execute(query)
				res = cursor.fetchall()
				if len(res) == 0:
					pass
				else:
					var = [res[0][0] , tem[0] , tem[1]]
					final.append(var)
				
			if len(final) == 0:
				messagebox.showinfo("Info" ,"There was not Exam for Course under you ")
			else:
				master.switch(Add_Marks,[user,final])
			
			
		label = Label(self, text ="Professor Details  ",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		details.pack(padx = 10 , pady = 10, anchor = 'w')
		
		details.configure(state ='normal')
		details.insert(END,message)
		details.configure(state ='disabled')
		
		Edit = Button(self, text = "Edit Profile ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_Profile,["professor",user]))
		Edit.pack(padx = 30, pady = 10,side = LEFT)
		
		Courses = Button(self, text = "Courses",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Proff_Courses,[user,result]))
		Courses.pack(padx = 10, pady = 10,side = LEFT)
		
		marks = Button(self, text = "Add marks",font = ('Times new roman',(20)), width = 15, command = on_click_mar)
		marks.pack(padx = 10, pady = 10,side = LEFT)
		
		atten = Button(self, text = "Add Attendance",font = ('Times new roman',(20)), width = 15, command = on_click_att)
		atten.pack(padx = 10, pady = 10,side = LEFT)
		
		self.button = Button(self, text = "Logout",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Menu))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
		#####################################################################################################################################################################################
		

class Proff_Courses(Frame):
	def __init__(self, master,list):
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		user = list[0]
		result = list[1]
	
		label = Label(self, text =f"Professor Courses",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 30)
		# user input, product
	
		output = Text(self, width = 40,font = ('times new roman',(25)), height = 20, wrap = WORD, bg = "white")
		output.pack()
		
		output.delete(0.0, END)
		
		if len(result) == 0:
			message = "\n\n\n \tCurrently don't have any Course "
		else:
			message = f"Total Courses : {len(result)} \n"
			for list in result:
				query = f" Select s_id from enrolled where course_id = \"{list[0]}\" and sem = {list[1]} "
				cursor.execute(query)
				res = cursor.fetchall()
				message += f" Course: {list[0]}  Semester: {list[1]}  Students: {len(res)} \n"
				
		output.configure(state = "normal")	
		output.insert(0.0,message)
		output.configure(state = "disabled")
		
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda : master.switch(Professor,[user]))
		self.button.pack(padx = 10, pady = 10)
class Add_Attendance(Frame):
	def __init__(self, master,list):
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		user = list[0]
		result = list[1]
	
		def next():
			
					
			temp = value_in.get()
			temp = temp.split()
			cours = temp[0]
			se = temp[-1]
			output = Text(self,height = 20, width = 30,font = ('times new roman',(20)), bg = "white")
			output.pack(padx = 30 ,pady = 20)
			def on_click():
				inpu = output.get(1.0,END)
				inpu = inpu[:-2]
				inpu = inpu.split("\n")
				
				for list in inpu:
					tem = str(list)
					tem = tem.split()
					query = f"Update enrolled Set attendance = \"{tem[1]}\" where course_id = \"{cours}\" and sem = {se} and s_id = \"{tem[0]}\" "
					cursor.execute(query)
					connection.commit()
				
				output.delete(0.0,END)
				messagebox.showinfo("Info","Successfully Submitted Attendance")
				
					
					
			query = f" Select s_id from enrolled where course_id = \"{cours}\" and sem = {se} "
			cursor.execute(query)
			res = cursor.fetchall()
			message = ""
			if len(res) == 0:
				messagebox.showinfo("Info" , "None student has enrolled in this course")
			else:
				for list in res:
					message += f"{list[0]} \n"
				
				output.insert(0.0,message)
				
			submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 8, command = on_click)
			submit.pack(padx = 30, pady = 10)
			
		
		    
			self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda : master.switch(Professor,[user]))
			self.button.pack(padx = 30, pady = 10)			

		
		att_list = []
		for list in result:
			message = f"{list[0]}  Sem- {list[1]}" 
			att_list.append(message)
		
		value_in = StringVar(self)
		value_in.set("  Select the Course and Sem ")
		question_menu = OptionMenu(self,value_in,*att_list ).pack(padx = 30 )
		
		ok = Button(self, text = "Add Attendance",font = ('Times new roman',(20)), width = 30, command = next)
		ok.pack(padx = 30, pady = 10)
		
class Add_Marks(Frame):
	def __init__(self, master,list):
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		user = list[0]
		final = list[1]
	
		def next():
			
					
			temp = value_in.get()
			temp = temp.split()
			exam_id = temp[0]
			exam_id = exam_id[:-1]
			output = Text(self,height=6, width = 30,font = ('times new roman',(20)), bg = "white")
			output.pack(padx = 30,pady = 20)
			def on_click():
				inpu = output.get(1.0,END)
				inpu = inpu[:-2]
				inpu = inpu.split("\n")
				for list in inpu:
					tem = str(list)
					tem = tem.split()
					
					query = f"Update result Set grade = \"{tem[1]}\" where exam_id = \"{exam_id}\"  and s_id = \"{tem[0]}\" "
					cursor.execute(query)
					connection.commit()
				
				output.delete(0.0,END)
				messagebox.showinfo("Info","Successfully Submitted Marks")
				
					
					
			query = f" Select s_id from result where exam_id = \"{exam_id}\" "
			cursor.execute(query)
			res = cursor.fetchall()
			message = ""
			if len(res) == 0:
				messagebox.showinfo("Info" , "None student has enrolled in this course")
			else:
				for list in res:
					message += f"{list[0]} \n"
				
				output.insert(0.0,message)
				
			submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 8, command = on_click)
			submit.pack(padx = 30, pady = 10)
			
		
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda : master.switch(Professor,[user]))
		self.button.pack(padx = 30, pady = 10,side = BOTTOM)			

		
		att_list = []
		for list in final:
			message = f"{list[0]}: {list[1]}  Sem- {list[2]}" 
			att_list.append(message)
		
		value_in = StringVar(self)
		value_in.set("  Select the Course and Sem ")
		question_menu = OptionMenu(self,value_in,*att_list ).pack(padx=30,pady = 10)
		
		ok = Button(self, text = "Add Marks",font = ('Times new roman',(20)), width = 20, command = next)
		ok.pack(padx = 30, pady = 10)
		

class Administrator(Frame):
	def __init__(self, master,list):
		
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		
		query = f"Select * from administrator where id = \"{user}\""
		cursor.execute(query)
		result = cursor.fetchall()
		message = f"\n\nAdministrator ID : {result[0][0]} \nName : {result[0][1]} \n Email : {result[0][2]} \nDepartment : {result[0][3]} \nDate of Birth : {result[0][4]} \nGender : {result[0][5]}"
		
		label = Label(self, text ="Administrator Details  ",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		details = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		details.pack(padx = 10 , pady = 10, anchor = 'w')
		
		details.configure(state ='normal')
		details.insert(END,message)
		details.configure(state ='disabled')
		
		Edit = Button(self, text = "Edit Profile ",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Edit_Profile,["administrator",user]))
		Edit.pack(padx = 30, pady = 10,side = LEFT)
		Manages = Button(self, text = "Manages",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Administrator_Management,[user]))
		Manages.pack(padx = 10, pady = 10,side = LEFT)
		
		feedback = Button(self, text = "Feedback_Status",font = ('Times new roman',(20)), width = 15, command = lambda:master.switch(feed_back,[user]))
		feedback.pack(padx = 30, pady = 10, side = LEFT)
		
		TeachingEntry = Button(self, text = "Teaching",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Teaching,[user]))
		TeachingEntry.pack(padx = 10, pady = 10, side = LEFT)
		
		New_Exam = Button(self, text = "New Exam",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Add_Exam,[user]))
		New_Exam.pack(padx = 10, pady = 10, side = LEFT)
		
		promote = Button(self, text = "Promote",font = ('Times new roman',(20)), width = 15, command = lambda: master.switch(Promote,[user]))
		promote.pack(padx = 10, pady = 10, side = LEFT)
		
		self.button = Button(self, text = "Logout",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Menu))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
		

class Teaching(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		
		def next():
			def on_click():
					cou = valuein.get()
					pro = value.get()
					sem = PassEntry.get()
					f = 0
					query = f"Insert into teaches values(\"{cou}\" , \"{pro}\" , {sem} )" 
					try :
						cursor.execute(query)
						connection.commit()
					except:
						f = 1
					if f == 1:
						messagebox.showerror("ERROR ",f"Something Went Wrong : {Error}")
					else:
						messagebox.showinfo("Info" , "Information Saved Successfully")
						
			de = value_in.get()
			
			label = Label(self, text ="Select Course",font = ('Elephant',(25)), bg = "light blue", fg = "black")
			label.pack(padx = 10, pady = 20)
		
			query = f"Select id from course where dep = \"{de}\" "
			cursor.execute(query)
			result = cursor.fetchall()
			att_list = []
			for i in result:
				att_list.append(i[0])
				
			query = f"Select id from professor where dep = \"{de}\" "
			cursor.execute(query)
			result = cursor.fetchall()
			at_list = []
			for i in result:
				at_list.append(i[0])
				
			if len(att_list) == 0:
				messagebox.showinfo("Info" , f"No Course in {de} Department")
			elif len(at_list) == 0:
				messagebox.showinfo("Info" , f"No Professor to teach in {de} Department")
			else:
				valuein = StringVar(self)
				valuein.set("  Select Course_id ")
				question_menu = OptionMenu(self,valuein,*att_list ).pack(pady = 20)
				
				label = Label(self, text ="Select Professor",font = ('Elephant',(25)), bg = "light blue", fg = "black")
				label.pack(padx = 10, pady = 20)
				
				
				value = StringVar(self)
				value.set("  Select Professor_id ")
				question_menu = OptionMenu(self,value,*at_list ).pack(pady = 20)
				
				label = Label(self, text ="Enter the Semester",font = ('Elephant',(25)), bg = "light blue", fg = "black")
				label.pack(padx = 10, pady = 20)
				PassEntry = Entry(self, width = 30,font = ('times new roman',(20)), bg = "white")
				PassEntry.pack()
				
				submit = Button(self, text = "Save the chnages",font = ('times new roman',(20)), width = 20, command = on_click)
				submit.pack(padx = 10, pady = 10)
				
				
					
					
		query = f"Select dep_name from department"
		cursor.execute(query)
		result = cursor.fetchall()
		
		attr_list = []
		for i in result:
			attr_list.append(i[0])
			
		self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda : master.switch(Administrator,[user]))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM) 
		
		label = Label(self, text ="Select Department ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 20)
		
		value_in = StringVar(self)
		value_in.set("  Select the Department ")
		question_menu = OptionMenu(self,value_in,*attr_list ).pack(pady = 20)
		
		ok = Button(self, text = "OK",font = ('Times new roman',(10)), width = 5, command = next)
		ok.pack(padx = 10, pady = 10)
			
		
class Add_Exam(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
	
		query = f"Select dep_name from department"
		cursor.execute(query)
		result = cursor.fetchall()
		
		def next():
			temp = value_in.get()
			query = f"Select id from course where dep = \"{temp}\" "
			cursor.execute(query)
			res = cursor.fetchall()
			if len(res) == 0:
				messagebox.showinfo("Info" , "This Department has not any Course")
			else:
				final = []
				for list in res:
					query = f"Select course_id,semester from teaches where course_id = \"{list[0]}\" "
					cursor.execute(query)
					var = cursor.fetchall()
					for i in var:
						message = f"{i[0]} {i[1]}"
						final.append(message)
				def next2():
					te = value_inside.get()
					te = te.split()
					cou = te[0]
					sem = te[1]
					
					label = Label(self, text ="Enter Exam_id :",font = ('Elephant',(20)), bg = "light blue", fg = "black")
					label.pack(padx = 10, pady = 10)
					
					entryExam_id = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
					entryExam_id.pack(pady = 10)
					
					label1 = Label(self, text ="classroom :",font = ('Elephant',(20)), bg = "light blue", fg = "black")
					label1.pack(padx = 10, pady = 10)
					
					entrybuilding = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
					entrybuilding.pack(pady = 10)
					
					label2 = Label(self, text ="Select Date ",font = ('Elephant',(20)), bg = "light blue", fg = "black")
					label2.pack()
					DOB = Calendar(self,selectmode = 'day' , year = 2001 , month = 5 , day = 22 )
					DOB.pack(pady = 10)
					
					label2 = Label(self, text ="time :",font = ('Elephant',(20)), bg = "light blue", fg = "black")
					label2.pack(padx = 10, pady = 10)
					entrytime = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
					entrytime.pack(pady = 10)
					
					att = []
					query = f"Select id from professor "
					cursor.execute(query)
					at = cursor.fetchall()
					def on_click_new():
						ex_id = entryExam_id.get()
						classroom = entrybuilding.get()
						tim = entrytime.get()
						dob = DOB.get_date()
						p_id = pro_in.get()
						query = f"Insert into exam values( \"{ex_id}\" , \"{cou}\" , {sem} , \"{dob}\" , \"{tim}\" ,\"{classroom}\" , \"{p_id}\") "
						cursor.execute(query)
						connection.commit()
						
						query = f" Select s_id from enrolled where course_id = \"{cou}\" and sem = {sem} "
						cursor.execute(query)
						res = cursor.fetchall()
						for v in res:
							query = f"Insert into result values( \"{ex_id}\" , \"{v[0]}\" , 0)"
							cursor.execute(query)
							connection.commit()
							
						messagebox.showinfo("Info" , "Exam was scheduled Successfully")
						entryExam_id.delete(0,END)
						classroom = entrybuilding.delete(0,END)
						tim = entrytime.delete(0,END)
						
					for va in at:
						att.append(va[0])
					pro_in = StringVar(self)
					pro_in.set("  Select the Supervisor ")
					question_menu = OptionMenu(self,pro_in,*att ).pack()
					
					submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 8, command = on_click_new)
					submit.pack(padx = 10, pady = 10)
					
				if len(final) == 0:
					messagebox.showinfo("Info" , "This Department has not working Course")
					
				else:
					value_inside = StringVar(self)
					value_inside.set("  Select the Course and Sem ")
					question_menu = OptionMenu(self,value_inside,*final ).pack()

					ok = Button(self, text = "ok",font = ('Times new roman',(10)), width = 5, command = next2)
					ok.pack(padx = 30, pady = 5)
				
			
			self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 8, command = lambda : master.switch(Administrator,[user]))
			self.button.pack(padx = 10, pady = 10)			
		label = Label(self, text ="Select Department ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 5)	
		att_list = []
		for list in result: 
			att_list.append(list[0])
		value_in = StringVar(self)
		value_in.set("  Select the Department ")
		question_menu = OptionMenu(self,value_in,*att_list ).pack(padx = 30 ,pady = 20)
		
		ok = Button(self, text = "ok",font = ('Times new roman',(10)), width = 5, command = next)
		ok.pack(padx=30 ,pady = 5)
		
class feed_back(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		def feeed_back():
			query = "Update student SET flag = 1 "
			cursor.execute(query)
			connection.commit()
			messagebox.showinfo("Info" , "Feedback is Enabled")
		
		label = Label(self, text =" Options ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 20)
		
		label2 = Button(self, text = "Enable Feedback",font = ('Times new roman',(25)),bg = "white", width = 15, command = feeed_back)
		label2.pack(padx = 30, pady = 20)
		
		view = Button(self, text = "View Feedback",font = ('Times new roman',(25)),bg = "white", width = 15, command = lambda : master.switch(View_Feedback,[user]))
		view.pack(padx = 30, pady = 20)
		
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 12, command = lambda: master.switch(Administrator,[user]))
		self.button.pack(padx = 50, pady = 50) 
class View_Feedback(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		
		def next():
			def next2():
				proff = value_in.get()
				query = f"Select message from feedback where prof_id = \"{proff}\" "
				cursor.execute(query)
				result = cursor.fetchall()
		
				message = f"Total feedback : {len(result)} \n\n"
				for list in result :
					message += f"{list[0]} \n"
					output.insert(0.0,message)
					
			depp = value_inside.get()
			query = f"Select id from professor  where dep = \"{depp}\" "
			cursor.execute(query)
			result = cursor.fetchall()
			at = []
			for name in result:
				at.append(name[0])
			
			value_in = StringVar(self)
			value_in.set("  Select the Professor ")
			question_menu = OptionMenu(self,value_in,*at).pack(padx = 30 ,pady = 20)
			ok = Button(self, text = "ok",font = ('Times new roman',(10)), width = 30, command = next2)
			ok.pack()
			
		
			def next2():
				proff = value_in.get()
				query = f"Select message from feedback where prof_id = \"{proff}\" "
				cursor.execute(query)
				result = cursor.fetchall()
		
				message = f"Total feedback : {len(result)} \n\n"
				for list in result :
					message += f"{list[0]} : {list[1]} \n"
					output.insert(0.0,message)
		
		
		attribute_list = []
		query = "select dep_name from department"
		cursor.execute(query)
		result = cursor.fetchall()
		for name in result:
			attribute_list.append(name[0])
		
		value_inside = StringVar(self)
		value_inside.set("  Select the Department  ")
		question_menu = OptionMenu(self,value_inside,*attribute_list).pack(padx = 30 ,pady = 10)
		ok = Button(self, text = "ok",font = ('Times new roman',(10)), width = 30, command = next)
		ok.pack()
		
		
		
		self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Administrator,[user]))
		self.button.pack(padx = 20, pady = 20 , side = BOTTOM) 
		
		output = Text(self, width = 40,font = ('times new roman',(25)), height = 16, wrap = WORD, bg = "white")
		output.pack(side = BOTTOM)
		
		output.delete(0.0, END)
		
		
		
		
class Administrator_Management(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		label = Label(self, text =" Overall Database ",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		
		label2 = Button(self, text = "Manage Students",font = ('Times new roman',(30)),bg = "white", width = 15, command = lambda: master.switch(Student_manage,[user]))
		label2.pack(padx = 30, pady = 20)
		
		label3= Button(self, text = "Manage Professor",font = ('Times new roman',(30)),bg = "white", width = 15, command = lambda: master.switch(Professor_manage,[user]))
		label3.pack(padx = 30, pady = 20)
		
		label4 = Button(self, text = "Manage Course",font = ('Times new roman',(30)),bg = "white", width = 15, command = lambda: master.switch(Course_manage,[user]))
		label4.pack(padx = 30, pady = 20)
		
		label5 = Button(self, text = "Manage Department",font = ('Times new roman',(30)),bg = "white", width = 15, command = lambda: master.switch(Department_manage,[user]))
		label5.pack(padx = 30, pady = 20)
		
		self.button = Button(self, text = "Back",font = ('times new roman',(30)), width = 12, command = lambda: master.switch(Administrator,[user]))
		self.button.pack(padx = 50, pady = 50) 

class Student_manage(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		label = Label(self, text =" Student Management",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		
		button = Button(self, text = "View details",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Details,["student",user]))
		button.pack(padx = 10, pady = 10)
		button2 = Button(self, text = "Add New",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Add_New,["student",user]))
		button2.pack(padx = 10, pady = 10)
		
		button6 = Button(self, text = "Modify",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda:master.switch(Modify,["student",user]))
		button6.pack(padx = 10, pady = 10)
		
		button7 = Button(self, text = "Delete",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Delete,["student",user]) )
		button7.pack(padx = 10, pady = 10)
		
		button4 = Button(self, text = "View Branchwise ",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(View_Branch,["student",user]) )
		button4.pack(padx = 10, pady = 10)
		button5 = Button(self, text = "Total ",font = ('Times new roman',(30)),bg = "white", width = 12, command = lambda: master.switch(Total,["student",user]) )
		button5.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(30)), width = 12, command = lambda: master.switch(Administrator_Management,[user]))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM) 
		
class Department_manage(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		label = Label(self, text =" Department Management",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		
		button = Button(self, text = "View details",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(View_Dep,[user]))
		button.pack(padx = 10, pady = 10)
		button2 = Button(self, text = "Add New",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Add_New_Dep,[user]))
		button2.pack(padx = 10, pady = 10)
		
		button6 = Button(self, text = "Modify",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda:master.switch(Modify_Dep,[user]))
		button6.pack(padx = 10, pady = 10)
		
		button7 = Button(self, text = "Delete",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Delete_Dep,[user]) )
		button7.pack(padx = 10, pady = 10)
		
		
		button5 = Button(self, text = "Total ",font = ('Times new roman',(30)),bg = "white", width = 12, command = lambda: master.switch(Total,["department",user]) )
		button5.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(30)), width = 12, command = lambda: master.switch(Administrator_Management,[user]))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)
		
class View_Dep(Frame):
	def __init__(self,master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		attribute_list = []
		query = "select dep_name from department"
		cursor.execute(query)
		result = cursor.fetchall()
		for name in result:
			attribute_list.append(name[0])
		
		def on_click():
			branch = value_inside.get()
			output.delete(0.0, END)
			
			
			query = f" Select  * from department where dep_name = \"{branch}\" "
			cursor.execute(query)
			result = cursor.fetchall()
			
			message = f"\n\n"
			for list in result :
				message += f"Department name :  {list[0]} \nDepartment Building : {list[1]} \nDepartment Budget : {list[2]} "
			output.insert(0.0,message)
		label = Label(self,font = ('Elephant',(30)), bg = "light blue", fg = "black", text =f"Enter the details of the Department")
		label.pack(pady = 60)
		
		value_inside = StringVar(self)
		value_inside.set("  Select the Department  ")
		question_menu = OptionMenu(self,value_inside,*attribute_list ).pack()
		
		submit = Button(self, text = f"View Department",font = ('times new roman',(25)), width = 20, command = on_click)
		submit.pack(padx = 10, pady = 10)

		output = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		output.pack()
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda : master.switch(Department_manage,[user]))
		self.button.pack(padx = 10, pady = 10)
class Modify_Dep(Frame):
	def __init__(self, master,list):
		user = list[0]
		
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		attribute_list = []
		query = "select dep_name from department"
		cursor.execute(query)
		result = cursor.fetchall()
		for name in result:
			attribute_list.append(name[0])
			
		att_list = ["dep_name" , "budget" , "building"]
		
		def on_click():
			"""Checking data and writing the results"""

			value = value_inside.get()
			attribute = value_in.get()
			modified = entryModify.get()
			
			query = f"Update department Set {attribute} = \"{modified}\" where dep_name = \"{value}\" "
			cursor.execute(query)
			connection.commit()
			messagebox.showinfo( "Status" , " Information modified Successfully !")
			
			entryModify.delete(0,END)
		
		
		label = Label(self, text =f"Modifying  Department",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 60 )
		
		label1 = Label(self, text =f"Select Department",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label1.pack(pady = 20)
		value_inside = StringVar(self)
		value_inside.set("  Select the Department  ")
		question_menu = OptionMenu(self,value_inside,*attribute_list ).pack()
		
		
		label2 = Label(self, text = "Select the Attribute ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack(pady = 20)
		value_in = StringVar(self)
		value_in.set("  Select the Attribute ")
		question_menu = OptionMenu(self,value_in,*att_list ).pack()
		
		label3 = Label(self, text = "Modified value : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack(pady = 20)
		entryModify = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryModify.pack(pady = 20)
		
		submit = Button(self, text = f"Submit",font = ('times new roman',(25)), width = 20, command = on_click)
		submit.pack(padx = 10, pady = 10)
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda : master.switch(Department_manage,[user]))
		self.button.pack(padx = 10, pady = 10)
class Delete_Dep(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		attribute_list = []
		query = "select dep_name from department"
		cursor.execute(query)
		result = cursor.fetchall()
		for name in result:
			attribute_list.append(name[0])	
		def on_click():
			"""Checking data and writing the results"""
			value = value_inside.get()
			query = f"Delete from department where dep_name = \"{value}\""
			cursor.execute(query)
			connection.commit()
			messagebox.showinfo( "Status" , " Information Deleted Successfully !")
			
		"""Frame widgets"""
		label = Label(self, text =f"Deleteing the Record of department ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 60)
		# user input, product
		label2 = Label(self, text = f"Department name  : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack(pady = 20)
		value_inside = StringVar(self)
		value_inside.set("  Select the Department  ")
		question_menu = OptionMenu(self,value_inside,*attribute_list ).pack()
		
		submit = Button(self, text = "Submit",font = ('times new roman',(25)), width = 8, command = on_click)
		submit.pack(padx = 10, pady = 20)
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda : master.switch(Department_manage,[user]))
		self.button.pack(padx = 10, pady = 20)
		
class Add_New_Dep(Frame):
	def __init__(self,master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
	
		
		def on_click():
			name = nameEntry.get()
			building = BuildingEntry.get()
			budget = BudgetEntry.get()
			if name.strip() == "" :
				messagebox.showerror("Error", "Department name cannot be Empty")
			elif building.strip() == "":
				messagebox.showerror("Error", "Buildinf name cannot be empty ")
			else :
				try :
					budget = int(budget)
					query = f"Insert into department values(\"{name}\" , \"{building}\" , \"{budget}\" ) "
					cursor.execute(query)
					connection.commit()
					messagebox.showinfo("Info", "Data added Successfully")
					nameEntry.delete(0,END)
					BuildingEntry.delete(0,END)
					BudgetEntry.delete(0,END)
				except :
					messagebox.showerror("Error" , "Budget should contain only digits")
					
		
		label = Label(self,font = ('Elephant',(30)), bg = "light blue", fg = "black", text =f"Enter the details of the Department")
		label.pack(pady = 20)
		
		label1 = Label(self, text = "Name : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label1.pack(pady = 10)
		nameEntry = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		nameEntry.pack(pady = 20)

		label2 = Label(self, text = "Building : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack(pady = 20)
		BuildingEntry = Entry(self,font = ('times new roman',(20)), width = 20, bg = "white")
		BuildingEntry.pack(pady = 20)

		label3 = Label(self, text = "Budget : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack(pady = 20)
		BudgetEntry = Entry(self,font = ('times new roman',(20)), width = 20, bg = "white")
		BudgetEntry.pack(pady = 20)
		
		submit = Button(self, text = f"Add Department",font = ('times new roman',(25)), width = 20, command = on_click)
		submit.pack(padx = 10, pady = 10)
		
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda : master.switch(Department_manage,[user]))
		self.button.pack(padx = 10, pady = 10)

class Add_New(Frame):

	def __init__(self, master,list):
		role = list[0]
		user = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		attribute_list = [ "MALE" , "FEMALE" , "Other" ]
		
		at_list = []
		query = "select dep_name from department"
		cursor.execute(query)
		result = cursor.fetchall()
		for name in result:
			at_list.append(name[0])
			
		def validate():
			
			ID = IDEntry.get()
			name = nameEntry.get()
			dep = value_in.get()
			
			if role == "course":
				year = YearEntry.get()
				try :
					year = int(year)
				except:
					messagebox.showinfo("ERROR", "Credits should be Numberic")
				query = f"Insert into course values(\"{ID}\" , \"{name}\" ,\"{dep}\" , {year} )"
				YearEntry.delete(0,END)
				cursor.execute(query)
				connection.commit()	
			elif role == "professor":
				email = EmailEntry.get()
				dob = DOB.get_date()
				gender = value_inside.get()
				password = PassEntry.get()
				query = f"Insert into {role} values(\"{ID}\" , \"{name}\" ,\"{email}\" , \"{dep}\" , \"{dob}\" , \"{gender}\" , \"{password}\")"
				EmailEntry.delete(0,END)
				PassEntry.delete(0,END)
				cursor.execute(query)
				connection.commit()	
			else:
				email = EmailEntry.get()
				dob = DOB.get_date()
				gender = value_inside.get()
				semester = SemEntry.get()
				password = PassEntry.get()
				try :
					semester = int(semester)
				except:
					messagebox.showerror("Error", "Semester should be Integer")
				query = f"Insert into {role} values(\"{ID}\" , \"{name}\" ,\"{email}\" , \"{dep}\" , \"{dob}\" , \"{gender}\" , \"{password}\" , {semester} , 0)"
				cursor.execute(query)
				connection.commit()	
				EmailEntry.delete(0,END)
				PassEntry.delete(0,END)
				SemEntry.delete(0,END)
				merry = f"Insert into fees values(\"{ID}\" , \"NULL\" , 0 , {semester})"
				cursor.execute(merry)
				connection.commit()	
				
			
			
			messagebox.showinfo("Info", "Data added Successfully")
			nameEntry.delete(0, END)
			IDEntry.delete(0, END)
			
			
		def on_click():
			if role == "student":
				master.switch(Student_manage,[user])
			elif role == "course":
				master.switch(Course_manage,[user])
			elif role == "professor":
				master.switch(Professor_manage,[user])
			
		"""Frame widgets"""
		label = Label(self,font = ('Elephant',(30)), bg = "light blue", fg = "black", text =f"Enter the details of the {role}")
		label.pack()
		
		label2 = Label(self, text = f"{role}_ID : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack()
		IDEntry = Entry(self,font = ('times new roman',(20)), width = 20, bg = "white")
		IDEntry.pack()
		
		label1 = Label(self, text = "Name : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label1.pack()
		nameEntry = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		nameEntry.pack()

		

		label3 = Label(self, text = "Department : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack()
		value_in = StringVar(self)
		value_in.set("  Select the Department  ")
		question_menu = OptionMenu(self,value_in,*at_list ).pack(pady = 10)
		if role == "student":
			label9 = Label(self, text = "Semester : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
			label9.pack()
			SemEntry = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
			SemEntry.pack()
		
		if role == "course":
			
			label4 = Label(self, text = "Credits : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
			label4.pack()
			YearEntry = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
			YearEntry.pack()
		else:
		
			label5 = Label(self, text = "Email : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
			label5.pack()
			EmailEntry = Entry(self, width = 30,font = ('times new roman',(20)), bg = "white")
			EmailEntry.pack()
		
			label7 = Label(self, text ="Select Birth Date ",font = ('Elephant',(20)), bg = "light blue", fg = "black")
			label7.pack()
			DOB = Calendar(self,selectmode = 'day' , year = 2001 , month = 5 , day = 22 )
			DOB.pack(pady = 20)
			
			label8 = Label(self, text ="Password ",font = ('Elephant',(20)), bg = "light blue", fg = "black")
			label8.pack()
			PassEntry = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
			PassEntry.pack(pady = 20)
			PassEntry.insert(0,"Coep1234")
			
			value_inside = StringVar(self)
			value_inside.set("Select the Gender ")
			Question_menu = OptionMenu(self,value_inside,*attribute_list ).pack()
	
		submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 8, command = validate)
		submit.pack(padx = 10, pady = 10)

		button3 = Button(self, text = "Back",font = ('times new roman',(20)), width = 8, command = on_click)
		button3.pack(padx = 10, pady = 10)
		
		
class Details(Frame):

	def __init__(self, master,list):
		role = list[0]
		user = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		def on_back():
			if role == "student":
				master.switch(Student_manage,[user])
			elif role == "course":
				master.switch(Course_manage,[user])
			elif role == "professor":
				master.switch(Professor_manage,[user])

		def on_click():
			output.delete(0.0, END)
			ID = entryMIS.get()
			entryMIS.delete(0,END)
			message = "\t Details of {role} \n"
			if role == "course":
				query = f"Select * from course where id = \"{ID}\""
				cursor.execute(query)
				result = cursor.fetchall()
				message += f" \n\nCourse ID : {result[0][0]} \nCourse name : {result[0][1]} \nCourse_Department : {result[0][2]} \nCredits : {result[0][3]}"
			elif role == "administrator":
				query = f"Select * from {role} where id = \"{ID}\""
				cursor.execute(query)
				result = cursor.fetchall()
				message += f"\n\n{role} ID : {result[0][0]} \nName : {result[0][1]} \n Email : {result[0][2]} \nDepartment : {result[0][3]} \nDate of Birth : {result[0][4]} \nGender : {result[0][5]}"
			else:
				query = f"Select * from {role} where id = \"{ID}\""
				cursor.execute(query)
				result = cursor.fetchall()
				message += f"\n\n{role} ID : {result[0][0]} \nName : {result[0][1]} \nSemester : {result[0][7]} \n Email : {result[0][2]} \nDepartment : {result[0][3]} \nDate of Birth : {result[0][4]} \nGender : {result[0][5]}"
			output.insert(END,message)
			
		label = Label(self, text =f"Enter the ID of {role}",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack()
		# user input, product
		label2 = Label(self, text = f"{role} ID : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack()
		entryMIS = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryMIS.pack()
		    
		submit = Button(self, text = "Submit",font = ('times new roman',(25)), width = 8, command = on_click)
		submit.pack(padx = 10, pady = 10)

		output = Text(self, width = 40,font = ('times new roman',(25)), height = 6, wrap = WORD, bg = "white")
		output.pack()
		
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = on_back)
		self.button.pack(padx = 10, pady = 10)
########################################################################################################################################################################################
class Modify(Frame):
	def __init__(self, master,list):
		role = list[0]
		user = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		if role == "course" :
			attribute_list = [ "Name" , "Credits" , "Department" ]
			dict = {"Name" : "name" , "Credits" : "credits" , "Department" : "dep" }
		else:
			attribute_list = [ "Name" , "Email"  , "Department" ]
			dict = {"Name" : "name" , "Email" : "email" , "Department" : "dep" }
			
		def on_back():
			if role == "student":
				master.switch(Student_manage,[user])
			elif role == "course":
				master.switch(Course_manage,[user])
			elif role == "professor":
				master.switch(Professor_manage,[user])

	
		def on_click():
			"""Checking data and writing the results"""
			mis = entryMIS.get()
			value = value_inside.get()
			modified = entryModify.get()
			
			query = f"Update {role} Set {dict[value]} = \"{modified}\" where id = \"{mis}\" "
			cursor.execute(query)
			connection.commit()
			messagebox.showinfo( "Status" , " Information modified Successfully !")
			entryMIS.delete(0,END)
			entryModify.delete(0,END)
		"""Frame widgets"""
		label = Label(self, text =f"Modifying  {role}",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 60 )
		# user input, product
		label2 = Label(self, text = f"{role} ID : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack(pady = 20)
		entryMIS = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryMIS.pack(pady = 20)
		
		value_inside = StringVar(self)
		value_inside.set("Select the Attribute")
		question_menu = OptionMenu(self,value_inside,*attribute_list ).pack()
		value = value_inside.get()
		
		label3 = Label(self, text = "Modified value : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack(pady = 20)
		entryModify = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryModify.pack(pady = 20)
	
		
		submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 8, command = on_click)
		submit.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 8, command = on_back)
		self.button.pack(padx = 10, pady = 10)


class Delete(Frame):
	def __init__(self, master,list):
		role = list[0]
		user = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		def on_click():
			"""Checking data and writing the results"""
			mis = entryMIS.get()
			
			query = f"Delete from {role} where id = \"{mis}\""
			cursor.execute(query)
			connection.commit()
			messagebox.showinfo( "Status" , " Information Deleted Successfully !")
			entryMIS.delete(0,END)
		
		def on_back():
			if role == "student":
				master.switch(Student_manage,[user])
			elif role == "course":
				master.switch(Course_manage,[user])
			elif role == "professor":
				master.switch(Professor_manage,[user])
		
		"""Frame widgets"""
		label = Label(self, text =f"Deleteing the Record of {role} ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 60)
		# user input, product
		label2 = Label(self, text = f"{role} ID : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack(pady = 20)
		entryMIS = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryMIS.pack(pady = 20)
		
		submit = Button(self, text = "Submit",font = ('times new roman',(25)), width = 8, command = on_click)
		submit.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = on_back)
		self.button.pack(padx = 10, pady = 10)
		
class View_Branch(Frame):
	
	def __init__(self, master,list):
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		role = list[0]
		user = list[1]
		attribute_list = []
		query = "select dep_name from department"
		cursor.execute(query)
		result = cursor.fetchall()
		for name in result:
			attribute_list.append(name[0])
			
		def on_back():
			if role == "student":
				master.switch(Student_manage,[user])
			elif role == "course":
				master.switch(Course_manage,[user])
			elif role == "professor":
				master.switch(Professor_manage,[user])
		
		
		def on_click():
			"""Checking data and writing the results"""
			branch = value_inside.get()
			output.delete(0.0, END)

			
			
			query = f" Select id , name from {role} where dep = \"{branch}\" "
			cursor.execute(query)
			result = cursor.fetchall()
			
			message = f"Total {role}s : {len(result)} \n\n"
			for list in result :
				message += f" {list[0]} : {list[1]} \n"
			output.insert(0.0,message)
		"""Frame widgets"""
		label = Label(self, text ="Branchwise Data",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 30)
		# user input, product
		label2 = Label(self, text = "Branch : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack(pady = 20)
		
		value_inside = StringVar(self)
		value_inside.set("  Select the Department  ")
		question_menu = OptionMenu(self,value_inside,*attribute_list ).pack()
		
		    
		submit = Button(self, text = f"View {role}s",font = ('times new roman',(25)), width = 20, command = on_click)
		submit.pack(padx = 10, pady = 10)

		output = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		output.pack()
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = on_back)
		self.button.pack(padx = 10, pady = 10)

class Total(Frame):
	
	def __init__(self, master,list):
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		role = list[0]
		user = list[1]	
		
		def on_back():
			if role == "student":
				master.switch(Student_manage,[user])
			elif role == "course":
				master.switch(Course_manage,[user])
			elif role == "professor":
				master.switch(Professor_manage,[user])
			elif role == "department":
				master.switch(Department_manage,[user])
			
		
			
		label = Label(self, text =f"{role} Data",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 30)
		# user input, product
	
		output = Text(self, width = 40,font = ('times new roman',(25)), height = 20, wrap = WORD, bg = "white")
		output.pack()
		
		output.delete(0.0, END)
		if role == "department":
			query = f"Select dep_name,building from department"
		else:
			query = f"Select id,name from {role} "
		cursor.execute(query)
		result= cursor.fetchall()
		
		message = f"Total {role}s : {len(result)} \n\n"
		for list in result :
			message += f"{list[0]} : {list[1]} \n"
		output.insert(0.0,message)
		
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = on_back)
		self.button.pack(padx = 10, pady = 10)
			
class Professor_manage(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		label = Label(self, text =" Professor Management",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		
		button = Button(self, text = "View details",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Details,["professor",user]))
		button.pack(padx = 10, pady = 10)
		button2 = Button(self, text = "Add New",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Add_New,["professor",user]))
		button2.pack(padx = 10, pady = 10)
		
		button6 = Button(self, text = "Modify",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda:master.switch(Modify,["professor",user]))
		button6.pack(padx = 10, pady = 10)
		
		button7 = Button(self, text = "Delete",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Delete,["professor",user]) )
		button7.pack(padx = 10, pady = 10)
		
		button4 = Button(self, text = "View Branchwise ",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(View_Branch,["professor",user]) )
		button4.pack(padx = 10, pady = 10)
		button5 = Button(self, text = "Total ",font = ('Times new roman',(30)),bg = "white", width = 12, command = lambda: master.switch(Total,["professor",user]) )
		button5.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Administrator_Management,[user]))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM) 
class Course_manage(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		label = Label(self, text =" Course Management",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack(padx = 10, pady = 60)
		button = Button(self, text = "View details",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Details,["course",user]))
		button.pack(padx = 10, pady = 10)
		button2 = Button(self, text = "Add New",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Add_New,["course",user]))
		button2.pack(padx = 10, pady = 10)
		
		button6 = Button(self, text = "Modify",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda:master.switch(Modify,["course",user]))
		button6.pack(padx = 10, pady = 10)
		
		button7 = Button(self, text = "Delete",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Delete,["course",user]) )
		button7.pack(padx = 10, pady = 10)
		
		button4 = Button(self, text = "View Branchwise ",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(View_Branch,["course",user]) )
		button4.pack(padx = 10, pady = 10)
		button5 = Button(self, text = "Total ",font = ('Times new roman',(30)),bg = "white", width = 12, command = lambda: master.switch(Total,["course",user]) )
		button5.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 12, command = lambda: master.switch(Administrator_Management,[user]))
		self.button.pack(padx = 50, pady = 50, side = BOTTOM)  
###############################################################################################################################################################################################
class FEES(Frame):
	def __init__(self, master,list):
		user = list[0]
		SEM = list[1]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		
		def on_click():
			amount = entryAmount.get()
			trans = entryTrans.get()
			
			try :
				amount =int(amount)
			except :
				messagebox.showerror("Error", "Amount shuld be Integer!")
			
			query = f"Update fees Set ID = \"{trans}\" , amount = {amount}  where s_id = \"{user}\" and semester = \"{SEM}\" "
			cursor.execute(query)
			connection.commit()
			messagebox.showinfo( "Status" , f"Successfully registered")
			entryTrans.delete(0,END)
			entryAmount.delete(0,END)
				
		label = Label(self, text =f"Payment Details ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 30)
		
		label2 = Label(self, text = f"Student ID : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack(pady = 20)
		entryMIS = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryMIS.pack(pady = 20)
		entryMIS.configure(state = "normal")
		entryMIS.insert(0,user)
		entryMIS.configure(state = "disabled")
		
		label3 = Label(self, text = f"Transaction ID : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack(pady = 20)
		entryTrans = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryTrans.pack(pady = 20)
		
		label4 = Label(self, text = f"Amount : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label4.pack(pady = 20)
		entryAmount = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryAmount.pack(pady = 20)
		
		submit = Button(self, text = "Submit",font = ('times new roman',(25)), width = 8, command = on_click)
		submit.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command =lambda :master.switch(Student,[user]) )
		self.button.pack(padx = 10, pady = 10)
		

		
class Enroll(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		final = list[1]
		course = list[2]
		SEM = list[3]
		
			
		label = Label(self, text =f"New Courses ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 30)
		list = []
		for message in final:
			temp = IntVar()
			a = Checkbutton(self,text = f"{message}" , var = temp , onvalue = 1 , offvalue = 0 ,height = 3 ,width = 60)
			a.pack()
			list.append(temp)
		 
		def on_click():
			i = 0
			for var in list:
				key = var.get()
				if key == 1: #enrolling
					query = f"Insert into enrolled values(\"{course[i]}\" , \"{user}\" ,{SEM} , 0 ) "
					cursor.execute(query)
					connection.commit()
				i += 1
				
			messagebox.showinfo("Info","Succesfully Enrolled")
				
						
		
		submit = Button(self, text = "Submit",font = ('times new roman',(20)), width = 8, command = on_click)
		submit.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(20)), width = 8, command =lambda :master.switch(Student,[user]) )
		self.button.pack(padx = 10, pady = 10)
		
class Feedback(Frame):
	def __init__(self, master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		result = list[1]
		SEM = list[2]
		
				
		
		label = Label(self, text =f"FeedBack Details ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(padx = 30,pady = 20)
		
		label2 = Label(self, text = f"Student ID : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack(padx = 30 ,pady = 10)
		entryMIS = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryMIS.pack(padx = 30,pady = 10)
		entryMIS.configure(state = "normal")
		entryMIS.insert(0,user)
		entryMIS.configure(state = "disabled")
		
		label1 = Label(self, text = f"Semester : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label1.pack(padx = 30 ,pady = 10)
		entrySem = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entrySem.pack(padx = 30 ,pady = 10)
		entrySem.configure(state = "normal")
		entrySem.insert(0,SEM)
		entrySem.configure(state = "disabled")
		
		
		label3 = Label(self, text = f"Course Id : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack(padx = 30 ,pady = 10)
		
		def bekar():
			def on_click():
				course = course_in.get()
				Proff = entryProf.get()
				message = Feed_back.get(1.0,END)
				query = f"Select * from teaches where course_id = \"{course}\" and semester = {SEM} and prof_id = \"{Proff}\""
				cursor.execute(query)
				result = cursor.fetchall()
				if len(result) == 0:
					messagebox.showerror("ERROR", f" {query} This Professor doesnot teach this subject")
				else:
					query = f"Insert Into feedback values(\"{user}\" , \"{Proff}\" , {SEM} , \"{course}\" , \"{message}\" )"
					flag = 0
					try :
						cursor.execute(query)
						connection.commit()
					except:
						flag = 1
					if flag == 1:
						messagebox.showinfo("Error",f"{Error}")
					else:
					
						messagebox.showinfo("Info","Submitted Succesfully")
						Feed_back.delete(0.0,END)
						
					
			course = course_in.get()
			query = f"Select prof_id from teaches where course_id = \"{course}\" and semester = \"{SEM}\" "
			cursor.execute(query)
			result = cursor.fetchall()
			att = []
			for ilu in result:
				att.append(ilu[0])
		
			
			label4 = Label(self, text = f"Professor Id ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
			label4.pack(pady = 10)	
			entryProf = StringVar(self)
			entryProf.set("  Select the Prof ID ")
			question_menu = OptionMenu(self,entryProf,*att ).pack()
			
			label5 = Label(self, text = f"Feedback : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
			label5.pack(padx = 30 ,pady = 10)
			
			
			Feed_back = Text(self, height = 6 ,width = 40,font = ('times new roman',(20)), bg = "white")
			Feed_back.pack(padx = 30 ,pady = 10)
			submit = Button(self, text = "Submit",font = ('times new roman',(25)), width = 8, command = on_click)
			submit.pack(padx = 30, pady = 10)
		
		course_list = []
		for list in result:
			course_list.append(list[0])
		course_in = StringVar(self)
		course_in.set("  Select the Course_ID ")
		question_menu = OptionMenu(self,course_in,*course_list ).pack()
		ok = Button(self,text ="ok" ,font = ('times new roman',(10)) , bg = "light yellow" ,fg = "black" ,width = 5 , command = bekar)
		ok.pack(padx = 30)

		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command =lambda :master.switch(Student,[user]) )
		self.button.pack(padx = 30, pady = 10,side = BOTTOM)
		
class Academics(Frame):
	def __init__(self, master,list):
		user = list[0]
		SEM = list[1]
		SEM = int(SEM)
		
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		label = Label(self, text =f"Academics Details ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(pady = 30)
		
		button_list = []
		for semester in range(1 , SEM + 1):
			button = Button(self, text = f"Semester {semester}",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda x=semester: master.switch(Semester,[user,x,SEM]))
			button.pack(padx = 10, pady = 10)
			button_list.append(button)
		
		
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command =lambda :master.switch(Student,[user]) )
		self.button.pack(padx = 10, pady = 10)
class Semester(Frame):
	def __init__(self, master,list):
		user = list[0]
		SEM = list[1]
		SEMESTER = list[2]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		label = Label(self, text =f"Semester {SEM} ",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(padx= 30 , pady = 30)
		
		output = Text(self, width = 60,font = ('times new roman',(25)), height = 20, wrap = WORD, bg = "white")
		output.pack()
		
		output.delete(0.0, END)
		query = f"Select course_id , attendance from enrolled where s_id = \"{user}\" and sem = {SEM} "
		cursor.execute(query)
		result= cursor.fetchall()
		
		message = f"Total Courses : {len(result)}\n"
		var = 0 
		su = 0 
		for temp in result :
			query = f"Select exam_id from exam  where course_id = \"{temp[0]}\" and sem = {SEM} "
			cursor.execute(query)
			res= cursor.fetchall()
			if len(res) == 0 :
				message += f"Course_Id : \"{temp[0]}\"       Attendance: {temp[1]}          Grade: NULL \n"
			else:
				query = f"Select grade from result where exam_id = \"{res[0][0]}\" and s_id = \"{user}\" "
				cursor.execute(query)
				re= cursor.fetchall()
				if len(re) == 0:
					continue 
				message += f"Course_Id : \"{temp[0]}\"        Attendance: {temp[1]}         Grade: {re[0][0]} \n"
				su += int(re[0][0])
				var += 1
		if var==0:
			pass
		else :
			message += f"\n\n\n\t \tCGPA : {su/var} \n "
		
		output.configure(state = "normal")	
		output.insert(0.0,message)
		output.configure(state = "disabled")
		
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command =lambda :master.switch(Academics,[user,SEMESTER]) )
		self.button.pack(padx = 10, pady = 10)
		
class Promote(Frame):
	def __init__(self,master,list):
		user = list[0]
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		def on_click():
			SEM = entrySem.get()
			cutt = cutoff.get()
			next_sem = nextSem.get()
			query = f"Select id from student where  sem = {SEM} "
			cursor.execute(query)
			result= cursor.fetchall()
			
			for list in result :
				st_id = list[0]
				
				query = f"Select course_id from enrolled  where s_id = \"{st_id}\" and sem = {SEM} "
				cursor.execute(query)
				res= cursor.fetchall()
				exam_list = []
				
				for k in res:
					query = f"Select exam_id from exam where course_id = \"{k[0]}\" and sem = {SEM} "
					cursor.execute(query)
					re = cursor.fetchall()
					for i in re:
						exam_list.append(i[0])
			
				if len(exam_list) == 0 :
					pass
				else:
					sum = 0 
					count = 0 
					for exam in exam_list:
						query = f"Select grade from result where exam_id = \"{exam}\" and s_id = \"{st_id}\" "
						cursor.execute(query)
						re = cursor.fetchall()
						if len(re) == 0:
							continue
						else:
							count += 1
							sum+= int(re[0][0])
					
					he = sum/count
					
					if (he) >= float(cutt):
						query = f"Update student Set sem = \"{next_sem}\" where id = \"{st_id}\" "
						cursor.execute(query)
						connection.commit()
						
						merry = f"Insert into fees values(\"{st_id}\" , \"NULL\" , 0 , {next_sem})"
						cursor.execute(merry)
						connection.commit()	
				
			messagebox.showinfo("Info","Succesfully Done")
			entrySem.delete(0,END)
			cutoff.delete(0,END)
			nextSem.delete(0,END)

		
		label = Label(self, text =f"Enter the Semester :",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label.pack(padx = 30 ,pady = 30)
		entrySem = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entrySem.pack(padx = 30 ,pady = 10)
		
		label1 = Label(self, text =f"Promote to Semester :",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label1.pack(padx = 30 ,pady = 30)
		nextSem = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		nextSem.pack(padx = 30 ,pady = 10)
		
		label2 = Label(self, text =f"Enter Cutoff CGPA :",font = ('Elephant',(25)), bg = "light blue", fg = "black")
		label2.pack(padx = 30 ,pady = 30)
		cutoff = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		cutoff.pack(padx = 30 ,pady = 10)
		
		submit = Button(self, text = "Submit",font = ('times new roman',(25)), width = 8, command = on_click)
		submit.pack(padx = 30, pady = 10)
	
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command =lambda :master.switch(Administrator,[user]) )
		self.button.pack(padx = 30, pady = 10)
		
		
		
	
	
if __name__ == "__main__":
    app = App()
    app.mainloop()
