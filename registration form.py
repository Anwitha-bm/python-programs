import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
def enter_data():
    accepted=accept_var.get()
    if accepted=="Accepted":
            firstname=first_name_entry.get()
            lastname=last_name_entry.get()
            if firstname and lastname:
                title=title_Combobox.get()
                age=age_spinbox.get()
                nationality=nationality_scrolledtext.get('1.0','end-1c')
                print("Firstname: ",firstname,"Lastname: ",lastname)
                print("Title:",title,"Age:",age,"Nationality:",nationality)
                print("---------------------------------")
            else:
                    tkinter.messagebox.showwarning(title="Error",message="Firstname and lastname are required.")
    else:
                  tkinter.messagebox.showwarning(title="Error",message="You have not accepted the terms")
window=tkinter.Tk()
window.title("Data Entry form")

frame=tkinter.Frame(window)
frame.pack()

user_info_frame=tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0,padx=30,pady=20)

first_name_label=tkinter.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label=tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)
first_name_entry=tkinter.Entry(user_info_frame)
last_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)


title_label=tkinter.Label(user_info_frame, text="Title")
title_Combobox=ttk.Combobox(user_info_frame, values=["","Mr.","Ms."])
title_label.grid(row=0,column=2)
title_Combobox.grid(row=1,column=2)
age_label=tkinter.Label(user_info_frame,text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame,from_=18,to=28)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nationality_label = tkinter.Label(user_info_frame,text="Nationality")
nationality_scrolledtext=scrolledtext.ScrolledText(user_info_frame,wrap=tkinter.WORD, width=5,height=5,font=("Time New Roman",12))
nationality_label.grid(row=2,column=1)
nationality_scrolledtext.grid(row=3,column=1)


radio_var=tkinter.IntVar()
rb1=tkinter.Radiobutton(user_info_frame,text='I/IV B.Tech',variable=radio_var,value=1)
rb2=tkinter.Radiobutton(user_info_frame,text='II/IV B.Tech',variable=radio_var,value=2)
rb3=tkinter.Radiobutton(user_info_frame,text='III/IV B.Tech',variable=radio_var,value=3)
rb4=tkinter.Radiobutton(user_info_frame,text='IV/IV B.Tech',variable=radio_var,value=4)
rb1.grid(row=4,column=1)
rb2.grid(row=4,column=2)
rb3.grid(row=4,column=3)
rb4.grid(row=4,column=4)

radio_var1=tkinter.IntVar()
rb5=tkinter.Radiobutton(user_info_frame,text="Semester:I",variable=radio_var1,value=1)
rb6=tkinter.Radiobutton(user_info_frame,text="Semester:II",variable=radio_var1,value=2)
rb5.grid(row=5,column=0)
rb6.grid(row=5,column=1)
accept_var=tkinter.StringVar(value="Not Accepted")
terms_check=tkinter.Checkbutton(user_info_frame,text="I accept terms and conditions.",variable=accept_var,onvalue="Accepted",offvalue="Not Accepted")
terms_check.grid(row=6,column=0)
button=tkinter.Button(user_info_frame,text="Enter data",command=enter_data)
button.grid(row=7,column=0,sticky="news",padx=20,pady=10)
quit_button=tkinter.Button(user_info_frame,text="Quit",command=window.destroy)
quit_button.grid(row=7,column=1)
window.mainloop()