# Crud Fast Api

Para ejecutar este programa primero debemos tener python una versión igual o superior a la 3.8 e instalado posgreSQL

## Instalación
Para la instalación lo primero será crear un entorno virtual usando el siguiente comando:
```
python -m venv env
```
El siguiente paso es instalar las librerías necesarias para que el proyecto funcione, usa: 
```
pip install -r requirements.txt
```

## Configuración  conexión a database
Luego pasaremos a configurar un archivos que encontraremos en la carpeta ```config```, modificaremos el archivo ```database.py```, ahí estableceremos los valores para la conexión a la base de datos:

```
usernamedb = 'username'
passworddb = 'password'
hostdb = 'localhost'
port = 5432
database = 'postgres'
```

## Árbol de carpetas
```
#       
+---config
|       database.py  
|                   
+---models
|       events.py
|           
+---routes
|       events.py
|           
+---schemas
|       events.py
|
|   .gitignore
|   main.py
|   requirements.txt
```
