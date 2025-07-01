from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'un_api_key'

base_de_datos_usuarios = []
base_de_datos_productos = []

def imprimir_usuarios():
    print("\n--- LISTA ACTUAL DE USUARIOS ---")
    print("-------------------------------\n")

def imprimir_productos():
    print("\n--- LISTA ACTUAL DE PRODUCTOS ---")
    print("-------------------------------\n")
    for i, producto in enumerate(base_de_datos_productos):
        print(f"Producto #{i+1}: Nombre: {producto['nombre']}, Descripción: {producto['descripcion']}, Precio: {producto['precio']}")
    print("-------------------------------\n")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/productos')
def productos():
    imprimir_productos()
    return render_template('productos.html', productos=base_de_datos_productos)

@app.route('/usuarios')
def usuarios():
    imprimir_usuarios()
    return render_template('usuarios.html', usuarios=base_de_datos_usuarios)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()

        if nombre and correo:
            base_de_datos_usuarios.append({'nombre': nombre, 'correo': correo})
            flash('Usuario creado con éxito.', 'success')
            imprimir_usuarios()
            return redirect(url_for('usuarios'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('crear_usuario'))

    return render_template('form.html', accion='Crear', usuario={})

@app.route('/usuarios/editar/<int:indice>', methods=['GET', 'POST'])
def editar_usuario(indice):
    if indice >= len(base_de_datos_usuarios):
        flash('Índice de usuario inválido.', 'error')
        return redirect(url_for('usuarios'))

    usuario = base_de_datos_usuarios[indice]

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()

        if nombre and correo:
            print(f"\nEditando usuario #{indice + 1}:")
            print(f"Antes: Nombre: {usuario['nombre']}, Correo: {usuario['correo']}")
            usuario['nombre'] = nombre
            usuario['correo'] = correo
            print(f"Después: Nombre: {nombre}, Correo: {correo}")
            imprimir_usuarios()
            flash('Usuario editado con éxito.', 'success')
            return redirect(url_for('usuarios'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('editar_usuario', indice=indice))

    return render_template('form.html', accion='Editar', usuario=usuario, indice=indice)

@app.route('/usuarios/eliminar/<int:indice>')
def eliminar_usuario(indice):
    if 0 <= indice < len(base_de_datos_usuarios):
        usuario_eliminado = base_de_datos_usuarios[indice]
        print(f"\nEliminando usuario #{indice + 1}:\nUsuario eliminado: Nombre: {usuario_eliminado['nombre']}, Correo: {usuario_eliminado['correo']}")
        base_de_datos_usuarios.pop(indice)
        imprimir_usuarios()
        flash('Usuario eliminado con éxito.', 'success')
    else:
        flash('Índice inválido.', 'error')
    return redirect(url_for('usuarios'))

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
            base_de_datos_productos.append({'nombre': nombre, 'descripcion': descripcion, 'precio': precio})
            flash('Producto creado con éxito.', 'success')
            imprimir_productos()
            return redirect(url_for('productos'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('crear_producto'))
    return render_template('form_producto.html', accion='Crear', producto={})

@app.route('/productos/editar/<int:indice>', methods=['GET', 'POST'])
def editar_producto(indice):
    if indice >= len(base_de_datos_productos):
        flash('Índice de producto inválido.', 'error')
        return redirect(url_for('productos'))

    producto = base_de_datos_productos[indice]

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        descripcion = request.form['descripcion'].strip()
        precio_str = request.form['precio'].strip()

        try:
            precio = float(precio_str)
        except ValueError:
            flash('El precio debe ser un número válido.', 'error')
            return redirect(url_for('editar_producto', indice=indice))

        if nombre and descripcion and precio_str:
            print(f"\nEditando producto #{indice + 1}:")
            print(f"Antes: Nombre: {producto['nombre']}, Descripción: {producto['descripcion']}, Precio: {producto['precio']}")
            producto['nombre'] = nombre
            producto['descripcion'] = descripcion
            producto['precio'] = precio
            print(f"Después: Nombre: {nombre}, Descripción: {descripcion}, Precio: {precio}")
            imprimir_productos()
            flash('Producto editado con éxito.', 'success')
            return redirect(url_for('productos'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('editar_producto', indice=indice))

    return render_template('form_producto.html', accion='Editar', producto=producto, indice=indice)

if __name__ == '__main__':
    import warnings
    warnings.filterwarnings("ignore", message="This is a development server.")
    app.run(debug=True)