import tkinter as tk


class calculadora:
    def __init__(self,master):
        self.master = master
        self.display = tk.Entry(master,width=18, font=("Arial",23), bd=15, insertwidth=3, bg="#9333FF", justify="right")
        self.display.grid(row=0, column=0,columnspan=4)
        self.operation_verification = False
        self.current = ''
        self.op = ''
        self.total = 0

        row = 1
        col = 0
        
        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "C","0",".","+",
            "=",
            "HI"  # Botón adicional para enviar un mensaje
        ]
        for button in buttons:
            self.build_buttons(button,row,col)
            col+=1
            if col>3:
                col=0
                row+=1

        self.master.bind("<Key>",self.press_key)
    
    def press_key(self,event):
        key = event.char
        if key == "\r":
            self.calculated()
            return 
        elif key == "\x08":
            self.clear_display()
            return
        elif key == "\x1b":
            self.master.quit()
            return
        self.click(key)

    def click(self,key):
        if self.operation_verification:
            self.operation_verification = False

        self.display.insert(tk.END,key)
        
        if key in '0123456789' or key == '.':
            self.current+=key
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)

            self.current=''
            self.operation_verification = True
            self.op = key

    def calculated(self):
        if self.current and self.op:
            if self.op == '/':
                self.total/=float(self.current)
            if self.op == '*':
                self.total*=float(self.current)    
            if self.op == '+':
                self.total+=float(self.current)
            if self.op == '-':
                self.total-=float(self.current)
           
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,round(self.total,3))
    
    def clear_display(self):
        self.display.delete(0,tk.END)
        self.operation_verification = False
        self.current = ''
        self.op= ''
        self.total = 0
    
    def build_buttons(self,button,row,col):
        if button == "C":
            b = tk.Button(self.master,text=button,width=10,command=lambda: self.clear_display())
            
        elif button == '=':
            b = tk.Button(self.master,text=button,width=10,command=lambda: self.calculated())
        elif button == "HI":  # Botón para enviar un mensaje
            b = tk.Button(self.master,text=button,width=10,command=self.send_message)
            b.grid(pady=8)

        else:
             b = tk.Button(self.master,text=button,width=10,command=lambda: self.click(button))
        b.grid(row=row,column=col)

    def send_message(self):
        message = "I LOVE U"
        self.display.delete(0,tk.END)
        self.display.insert(tk.END, message)

root = tk.Tk()
root.title("LOVECALC")
root.resizable(False,False)
my_gui = calculadora(root)

root.mainloop()
