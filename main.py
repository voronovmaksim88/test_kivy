from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):  # Наш главный класс-приложение, наследуется от App
    def build(self):  # Этот метод создает и возвращает корневой виджет
        return Label(text='Привет, Kivy!')  # Создаем и возвращаем виджет "Метка" с текстом

# Запускаем наше приложение
if __name__ == '__main__':
    MyApp().run()