from kivy.app import App
from kivy.utils import platform

class MyApp(App):  # Наш главный класс-приложение, наследуется от App
    @staticmethod
    def _set_android_orientation():
        """Устанавливает принудительную горизонтальную ориентацию для Android"""
        try:
            # Импортируем модули Android (доступны только на устройстве)
            from jnius import autoclass
            
            # Получаем активность Android
            python_activity = autoclass('org.kivy.android.PythonActivity')
            activity = python_activity.mActivity
            
            # Устанавливаем принудительную горизонтальную ориентацию
            # SCREEN_ORIENTATION_SENSOR_LANDSCAPE = 6 (поворот в любую горизонтальную сторону)
            activity.setRequestedOrientation(6)
        except ImportError:
            # Если импорт не удался (например, при разработке на ПК), игнорируем
            print("Android modules not available - running on desktop")
        except Exception as e:
            # Обрабатываем любые другие ошибки
            print(f"Error setting orientation: {e}")

    def build(self):  # Этот метод создает и возвращает корневой виджет
        # Принудительно устанавливаем горизонтальную ориентацию для Android
        if platform == 'android':
            self._set_android_orientation()
        
        # Не возвращаем ничего, чтобы Kivy автоматически загрузил my.kv файл
        pass

# Запускаем наше приложение
if __name__ == '__main__':
    MyApp().run()