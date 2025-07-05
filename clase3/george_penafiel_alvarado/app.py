from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'un_api_key'

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'mi_aplicacion.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Asegurarse de que el directorio de la instancia exista
with app.app_context():
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

# Definición de Modelos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'

# Crear las tablas en la base de datos (se ejecuta solo si no existen)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/productos')
def productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        descripcion = request.form['descripcion'].strip()
        precio_str = request.form['precio'].strip()

        try:
            precio = float(precio_str)
        except ValueError:
            flash('El precio debe ser un número válido.', 'error')
            return redirect(url_for('crear_producto'))

        if nombre and descripcion and precio_str:
            nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio)
            db.session.add(nuevo_producto)
            db.session.commit()
            flash('Producto creado con éxito.', 'success')
            return redirect(url_for('productos'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('crear_producto'))
    return render_template('form_producto.html', accion='Crear', producto={})

@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        descripcion = request.form['descripcion'].strip()
        precio_str = request.form['precio'].strip()

        try:
            precio = float(precio_str)
        except ValueError:
            flash('El precio debe ser un número válido.', 'error')
            return redirect(url_for('editar_producto', id=producto.id))

        if nombre and descripcion and precio_str:
            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.precio = precio
            db.session.commit()
            flash('Producto editado con éxito.', 'success')
            return redirect(url_for('productos'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('editar_producto', id=producto.id))

    return render_template('form_producto.html', accion='Editar', producto=producto, indice=producto.id)

@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado con éxito.', 'success')
    return redirect(url_for('productos'))

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()

        if nombre and correo:
            nuevo_usuario = Usuario(nombre=nombre, correo=correo)
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario creado con éxito.', 'success')
            return redirect(url_for('usuarios'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('crear_usuario'))

    return render_template('form.html', accion='Crear', usuario={})

@app.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()

        if nombre and correo:
            usuario.nombre = nombre
            usuario.correo = correo
            db.session.commit()
            flash('Usuario editado con éxito.', 'success')
            return redirect(url_for('usuarios'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('editar_usuario', id=usuario.id))

    return render_template('form.html', accion='Editar', usuario=usuario, indice=usuario.id)

@app.route('/usuarios/eliminar/<int:id>')
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado con éxito.', 'success')
    return redirect(url_for('usuarios'))

if __name__ == '__main__':
    app.run(debug=True)