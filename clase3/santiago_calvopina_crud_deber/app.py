from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura_123'  # Cambia esta clave por una secreta

productos = []
contador_id = 1


@app.route('/')
def home():
    return redirect(url_for('mostrar_productos'))


@app.route('/productos')
def mostrar_productos():
    return render_template('mostrar_productos.html', productos=productos)


@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    global contador_id
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            flash('Precio o cantidad inválidos.')
            return redirect(url_for('crear_producto'))

        productos.append({
            'id': contador_id,
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        })
        contador_id += 1
        flash(f'Producto "{nombre}" creado correctamente.')
        return redirect(url_for('mostrar_productos'))

    return render_template('crear_producto.html')


@app.route('/productos/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if not producto:
        flash('Producto no encontrado.')
        return redirect(url_for('mostrar_productos'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            flash('Precio o cantidad inválidos.')
            return redirect(url_for('actualizar_producto', id=id))

        producto['nombre'] = nombre
        producto['precio'] = precio
        producto['cantidad'] = cantidad

        flash(f'Producto "{nombre}" actualizado correctamente.')
        return redirect(url_for('mostrar_productos'))

    return render_template('actualizar_producto.html', producto=producto)


@app.route('/productos/borrar/<int:id>', methods=['POST'])
def borrar_producto(id):
    global productos
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        productos = [p for p in productos if p['id'] != id]
        flash(f'Producto "{producto["nombre"]}" eliminado correctamente.')
    else:
        flash('Producto no encontrado.')
    return redirect(url_for('mostrar_productos'))


if __name__ == '__main__':
    app.run(debug=True)
