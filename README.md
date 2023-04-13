# Configuración del proyecto

Una vez clonado el repositorio del proyecto, lo abrimos con vs code y con la terminal integrada del editor escribimos el siguiente comando:

```
python3 -m venv env
```

Esto sera para crear un entorno virtual y así todos nuestros paquetes queden instalados en nuestro entorno y no en nuestra maquina.
Una vez hecho este paso accedemos a nuestro entorno virtual con el siguiente comando:

```
Linux & MacOs
source env/bin/actuvate
Windows
.\env\Scripts\activate
```

# Nota

Si queremos salir de nuestra forma la forma correcta es escribir en la terminar este comando.

```
deactivate
```

Luego de haber accedido a nuestro entorno debemos realizar la instalación de los paquetes requeridos los cuales estan en el archivo requirements.txt esto es para la correcta ejecución del código:

```
pip install requirements.txt
```

Ya por ultimo para su ejecución es una ejecución normal como cualquier proyecto hecho en python.
