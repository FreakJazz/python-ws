# -*- coding: utf-8 -*-
"""

Tarea Clase 3

@author: Lourdes Farinango
"""

from flask import Flask, render_template, request, redirect, url_for, flash

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesaria para los mensajes flash

# --- Almacenamiento en memoria (simula una base de datos) ---
# Lista de diccionarios para guardar los productos.
# Cada producto tiene un 'id' único para poder identificarlo.
productos = [
    {'id': 1, 'nombre': 'Laptop UltraFina', 'precio': 1200.50, 'cantidad': 15},
    {'id': 2, 'nombre': 'Mouse Inalámbrico', 'precio': 25.00, 'cantidad': 80},
    {'id': 3, 'nombre': 'Teclado Mecánico RGB', 'precio': 150.75, 'cantidad': 30}
]
# Contador para generar IDs únicos para nuevos productos
next_id = 4

# --- Rutas de la Aplicación ---

@app.route('/')
def index():
    """Redirige a la página principal de productos."""
    return redirect(url_for('mostrar_productos'))

@app.route('/productos')
def mostrar_productos():
    """
    Ruta para mostrar todos los productos. (Read)
    Renderiza una plantilla que itera sobre la lista de productos.
    """
    return render_template('productos.html', productos=productos)

@app.route('/productos/nuevo', methods=['GET', 'POST'])
def crear_producto():
    """
    Ruta para crear un nuevo producto. (Create)
    Si el método es GET, muestra el formulario.
    Si es POST, procesa los datos y añade el nuevo producto a la lista.
    """
    global next_id
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])

        # Crear el nuevo producto
        nuevo_producto = {
            'id': next_id,
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }

        # Añadir a la lista y actualizar el contador de ID
        productos.append(nuevo_producto)
        next_id += 1
        
        flash(f'Producto "{nombre}" creado exitosamente.', 'success')
        return redirect(url_for('mostrar_productos'))
    
    # Si es GET, simplemente mostrar el formulario
    return render_template('formulario_producto.html')

@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    """
    Ruta para editar un producto existente. (Update)
    Busca el producto por su ID.
    Si es GET, muestra el formulario con los datos actuales.
    Si es POST, actualiza los datos del producto en la lista.
    """
    # Buscar el producto en la lista por su id
    producto = next((p for p in productos if p['id'] == id), None)

    if not producto:
        flash('Producto no encontrado.', 'error')
        return redirect(url_for('mostrar_productos'))

    if request.method == 'POST':
        # Actualizar los datos del producto
        producto['nombre'] = request.form['nombre']
        producto['precio'] = float(request.form['precio'])
        producto['cantidad'] = int(request.form['cantidad'])
        
        flash(f'Producto "{producto["nombre"]}" actualizado exitosamente.', 'success')
        return redirect(url_for('mostrar_productos'))

    # Si es GET, mostrar el formulario con los datos del producto
    return render_template('formulario_editar_producto.html', producto=producto)

@app.route('/productos/eliminar/<int:id>', methods=['POST'])
def eliminar_producto(id):
    """
    Ruta para eliminar un producto. (Delete)
    Esta ruta solo acepta POST para mayor seguridad.
    """
    global productos
    # Filtrar la lista para excluir el producto con el id a eliminar
    producto_a_eliminar = next((p for p in productos if p['id'] == id), None)
    
    if producto_a_eliminar:
        productos = [p for p in productos if p['id'] != id]
        flash(f'Producto "{producto_a_eliminar["nombre"]}" eliminado exitosamente.', 'success')
    else:
        flash('Producto no encontrado.', 'error')
        
    return redirect(url_for('mostrar_productos'))

if __name__ == '__main__':
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)