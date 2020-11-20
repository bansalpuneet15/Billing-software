from tkinter import *
import math, random, os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1750x1050')
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # ---------------------- VARIABLES ------------------
        self.product = StringVar()
        self.quantity = IntVar()
        self.price = IntVar()
        self.product_total = IntVar()

        # ---------Total Product Price ---------------
        self.total_price = StringVar()

        # ------------------Customer-------------------
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        self.l = list()

        # ---------------------- Customer Detail Frame ------------------------
        f1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        f1.place(x=0, y=80, relwidth=1)

        cname_label = Label(f1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(f1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_label = Label(f1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(f1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_btn = Button(f1, text="Add", width=10, bd=7, font="arial 12 bold", command=self.add_cust).grid(row=0, column=4, pady=20, padx=10)

        c_bill_label = Label(f1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=5, padx=20, pady=5)
        c_bill_txt = Entry(f1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=6, pady=5, padx=10)

        bill_btn = Button(f1, text="Search", width=10, bd=7, font="arial 12 bold", command=self.find_bill).grid(row=0, column=7, pady=10, padx=20)

        # -----------------Product details Frame -----------------------
        f2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Product Details", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        f2.place(x=0, y=180, height=460, width=600)

        product_lbl = Label(f2, text="Product Name", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=40, pady=5)
        product_txt = Entry(f2, width=15, textvariable=self.product, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=20)

        quantity_lbl = Label(f2, text="Quanity", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=40, pady=5)
        quantity_txt = Entry(f2, width=15, textvariable=self.quantity, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=20)

        price_lbl = Label(f2, text="Price", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=40, pady=5)
        price_txt = Entry(f2, width=15, textvariable=self.price, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=20)

        add_btn = Button(f2, text="Add", width=15, bd=7, font="arial 12 bold", command=self.add_item).grid(row=3, column=1, pady=20, padx=50)

        # --------------------Bill Area Frame -----------------------
        f5 = Frame(self.root, bd=7, relief=GROOVE)
        f5.place(x=600, y=188, height=460, width=940)
        bill_title = Label(f5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(f5, orient=VERTICAL)
        self.txtarea = Text(f5, yscrollcommand=scroll_y.set, font=("Helvetica", 11))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ---------Button Frame-------------
        f6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        f6.place(x=0, y=640, relwidth=1, height=160)

        m1_lbl=Label(f6, text="Total Price", bg=bg_color, fg="lightgreen", font=("times new roman", 17, "bold")).grid(row=0, column=0, padx=40, pady=5, sticky=W)
        m1_txt = Entry(f6, width=24, textvariable=self.total_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=40, pady=45)

        btn_f = Frame(f6, bd=7, relief=GROOVE)
        btn_f.place(x=600, width=715, height=100)

        total_btn = Button(btn_f, text="Total", bg="cadetblue", fg="white", bd=2, pady=15, width=12, font="arial 15 bold", command=self.total).grid(row=0, column=0, padx=10, pady=5)
        GBill_btn = Button(btn_f, text="Generate Bill", bg="cadetblue", fg="white", bd=2, pady=15, width=12, font="arial 15 bold", command=self.bill_area).grid(row=0, column=1, padx=10, pady=5)
        Clear_btn = Button(btn_f, text="Clear", bg="cadetblue", fg="white", bd=2, pady=15, width=12, font="arial 15 bold", command=self.clear_data).grid(row=0, column=2, padx=10, pady=5)
        Exit_btn = Button(btn_f, text="Exit", bg="cadetblue", fg="white", bd=2, pady=15, width=12, font="arial 15 bold", command=self.exit_app).grid(row=0, column=3, padx=10, pady=5)

        self.welcome_bill()

    def total(self):
        self.t_price = float(
            sum(self.l)
        )
        self.total_price.set(str(self.t_price))

    def welcome_bill(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END, "\t\t\t\t\t\tWelcome Webcode Retail\n")
        self.txtarea.insert(END, f"\n\t\t\t Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\t\t\t\t     Customer Name: ")
        self.txtarea.insert(END, f"\n\t\t\t Phone Number: ")
        self.txtarea.insert(END, f"\n\t\t===================================================================================")
        self.txtarea.insert(END, f"\n\t\t\tProduct\t\t  QTY\t\tPrice/item\t\t  Total Price")
        self.txtarea.insert(END, f"\n\t\t===================================================================================")

    def add_cust(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END, "\t\t\t\t\t\tWelcome Webcode Retail\n")
        self.txtarea.insert(END, f"\n\t\t\t Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\t\t\t\t     Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n\t\t\t Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n\t\t===================================================================================")
        self.txtarea.insert(END, f"\n\t\t\tProduct\t\t  QTY\t\tPrice/item\t\t  Total Price")
        self.txtarea.insert(END, f"\n\t\t===================================================================================")


    def add_item(self):
        self.p = (self.product.get())
        self.q = (self.quantity.get())
        self.pr = (self.price.get())
        self.pt = (self.quantity.get()*self.price.get())
        # ----------Cosmetics------------------
        if self.p !="" and self.q !=0 and self.pr !=0 and self.pt !=0:
            self.txtarea.insert(END, f"\n\t\t\t{self.p}\t\t   {self.q}\t\t      {self.pr}\t\t      {self.pt}")
            self.l.append(self.pt)

        self.product.set("")
        self.quantity.set(0)
        self.price.set(0)

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error", "Customer Details are must")
        elif self.total_price.get() == "0.0" and self.grocery_price.get() == "0.0" and self.cold_drink_price.get() == "0.0" :
            messagebox.showerror("Error", "No Product purchased")
        else:
            self.txtarea.insert(END, f"\n\t\t===================================================================================")
            self.txtarea.insert(END, f"\n\t\t\t\t\t\t    Total Bill: \t\t     {self.t_price}")
            self.txtarea.insert(END, f"\n\t\t===================================================================================")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do You Want to save the Bill?")
        if op>0:
            self.bill_data = self.txtarea.get(1.0, END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no.: {self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                self.c_name.set("")
                self.c_phone.set("")
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete(1.0,END)
                for d in f1:
                    self.txtarea.insert(END, d)
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        # -------------------Cosmetics--------------------
        self.product.set(0)
        self.quantity.set(0)
        self.price.set(0)
        self.product_total.set(0)

        # ---------Total Product Price and Tax variable---------------
        self.total_price.set("")

        # ------------------Customer-------------------
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x=random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.l = []
        self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op>0:
            self.root.destroy()



root=Tk()
obj = Bill_App(root)
root.mainloop()
