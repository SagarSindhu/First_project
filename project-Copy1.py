#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import*


# In[4]:


from tkinter import messagebox


# In[21]:


win=Tk()
win.state("zoomed")
win.resizable(width=False,height=False)
'''canvas=Canvas(win)
img=ImageTk.PhotoImage(Image.open('C:/Users/ASUS/Pictures/wallpapers/Anime').resize((180,130))) 
canvas.create_image(0,0,anchor=NW,image=img)
canvas.pack(expand=YES,fill=BOTH)''' 

win.configure(bg="yellow") 
win.title("hmmmm")

lbl_title=Label(win,text="Projects",font=('',50,'underline'),bg="black",fg="white") 
lbl_title.place(relx=.40,rely=0.04)


def home_screen():
    frm=Frame(win,bg='green')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=1)

    lbl_user=Label(frm,text="-By  Sagar Sindhu",font=('',20,'bold'),bg='black',fg="white") 
    lbl_user.place(relx=.8,rely=.1)

    lbl_user=Label(frm,text="Username",font=('',20,'bold'),bg='black',fg="white") 
    lbl_user.place(relx=.3,rely=.2)

    entry_user=Entry(frm,font=('',20,'bold'),bd=10) 
    entry_user.place(relx=.42,rely=.2)
    entry_user.focus()

    lbl_pass=Label(frm,text="Password",font=('',20,'bold'),bg='black',fg="white") 
    lbl_pass.place(relx=.3,rely=.3)

    entry_pass=Entry(frm,font=('',20,'bold'),bd=10,show="*") 
    entry_pass.place(relx=.42,rely=.3)

    btn_login=Button(frm,command=lambda:welcome_screen(entry_user,entry_pass),text="login",font=('',20,'bold'),bd=10,width=10) 
    btn_login.place(relx=.46,rely=.4)



def  welcome_screen(entry_user=None,entry_pass=None):
    if(entry_user!=None  and  entry_pass!=None): 
        user=entry_user.get()
        pwd=entry_pass.get()
    else:
        user="user" 
        pwd="user"
    if(len(user)==0  or  len(pwd)==0):
        messagebox.showwarning("validation","Please  fill  both  fields")
        return 
    else:
        if(user=="user"  or  pwd=="user"): 
            frm=Frame(win,bg='black')
            frm.place(relx=0,rely=.15,relwidth=1,relheight=1)
            
            btn_single=Button(frm,command=lambda:welcome(),text="Review  Analysis",font=('',20,'bold'),bd=10,width=25)
            btn_single.place(relx=.35,rely=.2)

            btn_bulk=Button(frm,command=lambda:spam_detection(),text="Spam  Detection",font=('',20,'bold'),bd=10,width=25) 
            btn_bulk.place(relx=.35,rely=.3)

            btn_bulk=Button(frm,command=lambda:welcome_screen_new(),text="Face  Detection",font=('',20,'bold'),bd=10,width=25) 
            btn_bulk.place(relx=.35,rely=.4)
            
            btn_bulk=Button(frm,command=lambda:welcome_screen_new(),text="Time pass",font=('',20,'bold'),bd=10,width=25) 
            btn_bulk.place(relx=.35,rely=.5)

            btn_logout=Button(frm,command=lambda:logout(),text="logout",font=('',20,'bold'),bd=10) 
            btn_logout.place(relx=.9,rely=0)
        else:
            messagebox.showerror("Fail","Invalid  Username/Password")
            
            

def logout():
    option=messagebox.askyesno('Confirmation','Are  you  sure  you  want  to  logout?')
    if(option==True): 
        home_screen()
    else:
        pass

home_screen()
win.mainloop()
                  
                                                                            


# In[ ]:




