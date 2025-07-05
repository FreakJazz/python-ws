# 🚀 CRUD de Productos y Usuarios con Flask y SQLite

## 📌 Tabla de Contenidos
- [Requisitos](#-requisitos)
- [Configuración](#-configuración)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Funcionalidades](#-funcionalidades)
- [Modelos de Datos](#-modelos-de-datos)
- [Ejecución](#-ejecución)
- [Migraciones](#-migraciones)

## 📋 Requisitos

### Prerrequisitos
- Python 3.8+
- Pip (Gestor de paquetes de Python)

### Dependencias

```bash
pip install flask flask-sqlalchemy flask-migrate
```

# Linux/Mac
export FLASK_APP=run.py
export FLASK_ENV=development

# Windows
set FLASK_APP=run.py
set FLASK_ENV=development

## 📁 Estructura del Proyecto

```bash
flask_crud_usuarios/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── user.py
│   │   └── product.py
│   ├── routes/
│   │   ├── users.py
│   │   └── products.py
│   └── templates/
│       ├── products/
│       │   ├── listar.html
│       │   ├── crear.html
│       │   └── editar.html
│       └── base.html
├── migrations/
├── config.py
└── run.py

```
## 🛠️ Funcionalidades

Productos
Endpoint	              Método	  Descripción
/productos	               GET	      Listar productos
/productos/crear	       GET/POST	  Crear producto
/productos/editar/<id>	   GET/POST	  Editar producto
/productos/eliminar/<id>   POST	      Eliminar producto
Usuarios
Endpoint	               Método	  Descripción
/usuarios	                GET	      Listar usuarios
/usuarios/crear	GET/POST	Crear     usuario
/usuarios/editar/<id>	    GET/POST  Editar usuario

## 🚀 Ejecución

```bash
flask run
```

## 🔄 Migraciones

```bash
flask db init
flask db migrate -m "Descripción de cambios"
flask db upgrade
```
