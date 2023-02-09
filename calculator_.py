from tkinter import *


cal = Tk()
cal.title("The Simple Easy Calculator")

m = Entry(cal, width = 35, borderwidth = 5)
m.grid(row =0,column=0, columnspan = 3, padx= 10, pady=10)

def b_click(n):
    current = m.get()
    m.delete(0,END)
    m.insert(0, str(current) + str(n))

def b_clear():
    m.delete(0,END)
    return
def b_add():
    fn = m.get()
    global f_n
    global math
    math = "addition"
    f_n = int(fn)
    m.delete(0,END)

def b_equal():
    sn = m.get()
    m.delete(0,END)
    if math == "addition":
        m.insert(0,f_n + int(sn))
    elif math == "subtraction":
        m.insert(0,f_n - int(sn))
    elif math == "multipication":
        m.insert(0,f_n * int(sn))
    elif math =="division":
        m.insert(0,f_n / int(sn))

def b_sub():
    fn = m.get()
    global f_n
    global math
    math = "subtraction"
    f_n = int(fn)
    m.delete(0,END)
    

def b_mult():
    fn = m.get()
    global f_n
    global math
    math = "multipication"
    f_n = int(fn)
    m.delete(0,END)

def b_div():
    fn = m.get()
    global f_n
    global math
    math = "division"
    f_n = int(fn)
    m.delete(0,END)
    

    
    

b1 =Button(cal, text ="1", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda: b_click(1))
b2 =Button(cal, text ="2", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda: b_click(2))
b3 =Button(cal, text ="3", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_click(3))
b4 =Button(cal, text ="4", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_click(4))
b5 =Button(cal, text ="5", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_click(5))
b6 =Button(cal, text ="6", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_click(6))
b7 =Button(cal, text ="7", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda: b_click(7))
b8 =Button(cal, text ="8", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_click(8))
b9 =Button(cal, text ="9", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_click(9))
b0 =Button(cal, text ="0", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_click(0))

an = Button(cal, text ="+", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_add())
mn = Button(cal, text ="*", bg= "#7FFFD4", fg = "blue", padx =40, pady=40,
           command= lambda:b_mult())
dn = Button(cal, text ="/", bg= "#7FFFD4", fg = "blue", padx =60, pady=40,
           command= lambda:b_div())
sn = Button(cal, text ="-", bg= "#7FFFD4", fg = "blue", padx =60, pady=40,
           command= lambda:b_sub())
el = Button(cal, text ="=", bg= "#7FFFD4", fg = "blue", padx =60, pady=40,
           command= lambda:b_equal())
cr =Button(cal, text ="CLEAR", bg= "#7FFFD4", fg = "blue", padx =45, pady=40,
           command= lambda:b_clear())

b1.grid(row =1, column = 0)
b2.grid(row = 1, column = 1)
b3.grid(row= 1, column =2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b7.grid(row = 3, column =0)
b8.grid(row = 3, column =1)
b9.grid(row =3, column =2)
b0.grid(row =4, column = 0)

an.grid(row =4, column = 1)
mn.grid(row =4, column =2)
dn.grid(row = 3, column = 3)
sn.grid( row =4, column =3)
el.grid(row =2, column =3)
cr.grid(row =1, column =3)




cal.mainloop()
 
