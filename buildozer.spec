[app]

# (str) Nombre de la aplicación
title = Kivy Launcher

# (str) Nombre del paquete
package.name = kivylauncher

# (str) Nombre del directorio que contiene los archivos .py
source.include_exts = py,png,jpg,kv,atlas

source.dir = .  # <-- Esta línea es la que falta

# (list) Dependencias de la aplicación
# Aquí se incluyen las dependencias necesarias (por ejemplo, kivy y permisos)
requirements = kivy, runpy, android

# (str) Versión de la aplicación
version = 0.1

# (str) Nombre del archivo .apk
package.domain = org.kivylauncher

# (int) Versión mínima de Android
android.minapi = 21  # Puedes ajustarlo según el dispositivo mínimo que quieras soportar

# (bool) Si la app usa orientación vertical o apaisada
orientation = portrait

# (list) Permisos de la aplicación
# Especificamos que queremos acceso al almacenamiento
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (bool) Habilitar las características de OpenGL
fullscreen = 1

[buildozer]

# (str) Ruta a los archivos adicionales para empaquetar
# Aquí puedes especificar las rutas a los archivos adicionales, como imágenes o otros recursos
# (Ejemplo: /path/to/your/project/assets)
