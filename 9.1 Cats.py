from tkinter import*
from PIL import Image, ImageTk
import requests
from io import BytesIO
from pygame.examples.moveit import load_image


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


def open_new_window():
    img = load_image(url)
    if img:
        # Создаем новое вторичное окно
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")

        # Добавляем изображение в новое окно
        label = Label(new_window, image=img)
        label.image = img  # Сохраняем ссылку на изображение
        label.pack()


def open_new_window(): # функция загрузки по тегу
    tag = tag_entry.get() #считываем тег – то что ввел пользователь
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'  # адрес с тегом
    img = load_image(url_with_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")

        label = Label(new_window, image=img)
        label.image = img  # Сохраняем ссылку на изображение
        label.pack()

def exit():
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry("600x520")

# Поле ввода для тегов
tag_entry = Entry()
tag_entry.pack()

# Кнопка для загрузки изображения с тегом
load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)


url = "https://cataas.com/cat"
''' img = load_image(url)
if img:
    label.config(image=img)
    label.image = img'''

window.mainloop()
