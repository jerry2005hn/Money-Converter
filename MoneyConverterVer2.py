from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
window.title("Money Converter Ver2")
window.geometry('900x500')

lblMoney = Label(window, text="Enter amount of money:", font=("Arial", 15))
lblMoney.grid(column=0, row=0)
txtMoney = Entry(window,width=20)
txtMoney.grid(column = 1, row = 0)
lblFrom = Label(window, text="Convert From: ", font=("Arial", 15))
lblFrom.grid(column=0, row=1)
#Create combobox
comboFrom = Combobox(window)
comboFrom['values'] = ('USD', 'VND', 'EUR', 'JPY', 'GBP', 'CNY')
comboFrom.current(0) #set the selected item
comboFrom.grid(column=1, row=1)

lblTo = Label(window, text="To: ", font=("Arial", 15))
lblTo.grid(column=2, row=1)
comboTo = Combobox(window)
comboTo['values']= ('USD', 'VND', 'EUR', 'JPY', 'GBP', 'CNY')
comboTo.current(1) #set the selected item
comboTo.grid(column=3, row=1)

values = [23256, 1, 25834, 214, 29907, 3291]
def Convert():
    money = float(txtMoney.get())
    a = comboFrom.current()
    b = comboTo.current()
    result = money*values[a]/values[b]
    lblResult.configure(text = str(result))
    
btn = Button(window, text="Convert", command=Convert) 
btn.grid(column=0, row=2)
lblResult = Label(window, text = '')
lblResult.grid(column = 1, row = 2)

window.mainloop()
a = input('')
