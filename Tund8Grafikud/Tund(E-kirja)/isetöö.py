import imghdr
import smtplib
import ssl
from email.message import EmailMessage
from tkinter import messagebox, filedialog, Tk, Label, Button, Entry, END

def vali_pilt():
    global file
    file = filedialog.askopenfilename()
    l_lisatud.configure(text=file)
    return file

def saada_kiri():
    kellele = email_box.get().strip() 
    
    if not kellele:
        messagebox.showerror("Tekkis viga", "Emaili aadress on puudu")
        return
    
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "andreilebedev321@gmail.com"
    password = "" 
    context = ssl.create_default_context()
    
    kiri = "This is the email body" 

    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = "E-kiri saatmine"
    msg['From'] = sender_email  
    msg['To'] = kellele

    try:
        with open(file, 'rb') as fpilt:
            pilt = fpilt.read()
        msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
    except Exception as e:
        messagebox.showerror("Tekkis viga", f"Viga pildi lisamisel: {e}")
        return

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Informatsioon", "Kiri oli saadetud")
    except Exception as e:
        messagebox.showerror("Tekkis viga", f"Viga kirja saatmisel: {e}")
    finally:
        server.quit()

root = Tk()
root.title("Email Sender")

email_label = Label(root, text="Recipient Email:")
email_label.pack()

email_box = Entry(root, width=30)  
email_box.pack()

valida_button = Button(root, text="Vali Pilt", command=vali_pilt)
valida_button.pack()

l_lisatud = Label(root, text="No file selected")
l_lisatud.pack()

saada_button = Button(root, text="Saada Kiri", command=saada_kiri)
saada_button.pack()

root.mainloop()
