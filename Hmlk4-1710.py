import tkinter as tk
from PIL import Image, ImageTk


class ProfileApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2.1 - User Profile GUI")
        self.geometry("300x450")
        self.create_widgets()

    def create_widgets(self):
        # Фон
        bg_img = Image.open("C:/Users/MamaL/Pictures/fon2.jpg")
        bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label = tk.Label(self, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Фото профиля
        profile_img = Image.open("C:/Users/MamaL/Pictures/ivanov_271.jpg").resize((90, 90))
        profile_photo = ImageTk.PhotoImage(profile_img)
        profile_label = tk.Label(self, image=profile_photo, bd=2)
        profile_label.image = profile_photo
        profile_label.place(x=105, y=15)

        # Имя пользователя
        user_label = tk.Label(self, text="Кирилл Вертаев", font=("Arial", 18, "bold"), bg="#ADD8E6")
        user_label.place(x=80, y=120)

        # Биография
        bio_label = tk.Label(self, text="Биография", font=("Arial", 14), bg="#ADD8E6")
        bio_label.place(x=20, y=155)
        about_label = tk.Label(self, text="Я инженер-конструктор с стажем 1 год",
                               font=("Arial", 11), wraplength=260, justify="left", bg="#ADD8E6")
        about_label.place(x=20, y=180)

        # Умения
        skills_label = tk.Label(self, text="Умения", font=("Arial", 14), bg="#ADD8E6")
        skills_label.place(x=20, y=230)
        languages_label = tk.Label(self, text="3D-Cad/Тех.док", bg="#ADD8E6")
        languages_label.place(x=20, y=255)

        # Опыт
        experience_label = tk.Label(self, text="Опыт", font=("Arial", 14), bg="#ADD8E6")
        experience_label.place(x=20, y=285)
        developer_label = tk.Label(self, text="Инженер-конструктор", bg="#ADD8E6")
        developer_label.place(x=20, y=310)
        dev_dates_label = tk.Label(self, text="Март 2024 - настоящее время", font=("Arial", 10), bg="#ADD8E6")
        dev_dates_label.place(x=20, y=332)
        driver_label = tk.Label(self, text="Продавец-консультант", bg="#ADD8E6")
        driver_label.place(x=20, y=355)
        driver_dates_label = tk.Label(self, text="Июнь 2023 - Август 2023", font=("Arial", 10), bg="#ADD8E6")
        driver_dates_label.place(x=20, y=375)


if __name__ == "__main__":
    app = ProfileApp()
    app.mainloop()
