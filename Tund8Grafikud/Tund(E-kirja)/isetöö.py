# импорт для библиотеке
from tkinter import *
from tkinter import filedialog, messagebox
import smtplib, ssl
from email.message import EmailMessage
import imghdr

#переменная для файлов
file = None

# добовление img
def choose_img():
    global file
    file = filedialog.askopenfilename()#открывает окно выбора файла
    added.configure(text = file)# отображает путь в Label1
    added.configure(font=("Arial", 14, "italic"), fg="blue")
    return file
# отправка письма
def send():
    to = email.get() #Эмейл получателя
    message_box = message.get() # сообшение получателю
    topic_value = topic.get() #Заглавие к письму

    # Проверяет все ли поля заполнены
    if not to or not message_box or not topic or not file:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля и добавьте изображение.")
        return

    # Настройка сервера
    smtp_server = "smtp.gmail.com"
    port = 587 #порт для GMAIL
    sender_email = "andreilebedev321@gmail.com"  # Отправитель
    password = "dkzp hqff vvcf pgce "
    context = ssl.create_default_context()
    
    # Оформление письма
    msg = EmailMessage()
    msg.set_content(message_box)
    msg['Subject'] = topic_value
    msg['From'] = sender_email
    msg['To'] = to

    # прикрепляет изображение к письму
    with open(file, 'rb') as fimage:
        image = fimage.read()
        image_type = imghdr.what(None, image)
        msg.add_attachment(image, maintype='image', subtype=image_type)

    try:
        server = smtplib.SMTP(smtp_server, port)# подключение к серверу
        server.starttls(context=context) # шифрование
        server.login(sender_email, password) # Авторизуеться в Gmail.
        server.send_message(msg)# отправляет письмо
        messagebox.showinfo("Информация", "Письмо отправлено успешно!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось отправить письмо: {str(e)}")
    finally:
        server.quit()

# Создание окно 
root = Tk()
root.geometry("600x500")
root.resizable(False, False)
root.title("Email")

# Заметки
label1 = Label(root, text="EMAIL:", font=("Helvetica", 18), fg="green", bg="lightgray")
label1.place(x=0, y=0)

label2 = Label(root, text="TOPIC:", font=("Helvetica", 18), fg="green", bg="lightgray")
label2.place(x=0, y=50)

label3 = Label(root, text="ADD:", font=("Helvetica", 18), fg="green", bg="lightgray")
label3.place(x=0, y=100)

label4 = Label(root, text="MESSAGE:", font=("Helvetica", 18), fg="green", bg="lightgray")
label4.place(x=0, y=200)

#Кнопки
button1 = Button(root, text="ADD IMAGE", font=("Helvetica", 14, "bold"), bg="orange", fg="white", command=choose_img)
button1.place(x=250, y=350)

button2 = Button(root, text="SEND", font=("Helvetica", 14, "bold"), bg="blue", fg="white", command=send)
button2.place(x=400, y=350)

# Поля для ввода
email = Entry(root, font=("Arial", 18), bg="lightyellow")
email.place(x=190, y=0, width=300, height=50)

topic = Entry(root, font=("Arial", 18), bg="lightyellow")
topic.place(x=190, y=50, width=300, height=50)

added = Label(root, text="...", font=("Arial", 12, "italic"), fg="blue", bg="lightgray")
added.place(x=190, y=110, width=300, height=20)

message = Entry(root, font=("Arial", 16), bg="lightyellow")
message.place(x=190, y=130, width=300, height=200)

#Запускает главное окно
root.mainloop()
