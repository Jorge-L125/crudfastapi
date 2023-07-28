# Crud Fast Api

![version](https://img.shields.io/badge/version-1.0.0-blue)   ![version](https://img.shields.io/badge/python->=3.8-green)

Este proyecto es una API desarrollada en Python utilizando el framework FastAPI y SQLAlchemy para interactuar con una base de datos PostgreSQL. La API permite realizar las operaciones de un CRUD, y unas funciones adicionales.

## Requisitos
- Python >= 3.8
- PostgreSQL
- Bibliotecas Python requeridas (ver archivo requirements.txt)

## Instalación
Una vez tenemos instalado python lo primero será crear un entorno virtual usando el siguiente comando:
```
python -m venv env
```
El siguiente paso es instalar las librerías necesarias para que el proyecto funcione, usa: 
```
pip install -r requirements.txt
```

## Configuración  conexión a database
Luego pasaremos a configurar un archivos que encontraremos en la carpeta ```config```, modificaremos el archivo ```database.py```, ahí estableceremos los detalles de la base de datos PostgreSQL:

```
usernamedb = 'username'
passworddb = 'password'
hostdb = 'localhost'
port = 5432
database = 'postgres'
```

## Uso
Para poder interactuar con la API en el shell ejecutamos el archivo ```main.py``` 
```
python main.py
``` 

La API estará disponible en ***http://localhost:5000***. Puedes acceder a la documentación interactiva de Swagger en ***http://localhost:5000/docs***

## Estructura del Proyecto
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
