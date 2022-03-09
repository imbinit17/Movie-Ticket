from tkinter import *
from fpdf import FPDF


def function():
    name = str(entryBox1.get())
    mobile = str(entryBox2.get())
    seats = int(entryBox3.get())
    seatType = int(seat.get())
    
    
    if(seatType==1):
        tag = "Bronze"
        price = 200
    elif(seatType==2):
        tag = "Silver"
        price = 400
    elif(seatType==3):
        tag = "Gold"
        price = 800
    elif(seatType==4):
        tag = "Platinum"
        price = 1200

    total = price * seats
    discount = 0.0
    if(total>1500 and total<2500):discount = 0.1 * total
    elif(total>2500 and total<5000):discount = 0.15 * total
    elif(total>5000): discount = 0.2 * total

    final_amt = total - discount

    txt1 = "Customer Name : " + name
    txt2 = "Mobile Number : " + mobile
    txt3 = "Seat Type : " + tag
    txt4 = "Per Seat Price : " + str(price)
    txt5 = "Number of Seats : " + str(seats)
    txt6 = "Gross Total : " + str(total)
    txt7 = "Discount : " +str(int(discount))
    txt8 = "Final Amount to be paid : " + str(int(final_amt))
    
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times",'BIU',size = 35)
    pdf.cell(200,20,txt="INOX Bill Receipt",ln=1,align="C")
    pdf.set_font("Times",'I',size = 15)
    pdf.cell(200,10,txt=txt1,ln=2,align="L")
    pdf.cell(200,10,txt=txt2,ln=3,align="L")
    pdf.cell(200,10,txt=txt3,ln=4,align="L")
    pdf.cell(200,10,txt=txt4,ln=5,align="L")
    pdf.cell(200,10,txt=txt5,ln=6,align="L")
    pdf.cell(200,10,txt=txt6,ln=7,align="L")
    pdf.cell(200,10,txt=txt7,ln=8,align="L")
    pdf.cell(200,10,txt=txt8,ln=9,align="L")

    pdf.output("receipt.pdf")


window = Tk()
window.geometry("600x450")
window.title("Bill Calculation Dashboard")

bg = PhotoImage(file="bg.png")
bg_img = Label(window,image=bg)
bg_img.place(x=0,y=0)

heading = Label(window,text="INOX",font=("Cambria",30),bg="Black",fg ="White")
heading.place(x=250,y=5)

label1 = Label(window,text="Enter Customer's Name ",font=("Times New Roman",15),bg="Black",fg ="White").place(x=5 ,y=70)
label2 = Label(window,text="Enter Customer's Mobile Number",font=("Times New Roman",15),bg="Black",fg ="White").place(x=5,y=110)
label3 = Label(window,text="Select the seat tier",font=("Times New Roman",15),bg="Black",fg ="White").place(x=5,y=150)

seat = IntVar()
rBtn1 = Radiobutton(window,text="Bronze",font=("Times New Roman",15),variable=seat,value=1,bg="Black",fg ="White").place(y=190)
rBtn2 = Radiobutton(window,text="Silver",font=("Times New Roman",15),variable=seat,value=2,bg="Black",fg ="White").place(y=220)
rBtn3 = Radiobutton(window,text="Gold",font=("Times New Roman",15),variable=seat,value=3,bg="Black",fg ="White").place(y=250)
rBtn4 = Radiobutton(window,text="Platinum",font=("Times New Roman",15),variable=seat,value=4,bg="Black",fg ="White").place(y=280)

label4 = Label(window,text="Number of seats booked : ",font=("Times New Roman",15),bg="Black",fg ="White").place(x=5,y=320)

entryBox1 = Entry(window,width=30,bg="Light Grey",font=("Times New Roman",13),fg ="Black")
entryBox1.place(x=295,y=73)
entryBox2 = Entry(window,width=30,bg="Light Grey",font=("Times New Roman",13),fg ="Black")
entryBox2.place(x=295,y=113)
entryBox3 = Entry(window,width=30,bg="Light Grey",font=("Times New Roman",13),fg ="Black")
entryBox3.place(x=295,y=323)

submitBtn = Button(window,text="Submit" ,width=20 ,bg ="Black" ,fg="White",command=function,font=("Times New Roman",15)).place(x=230,y=370)

mainloop()
