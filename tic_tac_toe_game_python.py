# Tic tac toe game 
from tkinter import*
from tkinter import messagebox  
root=Tk()
root.geometry("530x600+500+50")
root.configure(bg="powder blue")
root.title("TIC TAC TOE GAME Prepared By Arsalan")
root.resizable(False,False)
i=True
def checker(buttons):
    global i
    if buttons['text']==' ':
        if(i):
            i=False
            buttons['text']='X'
            winner()
        else:
            i=True
            buttons['text']='O'
            winner()

def reset():
    btn1['text']=''
    btn2['text']=''
    btn3['text']=''
    btn4['text']=''
    btn5['text']=''
    btn6['text']=''
    btn7['text']=''
    btn8['text']=''
    btn9['text']=''  

    btn1.configure(bg="gainsboro")
    btn2.configure(bg="gainsboro")
    btn3.configure(bg="gainsboro")
    btn4.configure(bg="gainsboro")
    btn5.configure(bg="gainsboro")
    btn6.configure(bg="gainsboro")
    btn7.configure(bg="gainsboro")
    btn8.configure(bg="gainsboro")
    btn9.configure(bg="gainsboro")
    
def winner():
    if (btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X'):
        btn1.configure(bg="yellow",fg="red")
        btn2.configure(bg="yellow",fg="red")
        btn3.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','X is WINNER')
    elif(btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X'):
        btn4.configure(bg="yellow",fg="red")
        btn5.configure(bg="yellow",fg="red")
        btn6.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','X is WINNER')
    elif(btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X'):
        btn7.configure(bg="yellow",fg="red")
        btn8.configure(bg="yellow",fg="red")
        btn9.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','X is WINNER') 
    elif(btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X'):
        btn1.configure(bg="yellow",fg="red")
        btn4.configure(bg="yellow",fg="red")
        btn7.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','X is WINNER')
    elif(btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X'):
        btn2.configure(bg="yellow",fg="red")
        btn5.configure(bg="yellow",fg="red")
        btn8.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','X is WINNER')
    elif(btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X'):
        btn3.configure(bg="yellow",fg="red")
        btn6.configure(bg="yellow",fg="red")
        btn9.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','X is WINNER') 
    elif(btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X'):
        btn1.configure(bg="yellow",fg="red")
        btn5.configure(bg="yellow",fg="red")
        btn9.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','X is WINNER')                  
    elif(btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X'):
        btn3.configure(bg="yellow",fg="red")
        btn5.configure(bg="yellow",fg="red")
        btn7.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','X is WINNER') 
# for winner O        
    elif (btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O'):
        btn1.configure(bg="yellow",fg="red")
        btn2.configure(bg="yellow",fg="red")
        btn3.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','O is WINNER')
    elif(btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O'):
        btn4.configure(bg="yellow",fg="red")
        btn5.configure(bg="yellow",fg="red")
        btn6.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','O is WINNER')
    elif(btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O'):
        btn7.configure(bg="yellow",fg="red")
        btn8.configure(bg="yellow",fg="red")
        btn9.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','O is WINNER') 
    elif(btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O'):
        btn1.configure(bg="yellow",fg="red")
        btn4.configure(bg="yellow",fg="red")
        btn7.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','O is WINNER')
    elif(btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O'):
        btn2.configure(bg="yellow",fg="red")
        btn5.configure(bg="yellow",fg="red")
        btn8.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','O is WINNER')
    elif(btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O'):
        btn3.configure(bg="yellow",fg="red")
        btn6.configure(bg="yellow",fg="red")
        btn9.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','O is WINNER') 
    elif(btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O'):
        btn1.configure(bg="yellow",fg="red")
        btn5.configure(bg="yellow",fg="red")
        btn9.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','O is WINNER')                  
    elif(btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O'):
        btn3.configure(bg="yellow",fg="red")
        btn5.configure(bg="yellow",fg="red")
        btn7.configure(bg="yellow",fg="red")
        messagebox.showinfo('Game Says','O is WINNER')
    elif (btn1['text']!=' ' and btn2['text']!=' ' and btn3['text']!=' ' and btn4['text']!=' ' and btn5['text']!=' ' and btn6['text']!=' ' and btn7['text']!=' ' and btn8['text']!=' ' and btn9['text']!=' '):
        btn1.configure(bg="blue",fg="red")
        btn2.configure(bg="blue",fg="red")
        btn3.configure(bg="blue",fg="red")
        btn4.configure(bg="blue",fg="red")
        btn5.configure(bg="blue",fg="red")
        btn6.configure(bg="blue",fg="red")
        btn7.configure(bg="blue",fg="red")
        btn8.configure(bg="blue",fg="red")
        btn9.configure(bg="blue",fg="red")        
        messagebox.showinfo('Game says ',"Tie Game")      
# buttons
mainframe=Frame(root,width=600,height=450)
mainframe.place(x=0,y=0)

btn1=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn1))
btn1.grid(row=0,column=0)

btn2=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn2))
btn2.grid(row=0,column=1)

btn3=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn3))
btn3.grid(row=0,column=2)

btn4=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn4))
btn4.grid(row=2,column=0)

btn5=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn5))
btn5.grid(row=2,column=1)

btn6=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn6))
btn6.grid(row=2,column=2)
6
btn7=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn7))
btn7.grid(row=3,column=0)

btn8=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn8))
btn8.grid(row=3,column=1)

btn9=Button(mainframe,text=" ",font=("arial",26,"bold"),bg="gainsboro",width=8,height=3,command=lambda:checker(btn9))
btn9.grid(row=3,column=2)

# reset Button
reset=Button(root,text="RESET",font=("arial",26,"bold"),bg="gainsboro",height=1,width=10,command=reset)
reset.place(x=155,y=500)          
root.mainloop()