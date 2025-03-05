from tkinter import *
from tkinter import filedialog, messagebox
import smtplib, ssl
from email.message import EmailMessage
import imghdr

file = None

def choose_img():
    global file
    file = filedialog.askopenfilename()
    added.configure(text = file)
    added.configure(font=("Arial", 14, "italic"), fg="blue")
    return file

def send():
    to = email.get()
    message_box = message.get()
    topic_value = topic.get()

    if not to or not message_box or not topic or not file:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля и добавьте изображение.")
        return

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "andreilebedev321@gmail.com"
    password = "dkzp hqff vvcf pgce "
    context = ssl.create_default_context()

    msg = EmailMessage()
    msg.set_content(message_box)
    msg['Subject'] = topic_value
    msg['From'] = sender_email
    msg['To'] = to

    with open(file, 'rb') as fimage:
        image = fimage.read()
        image_type = imghdr.what(None, image)
        msg.add_attachment(image, maintype='image', subtype=image_type)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Информация", "Письмо отправлено успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось отправить письмо: {str(e)}")
    finally:
        server.quit()

root = Tk()
root.geometry("600x500")
root.resizable(False, False)
root.title("Email")

label1 = Label(root, text="EMAIL:", font=("Helvetica", 18), fg="green", bg="lightgray")
label1.place(x=0, y=0)

label2 = Label(root, text="TOPIC:", font=("Helvetica", 18), fg="green", bg="lightgray")
label2.place(x=0, y=50)

label3 = Label(root, text="ADD:", font=("Helvetica", 18), fg="green", bg="lightgray")
label3.place(x=0, y=100)

label4 = Label(root, text="MESSAGE:", font=("Helvetica", 18), fg="green", bg="lightgray")
label4.place(x=0, y=200)

button1 = Button(root, text="ADD IMAGE", font=("Helvetica", 14, "bold"), bg="orange", fg="white", command=choose_img)
button1.place(x=250, y=350)

button2 = Button(root, text="SEND", font=("Helvetica", 14, "bold"), bg="blue", fg="white", command=send)
button2.place(x=400, y=350)

email = Entry(root, font=("Arial", 18), bg="lightyellow")
email.place(x=190, y=0, width=300, height=50)

topic = Entry(root, font=("Arial", 18), bg="lightyellow")
topic.place(x=190, y=50, width=300, height=50)

added = Label(root, text="...", font=("Arial", 12, "italic"), fg="blue", bg="lightgray")
added.place(x=190, y=110, width=300, height=20)

message = Entry(root, font=("Arial", 16), bg="lightyellow")
message.place(x=190, y=130, width=300, height=200)

root.mainloop()
