from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()
    if password == "1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message= text1.get(1.0,END)
        decode_message = message.encode("ascii")
        base64_byte=base64.b64decode(decode_message)
        decrypt= base64_byte.decode("ascii")

        Label(screen2,text="DECRYPT", font="arial", fg="white",bg="#00bd56").place(x=10,y=0)
        text2 = Text(screen2,font="arial" , bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("encryption", "Invlid Password")

    #เปิด Function decrypt ขึ้นมาโดยอย่างแรกเช็ครหัสผ่าน หากไม่ตรงตรวจสอบว่าค่าว่างหรือไม่ว่าง หากว่าง ให้แสดงว่ากรอกเพิ่มเติมแต่หากผิดให้กรอกใหม่อีกครั้ง และเมื่อรหัสผ่านถูกต้องแล้ว
    # ให้ทำการ Popup หน้าต่างใหม่ขึ้นมาพร้อมแสดงข้อมูลของ decrypt โดยใช้ ascii แปลง

def encrypt():
    password=code.get()

    if password == "1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message= text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_byte=base64.b64encode(encode_message)
        encrypt= base64_byte.decode("ascii")

        Label(screen1,text="ENCRYPT", font="arial", fg="white",bg="#ed3833").place(x=10,y=0)
        text2 = Text(screen1,font="arial" , bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)
    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("encryption", "Invlid Password")
    #เปิด Function encrypt ขึ้นมาโดยอย่างแรกเช็ครหัสผ่าน หากไม่ตรงตรวจสอบว่าค่าว่างหรือไม่ว่าง หากว่าง ให้แสดงว่ากรอกเพิ่มเติมแต่หากผิดให้กรอกใหม่อีกครั้ง และเมื่อรหัสผ่านถูกต้องแล้ว
    # ให้ทำการ Popup หน้าต่างใหม่ขึ้นมาพร้อมแสดงข้อมูลของ encrypt โดยใช้ ascii แปลง

def main_screen () :

    global screen   #ประกาศตัวแปร Screen มาใช้งาน
    global code     #ประกาศตัวแปร code มาใช้งาน
    global text1    #ประกาศตัวแปร text1 มาใช้งาน

    
    screen = Tk()
    screen.geometry ("375x398")   
    #โค้ดข้างบนคือ การสร้างหน้า UI มาใช้งาน โดยกำหนดขนาดคือ 375*398

    #icon
    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False,image_icon)
    screen.title("Encryption and Decryption text")
    # ข้างบนคือ การกำหนด แทบบาร์ข้างบนและมีไอคอนและรูปนำไปใช้งานด้วย

    def reset():
        code.set("")
        text1.delete(1.0,END)
    #โค้ดด้านบนคือการเปิดค่า Function reset ข้อมูล text ให้เป็นค่าว่าง
    

    Label(text = "Enter Text for  Encryption and Decryption", fg="black" , font=("calbri", 13)).place(x=10,y=10)
    text1 = Text(font = "Robote 20", bg="white", relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    #เป็นตัว input ในการแปลงค่าเริ่มต้นจาก Encryption สู่ Decryption หรือ Decryption ไป Encryption

    Label(text="Enter Secret key for Encryption and Decryption",fg="black",font=("calbri",13)).place(x=10,y=170)
    code= StringVar()
    Entry(textvariable=code,width=19,bd=0, font=("arial",25),show="*").place(x=10,y=200)
    #เป็น input รหัสผ่านในการใช้ยื่นยันว่าถูกต้องไหม โดนใช้ ตัวแปร code ในการเก็บค่า

    Button(text="ENCRYPT", height="2",width=23,bg="#ed3833", fg="white",bd=0,command=encrypt).place(x= 10 , y=250)
    Button(text= "DECRYPT", height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text= "RESET", height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
    #สร้างปุ่ม 3 ปุ่มเรียกใช้งาน Function ที่แตกต่างกันโดยเรียงตามลำดับ ENCRYPT  DECRYPT RESET

    screen.mainloop()
    # ทำการลูปไปเรื่อยๆ จนกว่าจะมีการออกจากโปรแกรม

main_screen()