from tkinter import *

mw = Tk()


def solve():
    try:
        ans = eval(db.get())
        db.delete(0, END)
        db.insert(0, str(ans))
    except:
        db.delete(0, END)
        db.insert(0, "ERROR")
def dark():
    mw.configure(bg="gray")
    frame1.configure(bg="gray")
    mw.configure(bg='black')
    btn_7 = Button(mw, text="7", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('7'), background="black",foreground="white")
    btn_7.grid(row=2, column=0, padx=2, pady=2)
    btn_8 = Button(mw, text="8", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('8'), background="black",foreground="white")
    btn_8.grid(row=2, column=1, padx=2, pady=2)
    btn_9 = Button(mw, text="9", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('9'), background="black",foreground="white")
    btn_9.grid(row=2, column=2, padx=2, pady=2)
    btn_m = Button(mw, text="x", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('*'), background="black",foreground="white")
    btn_m.grid(row=2, column=3, padx=2, pady=2)
    # new row
    btn_4 = Button(mw, text="4", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('4'), background="black",foreground="white")
    btn_4.grid(row=3, column=0, padx=2, pady=2)
    btn_5 = Button(mw, text="5", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('5'), background="black",foreground="white")
    btn_5.grid(row=3, column=1, padx=2, pady=2)
    btn_6 = Button(mw, text="6", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('6'), background="black",foreground="white")
    btn_6.grid(row=3, column=2, padx=2, pady=2)
    btn_s = Button(mw, text="-", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('-'), background="black",foreground="white")
    btn_s.grid(row=3, column=3, padx=2, pady=2)
    # new row
    btn_1 = Button(mw, text="1", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('1'), background="black",foreground="white")
    btn_1.grid(row=4, column=0, padx=2, pady=2)
    btn_2 = Button(mw, text="2", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('2'), background="black",foreground="white")
    btn_2.grid(row=4, column=1, padx=2, pady=2)
    btn_3 = Button(mw, text="3", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('3'), background="black",foreground="white")
    btn_3.grid(row=4, column=2, padx=2, pady=2)
    btn_a = Button(mw, text="+", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('+'), background="black",foreground="white")
    btn_a.grid(row=4, column=3, padx=2, pady=2)
    # new row
    btn_mod = Button(mw, text="%", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('%'), background="black",foreground="white")
    btn_mod.grid(row=5, column=0, padx=2, pady=2)
    btn_0 = Button(mw, text="0", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('0'), background="black",foreground="white")
    btn_0.grid(row=5, column=1, padx=2, pady=2)
    btn_dot = Button(mw, text=".", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('.'), background="black",foreground="white")
    btn_dot.grid(row=5, column=2, padx=2, pady=2)
    btn_Equal = Button(mw, text="=", padx=38, pady=12, font=("Arail", 15), command=solve, background="black",foreground="white")
    btn_Equal.grid(row=5, column=3, padx=2, pady=2)

    btn_clr = Button(mw, text="clear", padx=9, pady=12, font=("Arail", 20), command=cls,background="black",foreground="white")
    btn_clr.grid(row=1, column=0, padx=2, pady=2, columnspan=4)
    btn_del = Button(mw, text="delete", padx=5, pady=12, font=("Arail", 20), command=edit,background="black",foreground="white")
    btn_del.grid(row=1, column=2, padx=2, pady=2, columnspan=4)


def light():
    btn_7 = Button(mw, text="7", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('7'))
    btn_7.grid(row=2, column=0, padx=2, pady=2)
    btn_8 = Button(mw, text="8", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('8'))
    btn_8.grid(row=2, column=1, padx=2, pady=2)
    btn_9 = Button(mw, text="9", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('9'))
    btn_9.grid(row=2, column=2, padx=2, pady=2)
    btn_m = Button(mw, text="x", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('*'))
    btn_m.grid(row=2, column=3, padx=2, pady=2)
    # new row
    btn_4 = Button(mw, text="4", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('4'))
    btn_4.grid(row=3, column=0, padx=2, pady=2)
    btn_5 = Button(mw, text="5", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('5'))
    btn_5.grid(row=3, column=1, padx=2, pady=2)
    btn_6 = Button(mw, text="6", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('6'))
    btn_6.grid(row=3, column=2, padx=2, pady=2)
    btn_s = Button(mw, text="-", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('-'))
    btn_s.grid(row=3, column=3, padx=2, pady=2)
    # new row
    btn_1 = Button(mw, text="1", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('1'))
    btn_1.grid(row=4, column=0, padx=2, pady=2)
    btn_2 = Button(mw, text="2", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('2'))
    btn_2.grid(row=4, column=1, padx=2, pady=2)
    btn_3 = Button(mw, text="3", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('3'))
    btn_3.grid(row=4, column=2, padx=2, pady=2)
    btn_a = Button(mw, text="+", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('+'))
    btn_a.grid(row=4, column=3, padx=2, pady=2)
    # new row
    btn_mod = Button(mw, text="%", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('%'))
    btn_mod.grid(row=5, column=0, padx=2, pady=2)
    btn_0 = Button(mw, text="0", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('0'))
    btn_0.grid(row=5, column=1, padx=2, pady=2)
    btn_dot = Button(mw, text=".", padx=38, pady=12, font=("Arail", 15), command=lambda: ins('.'))
    btn_dot.grid(row=5, column=2, padx=2, pady=2)
    btn_Equal = Button(mw, text="=", padx=38, pady=12, font=("Arail", 15), command=solve)
    btn_Equal.grid(row=5, column=3, padx=2, pady=2)
    #top buttons
    btn_clr = Button(mw, text="clear", padx=9, pady=12, font=("Arail", 20), command=cls)
    btn_clr.grid(row=1, column=0, padx=2, pady=2, columnspan=4)
    btn_del = Button(mw, text="delete", padx=5, pady=12, font=("Arail", 20), command=edit)
    btn_del.grid(row=1, column=2, padx=2, pady=2, columnspan=4)


def ins(ele):
    s = db.get()
    db.delete(0, END)
    db.insert(0, s + ele)
def edit():
    s = db.get()
    s=s[:len(s)-1]
    db.delete(0, END)
    db.insert(0,s)
def cls():
    db.delete(0, END)
rv=StringVar()
db = Entry(mw, width=20, font=("Arail", 30), justify=RIGHT)
db.grid(row=0, column=0, padx=10, pady=20, columnspan=4)


frame1 = LabelFrame(mw,text="choose theme",padx=10,pady=10,foreground="white")
frame1.grid(row=1,column=0)

#Radiobutton(frame1,text="option 1",value="Dark",textvariable=rv,padx=10,pady=10).grid(row=1,column=0)
#rb2=Radiobutton(frame1,text="option 2",value="light",textvariable=rv,padx=10,pady=10)
#rb2.grid(row=1,column=2)
values = {"Dark": "1",
          "Light": "2"
          }
rv.set("1")
dark()
Radiobutton(frame1, text="Dark", variable=rv,value="1",command=dark).pack(side=LEFT, ipady=5)
Radiobutton(frame1, text="Light", variable=rv,value="2",command=light).pack(side=LEFT, ipady=5)


mw.mainloop()
