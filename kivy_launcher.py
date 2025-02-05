import os
import runpy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class KivyLauncherApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Select a Python File")
        self.layout.add_widget(self.label)

        self.file_chooser = FileChooserListView(path="/sdcard/")
        self.layout.add_widget(self.file_chooser)

        self.run_button = Button(text="Run Script")
        self.run_button.bind(on_press=self.run_script)
        self.layout.add_widget(self.run_button)

        return self.layout

    def run_script(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            script_path = selected_file[0]

            try:
                # Obtener la carpeta donde está el script
                script_dir = os.path.dirname(script_path)
                
                # Cambiar al directorio del script para que pueda importar sus módulos
                os.chdir(script_dir)

                # Eliminar todos los widgets de la pantalla
                self.layout.clear_widgets()

                # Ejecutar el script como un módulo
                runpy.run_path(script_path, run_name="__main__")

            except Exception as e:
                self.layout.add_widget(Label(text=f"Error: {e}"))

if __name__ == "__main__":
    KivyLauncherApp().run()
