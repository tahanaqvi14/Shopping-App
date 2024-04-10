from tkinter import *
import os.path
import datetime
from PIL import ImageTk, Image

r=Tk()
r.geometry('600x440')
r.configure(bg="#1A1A1A")
r.title("SMART SHOPPING APP")

products1 = (('Iphone 11', 3000), ('Redmi Note 8', 600), ('Oneplus 8', 7000), ('Samsung S22', 9000), ('Infinix HOT 10', 4000), ('Iphone 15', 5000), ('Huawei Y9', 3000), ('Vivo Y99', 1000), ('Iphone SE', 7600))
products = []

#Purchase history
def purchase_history():
    f3.destroy()
    global scrollbar,canvas,c3,product_frame
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    def scroll_up(event):
        canvas.yview_scroll(-1, "units")

    def scroll_down(event):
        canvas.yview_scroll(1, "units")

    scrollbar = Scrollbar(r)
    scrollbar.grid(row=0, column=2, sticky=N+S)
    history=[]

    canvas = Canvas(r, bg="#212121", width=410, height=370,highlightthickness=0)  # Fixed size canvas
    canvas.grid(row=0, column=1, padx=10, pady=10)

    c3 = Button(r, text='<<--Go Back', bg='#ADAFAF',command=lambda: options(3))
    c3.grid(row=1, column=0, padx=5, pady=5)

    # Bind the canvas to the scrollbar
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', on_configure)

    product_frame = Frame(canvas, bg="#212121", padx=10, pady=10)
    product_frame.grid(row=0, column=0, sticky="ew")  # Separate rows for each product
    canvas.create_window(0, 0, window=product_frame, anchor=NW)

    email=email_last

    if os.path.isfile('Userdata\\' + str(email) + '.txt'):
        with open(f'Userdata\\{email}.txt') as f:
            history = f.readlines()
            history = [i[:-1] for i in history]
        if history==[]:
            last_label1 = Label(product_frame, text="No purchase yet!", font=('lexend', 22), fg='white', bg='#E75628')
            last_label1.pack(anchor="w",padx=95, pady=5)
        else:
            for i in range(0, len(history), 5):
                text = f"{history[i]}\nCost: {history[i + 1]}\nQuantity: {history[i + 2]}\n{history[i + 3]}"
                last_label = Label(product_frame, text=text, font=('lexend', 12), fg='white', bg='#E75628',padx=10)
                last_label.pack(anchor="w",padx=95, pady=5)
    else:
        last_label1 = Label(product_frame, text="No purchase yet!", font=('lexend', 22), fg='white', bg='#E75628')
        last_label1.pack(anchor="w",padx=95, pady=5)


    canvas.yview_moveto(0.0)
    product_frame.bind("<MouseWheel>", lambda event: scroll_down(event) if event.delta < 0 else scroll_up(event))

    if len(history)<20:
        scrollbar.config(command=None)

def loginpage(n):
    
    def on_entry_click(event):
        if x.get() == "Email:":
            x.delete(0,END)
    def on_entry_click1(event):
        if y.get() == "Password:":
            y.delete(0,END)
    global x,y,f1

    f1 = Frame(r, bg="#212121")
    f1.grid(row=0, column=0,pady=20,padx=10)

    Label(f1, text='Sign in', font=('lexend', 28, 'bold'), bg='#212121', fg='white').grid(row=0, column=0, pady=15)

    x = Entry(f1, width=35, borderwidth=5)
    x.insert(0, "Email:")
    x.bind('<Button-1>', on_entry_click)
    x.grid(row=1, column=0,  pady=10)

    y = Entry(f1, width=35, borderwidth=5)
    y.insert(0, "Password:")
    y.bind('<Button-1>', on_entry_click1)
    y.grid(row=2, column=0,  pady=10)

    if n == 2:
        Label(f1, text='TRY AGAIN | ACCOUNT NOT FOUND', font=('lexend', 10, 'bold'), bg='black', fg='red').grid(row=3, column=0, pady=15)
    submit=Button(f1,text='Login' ,font=('lexend', 8, 'bold',),bg='#5050FD',fg='white',width=25,command=lambda: logedin(x.get(), y.get())).grid(row=4, column=0, pady=15)

def create_account(n):
    global f2
    f2 = Frame(r, bg="#212121")

    Label(f2, text='Create Account', font=('lexend', 28, 'bold'), bg='#212121', fg='white').grid(row=0, column=0, pady=15)
    def on_entry_click2(event):
        if email1.get() == "Enter email:":
            email1.delete(0,END)

    def on_entry_click3(event):
        
        if password.get() == "Enter your password[ATLEAST 8 CHARACTERS]:":
            password.delete(0, END)
  
    def on_entry_click4(event):
        if name.get() == "Enter your name:":
            name.delete(0,END)

    def on_entry_click5(event):
        if address.get() == "Enter your address:":
            address.delete(0,END)
    
    def on_entry_click6(event):
        if phone.get() == "Enter your phone number:":
            phone.delete(0,END)


    email1 = Entry(f2, width=35, borderwidth=5)
    email1.insert(0, "Enter email:")
    email1.bind('<Button-1>', on_entry_click2)
    email1.grid(row=1,column=0,pady=10)

    password = Entry(f2, width=35, borderwidth=5)
    password.insert(0, 'Enter your password[ATLEAST 8 CHARACTERS]:')
    password.bind('<Button-1>', on_entry_click3)
    password.grid(row=2,column=0,pady=10)

    name = Entry(f2, width=35, borderwidth=5)
    name.insert(0, "Enter your name:")
    name.bind('<Button-1>', on_entry_click4)
    name.grid(row=3,column=0,pady=10)

    address = Entry(f2, width=35, borderwidth=5)
    address.insert(0, "Enter your address:")
    address.bind('<Button-1>', on_entry_click5)
    address.grid(row=4,column=0,pady=10)

    phone = Entry(f2, width=35, borderwidth=5)
    phone.insert(0, "Enter your phone number:")
    phone.bind('<Button-1>', on_entry_click6)
    phone.grid(row=5,column=0,pady=10)
    if n==2:
        Label(f2,text='This email is occupied | Invalid password',font=('lexend', 10, 'bold',),bg='black',fg='red').grid(row=6,column=0,pady=10)
    elif n==3:
        Label(f2,text='Invalid password',font=('lexend', 10, 'bold',),bg='black',fg='red').grid(row=6,column=0,pady=10)
    elif n==4:        
        Label(f2,text='This email is occupied ',font=('lexend', 10, 'bold',),bg='black',fg='red').grid(row=6,column=0,pady=10)
    elif n==5:
        Label(f2,text='Enter appropriate credentials',font=('lexend', 10, 'bold',),bg='black',fg='red').grid(row=6,column=0,pady=10)
        
    submit = Button(f2, text='Create Account', font=('lexend', 8, 'bold'), width=25,bg='#5050FD', fg='white', command=lambda: writing(email1.get(), password.get(), name.get(), address.get(), phone.get())).grid(row=7,column=0,pady=3)
    f2.grid(row=0, column=1, pady=10,padx=70)

#Login Backend
def logedin(x,y):
    global f1,email_last
    x1=x
    if os.path.isfile('Userbasicdata\\'+str(x1)+'.txt'):# FILE SEARCHING (EMAIL MATCHING)        
        f=open('Userbasicdata\\'+str(x1)+'.txt','r')
        f.seek(0)
        content=f.read()
        content=content.split('\n')
        f.close()
        if content[4]==str(y): # PASSWORD MATCHING
            f1.destroy() 
            f2.destroy()
            email_last=x
            options(1)
        else:
            f1.destroy()
            loginpage(2)
    else:
        
        f1.destroy()
        loginpage(2)    

#Creating an account Backend
def writing(a, b, c, d, e):
    global email_last
    if a != "Enter email:" and a != '' and b != 'Enter your password[ATLEAST 8 CHARACTERS]:' and b != '' and c != "Enter your name:" and c != '' and d != "Enter your address:" and d != '' and e != "Enter your phone number:" and e != '':
        if os.path.isfile('Userbasicdata\\'+str(a)+'.txt') and len(b) < 8:
            f2.destroy()
            create_account(2)
            
        elif len(b) < 8:
            
            f2.destroy()
            create_account(3)
        elif os.path.isfile('Userbasicdata\\'+str(a)+'.txt'):
            f2.destroy()
            create_account(4)
        else:
            filename = a + '.txt'
            L = [a, c, d, e, b]
            with open(f'Userbasicdata\\{filename}', 'a+') as f:
                for i in L:
                    f.write(i + '\n')
            f1.destroy() 
            f2.destroy()
            email_last=a
            options(1)

    else:
        email_last=a
        f2.destroy()
        create_account(5)

#Add products to products list
def add_product(n,np):
    product_name = products1[n][0]
    product_price = products1[n][1]
    quantity=np
    products.append((product_name, int(product_price),quantity))

#Adding purchased products to file
def adding_to_history():
    global products,last_label
    with open(f'Userdata\\{email_last}.txt' , 'a') as f:
        for i in range(0 , len(products)):
            now = datetime.datetime.now()
            formatted = now.strftime("%d-%m-%Y %H:%M:%S")
            f.write(products[i][0]+'\n'+str(products[i][1])+'\n' + str(products[i][2])+'\n'+ formatted+'\n\n')
    label01.destroy()
    f7.destroy()    
    canvas.destroy() 
    frame.destroy()
    scrollbar.destroy()  
    c1.destroy()
    products[::] = []
    with open(f'Userbasicdata\\{email_last}.txt', 'a+') as f:
        f.seek(0)
        name=f.readlines()
        name=[i[:-1] for i in name]        
        last_label= Button(r, text=f"Thank you for your purchase\n {name[1]}!",font=('lexend', 25),fg='white',bg='#DB661F',relief='sunken',borderwidth=10,command=lambda: options(2))
        last_label.grid(padx=105,pady=20)        

##Cart
def view_cart():
    global label01, f7, cart_total, canvas, frame,scrollbar,c1,label14
    label1.destroy()
    Label12.destroy()
    f4.destroy()
    f42.destroy()
    f41.destroy()
    a.destroy()
    b.destroy()
    c.destroy()

    if products == []:
        label14 = Label(r, text='CART IS EMPTY!', font=('lexend', 45), bg="#1A1A1A", fg='white')
        label14.grid(row=2, column=0, padx=50, pady=10)
        c1=Button(r,text='<<--Go Back',command=lambda: func(-1))
        c1.grid(row=4, column=0, padx=10, pady=10)
    else:
        label01=Label(r,text='Your Cart',font=('lexend', 45),bg="#1A1A1A",fg='white') 
        label01.grid(row=0,column=0,columnspan=3)
        c1=Button(r,text='<<--Go Back',command=lambda: func(0))
        c1.grid(row=4,column=0,padx=10,pady=10)


        f7=Frame(r,bg="#212121",width=250,height=150)
        f7.grid_propagate(False)  # Ensure frame keeps its size
        f7.grid(column=2,row=2,padx=40) 

        def toggle_color(label):
            if label.winfo_exists():
                current_fg = label.cget("fg")
                new_fg = dark_fg_color if current_fg == dim_fg_color else dim_fg_color
                label.config(fg=new_fg)
                r.after(350, toggle_color, label)

        dim_fg_color = "white"
        dark_fg_color = "grey"

        a1=Label(f7,text='CheckOut',font=('lexend', 20),bg="#212121",fg='white') 
        a1.grid(column=0,pady=10,padx=60,columnspan=10)
        toggle_color(a1)

        canvas = Canvas(r, bg="#212121", width=250, height=250, highlightthickness=0)
        canvas.grid(row=2, column=0, pady=10, padx=10)

        scrollbar = Scrollbar(r, command=canvas.yview)
        scrollbar.grid(row=2, column=1, sticky=N+S)

        frame = Frame(canvas, bg="#212121")
        canvas.create_window((0, 0), window=frame, anchor='nw')

        canvas.config(yscrollcommand=scrollbar.set)
        frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

        
        cart_total=0
        update_display()

def update_display():
    global cart_total, products

    def onhover(event):
        event.widget.configure(cursor="hand2",bg='red')

    def offhover(event):
        event.widget.configure(cursor="arrow",bg='#E1EFF2')

    for widget in frame.winfo_children():
        widget.destroy()

    # for i, product in enumerate(products):
    for product in products:
        product_frame = Frame(frame, borderwidth=2, relief="groove",height=20,bg='#F1F1F1')
        # product_frame.grid_propagate(False)  # Ensure frame keeps its size
        product_frame.grid(padx=32,pady=5)
        product_label = Label(product_frame, text=f"{product[0]}: ${product[1]}:Quantity:{product[2]}",bg='#F1F1F1')
        product_label.grid(padx=15)
        total=int(product[1])*int(product[2])
        cart_total+=total
        remove_button = Button(product_frame, text="Remove", command=lambda p=product: remove_product(p))
        remove_button.grid(pady=5)
        remove_button.bind('<Enter>',onhover)
        remove_button.bind('<Leave>',offhover)         

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    final(cart_total)

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
#remove product
def remove_product(product):
    global products,cart_total
    if product in products:
        cart_total=0
        amount.destroy()
        products.remove(product)
        if products==[]:
            f7.destroy()
            label01.destroy()
            c1.destroy()
            canvas.destroy()
            scrollbar.destroy()
            view_cart()
        else:
            update_display()

def final(cart_total):
    global amount
    Button(f7,text='Pay' ,font=('lexend', 8, 'bold',),bg='#FF876C',fg='white',width=25,command=adding_to_history).grid(row=2,padx=30, column=0, pady=15)
    amount=Label(f7,text=f'Grand Total is:             ${cart_total}',font=('lexend 13 bold'),bg="#212121",fg='white') 
    amount.grid(row=1,pady=10)
##Cart

#Product page 1
def func(n):
    global label1,Label12,Label13,f4,f42,f41,a,b,c,spinbox1
    if n==2:
        button1.destroy()
        value=spinbox1.get()
        add_product(0,value)
    elif n==3:
        button2.destroy()
        value=spinbox2.get()

        add_product(1,value)
    elif n==4:
        value=spinbox3.get()
        button3.destroy()
        add_product(2,value)

    if n>1:
        label1.destroy()
        Label12.destroy()
        f4.destroy()
        f42.destroy()
        f41.destroy()
        a.destroy()
        b.destroy()
        c.destroy()
    elif n==0:
        label01.destroy()
        canvas.destroy()
        c1.destroy()
        scrollbar.destroy()
        f7.destroy()
    elif n==-1:
        label14.destroy()
        c1.destroy()
    elif n==-2:
        f3.destroy()

    def onhover(event):
        event.widget.configure(bg='#1ECF52',cursor="hand2")

    def offhover(event):
        event.widget.configure(bg='#FAB526',cursor="arrow")

    label1=Label(r,text='Products',font=('lexend', 45),bg="#1A1A1A",fg='white') 
    label1.grid(row=0,column=0,padx=5,columnspan=3)
    Label12=Label(r,text='Click on a product to add to your cart',font=('lexend', 15),bg="#1A1A1A",fg='#727272')
    Label12.grid(row=1,column=0,padx=5,columnspan=3)
    Label13=Label(r,text='',bg="#1A1A1A")
    Label13.grid(row=2,column=10,padx=5,columnspan=3)
    
    def spin1():
        global button1,spinbox1
        submit1.destroy()
        spinbox1 = Spinbox(f4, from_=1, to=10,width=10)
        spinbox1.grid(row=3,column=0)
        button1 = Button(f4, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func(2))
        button1.grid(row=4,column=0,pady=2)

    f4=Frame(r,bg="#212121")
    image_path = "images/iphone11.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f4, image=tk_image)
    label.image = tk_image 
    label.grid(row=0)
    Label(f4,text='Apple Iphone 11 256GB',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f4,text='$3000',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit1 = Button(f4, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin1)
    submit1.grid(row=3,column=0)
    submit1.bind('<Enter>',onhover)
    submit1.bind('<Leave>',offhover) 
    f4.grid(row=3,column=0,padx=10)

    def spin2():
        global button2,spinbox2
        submit2.destroy()
        spinbox2 = Spinbox(f41, from_=1, to=10,width=10)
        spinbox2.grid(row=3,column=0)

        button2 = Button(f41, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func(3))
        button2.grid(row=4,column=0,pady=2)

    f41=Frame(r,bg="#212121")    
    image_path = "images/s2.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f41, image=tk_image)
    label.image = tk_image 
    label.grid()
    Label(f41,text='Redmi Note 8',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f41,text='$600',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit2 = Button(f41, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin2)
    submit2.grid(row=3,column=0)
    submit2.bind('<Enter>',onhover)
    submit2.bind('<Leave>',offhover) 
    f41.grid(row=3,column=1,padx=5)

    def spin3():
        global button3,spinbox3
        submit.destroy()
        spinbox3 = Spinbox(f42, from_=1, to=10,width=10)
        spinbox3.grid(row=3,column=0)

        button3 = Button(f42, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func(4))
        button3.grid(row=4,column=0,pady=2)

    f42=Frame(r,bg="#212121")
    image_path = "images/oneplus8.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f42, image=tk_image)
    label.image = tk_image 
    label.grid()
    Label(f42,text='Oneplus 8',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f42,text='$2000',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit = Button(f42, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin3)
    submit.grid(row=3,column=0)
    submit.bind('<Enter>',onhover)
    submit.bind('<Leave>',offhover) 
    f42.grid(row=3,column=2,padx=5)

    a=Button(r,text='>>',command=lambda: func1(5))
    a.grid(row=4,column=2)
    b=Button(r,text='View Cart',command=view_cart)
    b.grid(row=4,column=1)
    c=Button(r,text='<<',state=DISABLED)
    c.grid(row=4,column=0,pady=10)  
#Product page 2
def func1(n):
    global label1,Label12,Label13,f4,f42,f41,a,b,c
    if n==2:
        button1.destroy()
        value=spinbox1.get()
        add_product(0,value)
    elif n==3:
        button2.destroy()
        value=spinbox2.get()
        add_product(1,value)
    elif n==4:
        value=spinbox3.get()
        button3.destroy()
        add_product(2,value)

    if n>1:
        label1.destroy()
        Label12.destroy()
        f4.destroy()
        f42.destroy()
        f41.destroy()
        a.destroy()
        b.destroy()
        c.destroy()

    def onhover(event):
        event.widget.configure(bg='#1ECF52',cursor="hand2")

    def offhover(event):
        event.widget.configure(bg='#FAB526',cursor="arrow")

    label1=Label(r,text='Products',font=('lexend', 45),bg="#1A1A1A",fg='white') 
    label1.grid(row=0,column=0,padx=5,columnspan=3)
    Label12=Label(r,text='Click on a product to add to your cart',font=('lexend', 15),bg="#1A1A1A",fg='#727272')
    Label12.grid(row=1,column=0,padx=5,columnspan=3)
    Label13=Label(r,text='',bg="#1A1A1A")
    Label13.grid(row=2,column=10,padx=5,columnspan=3)
    
    def spin1():
        global button1,spinbox1
        submit1.destroy()
        spinbox1 = Spinbox(f4, from_=1, to=10,width=10)
        spinbox1.grid(row=3,column=0)

        button1 = Button(f4, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func1(2))
        button1.grid(row=4,column=0,pady=2)

    f4=Frame(r,bg="#212121")
    image_path = "images/s22.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f4, image=tk_image)
    label.image = tk_image 
    label.grid(row=0)
    Label(f4,text='Samsung S22',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f4,text='$9000',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit1 = Button(f4, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin1)
    submit1.grid(row=3,column=0)
    submit1.bind('<Enter>',onhover)
    submit1.bind('<Leave>',offhover) 
    f4.grid(row=3,column=0,padx=10)

    def spin2():
        global button2,spinbox2
        submit2.destroy()
        spinbox2 = Spinbox(f41, from_=1, to=10,width=10)
        spinbox2.grid(row=3,column=0)

        button2 = Button(f41, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func1(3))
        button2.grid(row=4,column=0,pady=2)

    f41=Frame(r,bg="#212121")    
    image_path = "images/infinix.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f41, image=tk_image)
    label.image = tk_image 
    label.grid()
    Label(f41,text='Infinix HOT 10',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f41,text='$4000',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit2 = Button(f41, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin2)
    submit2.grid(row=3,column=0)
    submit2.bind('<Enter>',onhover)
    submit2.bind('<Leave>',offhover) 
    f41.grid(row=3,column=1,padx=5)

    def spin3():
        global button3,spinbox3
        submit.destroy()
        spinbox3 = Spinbox(f42, from_=1, to=10,width=10)
        spinbox3.grid(row=3,column=0)

        button3 = Button(f42, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func1(4))
        button3.grid(row=4,column=0,pady=2)
    
    f42=Frame(r,bg="#212121")
    image_path = "images/iphone15.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f42, image=tk_image)
    label.image = tk_image 
    label.grid()
    Label(f42,text='Iphone 15',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f42,text='$5000',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit = Button(f42, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin3)
    submit.grid(row=3,column=0)
    submit.bind('<Enter>',onhover)
    submit.bind('<Leave>',offhover)
    f42.grid(row=3,column=2,padx=5)

    a=Button(r,text='>>',command=lambda: func2(5))
    a.grid(row=4,column=2)

    b=Button(r,text='View Cart',command=view_cart)
    b.grid(row=4,column=1)

    c=Button(r,text='<<',command=lambda: func(5))
    c.grid(row=4,column=0,pady=10)  
#Product page 3
def func2(n):
    global label1,Label12,Label13,f4,f42,f41,a,b,c
    if n==2:
        button1.destroy()
        value=spinbox1.get()
        add_product(0,value)
    elif n==3:
        button2.destroy()
        value=spinbox2.get()

        add_product(1,value)
    elif n==4:
        value=spinbox3.get()
        button3.destroy()
        add_product(2,value)

    if n>1:
        label1.destroy()
        Label12.destroy()
        f4.destroy()
        f42.destroy()
        f41.destroy()
        a.destroy()
        b.destroy()
        c.destroy()


    def onhover(event):
        event.widget.configure(bg='#1ECF52',cursor="hand2")

    def offhover(event):
        event.widget.configure(bg='#FAB526',cursor="arrow")

    label1=Label(r,text='Products',font=('lexend', 45),bg="#1A1A1A",fg='white') 
    label1.grid(row=0,column=0,padx=5,columnspan=3)
    Label12=Label(r,text='Click on a product to add to your cart',font=('lexend', 15),bg="#1A1A1A",fg='#727272')
    Label12.grid(row=1,column=0,padx=5,columnspan=3)
    Label13=Label(r,text='',bg="#1A1A1A")
    Label13.grid(row=2,column=10,padx=5,columnspan=3)
    
    def spin1():
        global button1,spinbox1
        submit1.destroy()
        spinbox1 = Spinbox(f4, from_=1, to=10,width=10)
        spinbox1.grid(row=3,column=0)

        button1 = Button(f4, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func2(2))
        button1.grid(row=4,column=0,pady=2)

    f4=Frame(r,bg="#212121")
    image_path = "images/y9.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f4, image=tk_image)
    label.image = tk_image 
    label.grid(row=0)
    Label(f4,text='Huawei Y9',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f4,text='$3000',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit1 = Button(f4, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin1)
    submit1.grid(row=3,column=0)
    submit1.bind('<Enter>',onhover)
    submit1.bind('<Leave>',offhover) 
    f4.grid(row=3,column=0,padx=10)

    def spin2():
        global button2,spinbox2
        submit2.destroy()
        spinbox2 = Spinbox(f41, from_=1, to=10,width=10)
        spinbox2.grid(row=3,column=0)

        button2 = Button(f41, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func2(3))
        button2.grid(row=4,column=0,pady=2)


    f41=Frame(r,bg="#212121")    
    image_path = "images/vivo.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f41, image=tk_image)
    label.image = tk_image 
    label.grid()
    Label(f41,text='Vivo Y99',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f41,text='$1000',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit2 = Button(f41, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin2)
    submit2.grid(row=3,column=0)
    submit2.bind('<Enter>',onhover)
    submit2.bind('<Leave>',offhover) 
    f41.grid(row=3,column=1,padx=5)

    def spin3():
        global button3,spinbox3
        submit.destroy()
        spinbox3 = Spinbox(f42, from_=1, to=10,width=10)
        spinbox3.grid(row=3,column=0)

        button3 = Button(f42, text='Confirm', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=lambda: func2(4))
        button3.grid(row=4,column=0,pady=2)
    

    f42=Frame(r,bg="#212121")
    image_path = "images/iphonese.png"
    image = Image.open(image_path)
    new_width=180
    new_height=180
    image = image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(image)
    label = Label(f42, image=tk_image)
    label.image = tk_image 
    label.grid()
    Label(f42,text='Iphone SE',font=('lexend', 13),bg="#212121",fg='white').grid(row=1,column=0)
    Label(f42,text='$7600',font=('lexend', 10),bg="#212121",fg='white').grid(row=2,column=0)
    submit = Button(f42, text='Add To Cart', font=('lexend', 8, 'bold'), width=15,height=1,bg='#FAB526', fg='black', relief='raised',borderwidth=1.5,command=spin3)
    submit.grid(row=3,column=0)
    submit.bind('<Enter>',onhover)
    submit.bind('<Leave>',offhover)

    f42.grid(row=3,column=2,padx=5)

    a=Button(r,text='>>',state=DISABLED)
    a.grid(row=4,column=2)

    b=Button(r,text='View Cart',command=view_cart)
    b.grid(row=4,column=1)

    c=Button(r,text='<<',command=lambda: func1(5))
    c.grid(row=4,column=0,pady=10)  
#Main Menu
def options(n):
    global f3
    if n==2:
        last_label.destroy()
    if n==3:
        global scrollbar,canvas,c3,product_frame
        scrollbar.destroy()
        canvas.destroy()
        c3.destroy()
        product_frame.destroy()




    def onhover(event):
        event.widget.configure(bg='black')

    def offhover(event):
        event.widget.configure(bg='#212121')

    f3=Frame(r,bg="#1A1A1A")

    label1=Label(f3,text='Select an option:',font=('lexend 35 underline'),bg='#1A1A1A',fg='white')
    label1.grid(row=0,column=5,columnspan=6)

    showproduct=Button(f3,text='Show Products',font=('lexend', 18),bg='#1A1A1A',fg='white',cursor="hand2",relief='solid',borderwidth='3',padx=12,pady=12,command=lambda: func(-2))
    showproduct.grid(row=1,pady=10,padx=50,column=5)
    showproduct.bind('<Enter>',onhover)
    showproduct.bind('<Leave>',offhover)

    history=Button(f3,text='Purchase History',font=('lexend', 18),bg='#1A1A1A',fg='white',cursor="hand2",relief='solid',borderwidth='3',padx=12,pady=12,command=purchase_history)
    history.grid(row=1,column=7,pady=10,columnspan=15)
    history.bind('<Enter>',onhover)
    history.bind('<Leave>',offhover)    
    # f4=Frame(f3,width=100, height=100, background="bisque")
    f3.grid()

def destroyy():
    f.destroy()
    loginpage(1)    
    create_account(1)

f=Frame(r,bg="#1A1A1A")

def toggle_color(label):
    # Check if the label is still valid before accessing its properties
    if label.winfo_exists():
        current_fg = label.cget("fg")
        new_fg = dark_fg_color if current_fg == dim_fg_color else dim_fg_color
        label.config(fg=new_fg)
        r.after(350, toggle_color, label)

dim_fg_color = "white"
dark_fg_color = "grey"
first=Button(f,text='WELCOME TO THE SMART SHOPPING APP',font=('lexend', 18, 'bold','underline'),bg='#2B2E32',fg='white',relief='raised',borderwidth='20',padx=3,pady=3,command=destroyy).grid(row=0,column=0,pady=15,padx=15)
label1=Label(f,text='Click on the above button to continue',font=('lexend', 15),bg='#1A1A1A',fg='white')
label1.grid(row=1,column=0)
toggle_color(label1)
f.grid()
r.mainloop()