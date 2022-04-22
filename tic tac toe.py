 
from tkinter import *
from tkinter import messagebox

 

def ButtonClick(button):
    global x_o, flag
    button ["bg"] = "#000000"
    if button["text"] == "" and x_o == True:
        button ["text"] = "x"
        x_o = False
        Checkforwin()
         
         
        flag = flag  + 1
    elif button["text"] == "" and x_o == False:
        button["text"] = "o"
        x_o = True
        Checkforwin()
         
         
        flag =flag + 1
    else:
        messagebox.showerror("tic tac toe", "player has already entered")    




"""
1 2 3
4 5 6
7 8 9
1 5 9
3 5 7
1 4 7
2 5 8
3 6 9

"""
def Checkforwin():
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9
    if Button1["text"] == "x" and Button2["text"] == "x" and Button3["text"] == "x" or Button4["text"] == "x" and Button5["text"] == "x" and Button6["text"] == "x" or Button7["text"] == "x" and Button8["text"] == "x" and Button9["text"] == "x" or Button1["text"] == "x" and Button4["text"] == "x" and Button7["text"] == "x" or Button2["text"] == "x" and Button5["text"] == "x" and Button8["text"] == "x" or Button3["text"] == "x" and Button6["text"] == "x" and Button9["text"] == "x" or Button1["text"] == "x" and Button5["text"] == "x" and Button9["text"] == "x" or Button3["text"] == "x" and Button5["text"] == "x" and Button7["text"] == "x":
        messagebox.showinfo("tic tac toe", "player x has win the game!")
    elif Button1["text"] == "o" and Button2["text"] == "o" and Button3["text"] == "o" or Button4["text"] == "o" and Button5["text"] == "o" and Button6["text"] == "o" or Button7["text"] == "o" and Button8["text"] == "o" and Button9["text"] == "o" or Button1["text"] == "o" and Button4["text"] == "o" and Button7["text"] == "o" or Button2["text"] == "o" and Button5["text"] == "o" and Button8["text"] == "o" or Button3["text"] == "o" and Button6["text"] == "o" and Button9["text"] == "o" or Button1["text"] == "o" and Button5["text"] == "o" and Button9["text"] == "o" or Button3["text"] == "o" and Button5["text"] == "o" and Button7["text"] == "o":
        messagebox.showinfo("tic tac toe","player o has win the game!")     
    elif flag == 8:
        messagebox.showinfo("tic tac toe","The game is a tie")
   


main = Tk()
main.title("tic tac toe")
x_o = True
 
flag = 0

Button1 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7", fg= "white", width=3, command=lambda: ButtonClick(Button1))
Button1.grid(row=0,column=0)

Button2 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7", fg= "white", width=3, command=lambda: ButtonClick(Button2))
Button2.grid(row=0,column=1)

Button3 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7",  fg= "white", width=3, command=lambda: ButtonClick(Button3))
Button3.grid(row=0,column=2)

Button4 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7",fg= "white", width=3, command=lambda: ButtonClick(Button4))
Button4.grid(row=1,column=0)

Button5 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7",  fg= "white", width=3, command=lambda: ButtonClick(Button5))
Button5.grid(row=1,column=1)

Button6 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7",  fg= "white", width=3, command=lambda: ButtonClick(Button6))
Button6.grid(row=1,column=2)

Button7 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7",  fg= "white", width=3, command=lambda: ButtonClick(Button7))
Button7.grid(row=2,column=0)

Button8 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7",  fg= "white", width=3, command=lambda: ButtonClick(Button8))
Button8.grid(row=2,column=1)

Button9 = Button(main, text="", font=("arial", 60,"bold"), bg= "#ffb5a7",  fg= "white", width=3, command=lambda: ButtonClick(Button9))
Button9.grid(row=2,column=2)









main.mainloop()