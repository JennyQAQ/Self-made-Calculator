from tkinter import *

cal_string = ''

app = Tk()
app.geometry('260x460')
app.title('calculator')
app.config(background='coral',cursor="heart")

melabel = Label(app,text='CALCULATOR',font =('Apple chancery',20),cursor="heart")
melabel.pack(side=TOP)

melabel = Label(app,text='',bg =('coral'),cursor="heart")
melabel.pack(side=TOP)

textbox = StringVar()
metext = Entry(app,textvar=textbox)
metext.pack()


def cursor():
    cursor="heart"

def clickBtn(operator):   #button is from APP
    global cal_string
    cal_string += str(operator)
    textbox.set(cal_string)

def calculate():
    global cal_string
    cal_string = str(eval(cal_string))
    textbox.set(cal_string)

def clear():
    global cal_string
    cal_string = ''
    textbox.set(cal_string)
#first row
btn_7 = Button(app,padx=14,pady=14,text='7',command=lambda:clickBtn(7),cursor="heart")
btn_7.place(x=10,y=100)

btn_8 = Button(app,padx=14,pady=14,text='8',command=lambda:clickBtn(8),cursor="heart")
btn_8.place(x=75,y=100)

btn_9 = Button(app,padx=14,pady=14,text='9',command=lambda:clickBtn(9),cursor="heart")
btn_9.place(x=140,y=100)

btn_plus = Button(app,padx=14,pady=14,text='+',command=lambda:clickBtn('+'),cursor="heart")
btn_plus.place(x=205,y=100)

#second row
btn_4 = Button(app,padx=14,pady=14,text='4',command=lambda:clickBtn(4),cursor="heart")
btn_4.place(x=10,y=170)

btn_5 = Button(app,padx=14,pady=14,text='5',command=lambda:clickBtn(5),cursor="heart")
btn_5.place(x=75,y=170)

btn_6 = Button(app,padx=14,pady=14,text='6',command=lambda:clickBtn(6),cursor="heart")
btn_6.place(x=140,y=170)

btn_minus = Button(app,padx=14,pady=14,text='-',command=lambda:clickBtn('-'),cursor="heart")
btn_minus.place(x=205,y=170)

#third row
btn_1 = Button(app,padx=14,pady=14,text='1',command=lambda:clickBtn(1),cursor="heart")
btn_1.place(x=10,y=240)

btn_2 = Button(app,padx=14,pady=14,text='2',command=lambda:clickBtn(2),cursor="heart")
btn_2.place(x=75,y=240)

btn_3 = Button(app,padx=14,pady=14,text='3',command=lambda:clickBtn(3),cursor="heart")
btn_3.place(x=140,y=240)

btn_multiplication = Button(app,padx=14,pady=14,text='x',command=lambda:clickBtn('*'),cursor="heart")
btn_multiplication.place(x=205,y=240)

#fourth row
btn_0 = Button(app,padx=14,pady=14,text='0',command=lambda:clickBtn(0),cursor="heart")
btn_0.place(x=10,y=310)

btn_dot = Button(app,padx=14,pady=14,text='.',command=lambda:clickBtn('.'),cursor="heart")
btn_dot.place(x=75,y=310)

btn_clear = Button(app,padx=14,pady=14,text='CL',command=clear,cursor="heart")
btn_clear.place(x=140,y=310)

btn_division = Button(app,padx=14,pady=14,text='/',command=lambda:clickBtn('/'),cursor="heart")
btn_division.place(x=205,y=310)

#5th
btn_equal = Button(app,padx=100,pady=14,text='=',command=calculate,cursor="heart")
btn_equal.place(x=10,y=380)
app.mainloop()
