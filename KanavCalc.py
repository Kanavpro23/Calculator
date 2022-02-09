from tkinter import *#imported a library
import re

def main(master):#gave name to the function
    master.title("Kanav's calculator")#gave name to the window
    master.equation=Entry(master,width=40)#made display box
    master.equation.grid(row=0,column=0,columnspan=5,padx=10,pady=10)#gave coordinates to the display screen
    create_buttons(master)


def create_buttons(master):#made buttuons
    b0 = add_button(master,0)
    b0.grid(row=4,column=1,columnspan=1)#gave coordinates to the buttons
    b1 = add_button(master,1)
    b1.grid(row=3,column=0,columnspan=1)
    b2 = add_button(master,2)
    b2.grid(row=3,column=1,columnspan=1)
    b3 = add_button(master,3)
    b3.grid(row=3,column=2,columnspan=1)
    b4 = add_button(master,4)
    b4.grid(row=2,column=0,columnspan=1)
    b5= add_button(master,5)
    b5.grid(row=2,column=1,columnspan=1)
    b6 = add_button(master,6)
    b6.grid(row=2,column=2,columnspan=1)
    b7 = add_button(master,7)
    b7.grid(row=1,column=0,columnspan=1)
    b8 = add_button(master,8)
    b8.grid(row=1,column=1,columnspan=1)
    b9 = add_button(master,9)
    b9.grid(row=1,column=2,columnspan=1)
    b_plus =add_button(master,"+")
    b_plus.grid(row=1,column=3,columnspan=1)
    b_minus = add_button(master,"-")
    b_minus.grid(row=2,column=3,columnspan=1)
    b_multiply = add_button(master,"*")  
    b_multiply.grid(row=3,column=3,columnspan=1)
    b_divide = add_button(master,"/")
    b_divide.grid(row=4,column=3,columnspan=1)
    b_equal = add_button(master,"=")
    b_equal.grid(row=4,column=2,columnspan=1)
    b_delete = add_button(master,"c")
    b_delete.grid(row=4,column=0,columnspan=1)
    b_bracket1 = add_button(master, "(")
    b_bracket1.grid(row=1,column=5,columnspan=1)
    b_bracket2 = add_button(master, ")")
    b_bracket2.grid(row=2,column=5,columnspan=1)
    b_decimal = add_button(master, ".")
    b_decimal.grid(row=3,column=5,columnspan=1)
    b_square = add_button(master, "**")
    b_square.grid(row=4,column=5,columnspan=1)

    b_factor = add_button(master, "!")
    b_factor.grid(row=5,column=0,columnspan=1)
    b_absolut = add_button(master,"abs")
    b_absolut.grid(row=5,column=1, columnspan=1)
    b_sqrt = add_button(master, "√")
    b_sqrt.grid(row=5,column=2,columnspan=1)
   
    

def add_button(master, value):#gave value to buttons
    button=Button(master, text=value,width=9, command=lambda:clickButton(master,str(value)))
    return button

def  clickButton(master,value):
    #Get the equation that's entered by the user

    
    current_equation=str(master.equation.get())#current value for display. Fetches current values from display.
    if value == "c":
        master.equation.delete(0,END)#cleared the display
    elif value == "=":
        if '√'  in current_equation:
            ans = sqrt(current_equation)
        else:
            ans=eval(current_equation)#gives answer to display. Eval is a function which evaluates expression.
        master.equation.delete(0,END)
        master.equation.insert(-1, ans)
    elif value=="!":
        ans=fact(int(current_equation))
        master.equation.delete(0,END)
        master.equation.insert(-1, ans)
    else:
        master.equation.delete(0,END)
        master.equation.insert(-1, current_equation+value)#Concatenation is where two strings get added. 
 
    

    return master

def fact(value):#function of factorial 
    prod=1
    while(value>1):
        prod= value*prod
        value-=1
    return prod

def sqrt(value): 
    value = re.findall("\d+", value)
    value = int(value[0])
    result=value**0.5
    return result

    
    
  
root = Tk() #creating a blank window
main(root)
root.mainloop()




