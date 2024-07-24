import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from plyer import notification

t = tk.Tk()
t.title("Notifier-App")
t.geometry("500x300")

try:
    img = Image.open("notify.png")
    tkimage = ImageTk.PhotoImage(img)
    img_label = tk.Label(t, image=tkimage)
    img_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
except FileNotFoundError:
    messagebox.showerror("Error", "Image file 'notify.png' not found!")

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        try:
            int_time = int(get_time)
            min_to_sec = int_time * 60
            messagebox.showinfo("Notifier set", "Notification set!")

            t.withdraw()

            
            t.after(min_to_sec * 1000, lambda: send_notification(get_title, get_msg))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for time!")

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Notifier",
        timeout=10
    )


tk.Label(t, text="Title to notify", font=("poppins", 10)).grid(row=1, column=0, padx=10, pady=5)
title = tk.Entry(t, width='25', font=("poppins", 13))
title.grid(row=1, column=1, padx=10, pady=5)

tk.Label(t, text="Display Message", font=("poppins", 10)).grid(row=2, column=0, padx=10, pady=5)
msg = tk.Entry(t, width='40', font=("poppins", 13))
msg.grid(row=2, column=1, padx=10, pady=5)

tk.Label(t, text="Set time (minutes)", font=("poppins", 10)).grid(row=3, column=0, padx=10, pady=5)
time1 = tk.Entry(t, width='5', font=("poppins", 13))
time1.grid(row=3, column=1, padx=10, pady=5)


tk.Button(t, text="SET NOTIFICATION", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#528DFF",
          width=20, relief="raised", command=get_details).grid(row=4, column=0, columnspan=2, pady=10)

t.mainloop()
