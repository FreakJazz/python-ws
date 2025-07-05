from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.product import Product
from app.extensions import db
from datetime import datetime

bp = Blueprint('products', __name__, url_prefix='/productos')

@bp.route('/')
def listar():
    productos = Product.query.order_by(Product.fecha_creacion.desc()).all()
    return render_template('products/listar.html', productos=productos)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        try:
            producto = Product(
                nombre=request.form['nombre'],
                descripcion=request.form['descripcion'],
                precio=float(request.form['precio']),
                stock=int(request.form['stock']),
                categoria=request.form['categoria']
            )
            db.session.add(producto)
            db.session.commit()
            flash('Producto creado exitosamente', 'success')
            return redirect(url_for('products.listar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear producto: {str(e)}', 'danger')
    
    return render_template('products/crear.html')

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    producto = Product.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            producto.nombre = request.form['nombre']
            producto.descripcion = request.form['descripcion']
            producto.precio = float(request.form['precio'])
            producto.stock = int(request.form['stock'])
            producto.categoria = request.form['categoria']
            
            db.session.commit()
            flash('Producto actualizado exitosamente', 'success')
            return redirect(url_for('products.listar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar producto: {str(e)}', 'danger')
    
    return render_template('products/editar.html', producto=producto)

@bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    producto = Product.query.get_or_404(id)
    try:
        db.session.delete(producto)
        db.session.commit()
        flash('Producto eliminado exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar producto: {str(e)}', 'danger')
    
    return redirect(url_for('products.listar'))