from flask import request, redirect, url_for, render_template, flash

from flaskr import app, db
from flaskr.models import Product


@app.route('/')
def show_products():
    products = Product.query.order_by(Product.id.desc()).all()
    return render_template('show_products.html', products=products)


@app.route('/add', methods=['POST'])
def add_product():
    product = Product(
            product_name=request.form['product_name'],
            )
    db.session.add(product)
    db.session.commit()
    flash('New product was successfully posted')
    return redirect(url_for('show_products'))


@app.route('/delete/<product_id>', methods=['GET'])
def delete_product(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    db.session.delete(product)
    db.session.commit()
    flash('product was successfully deleted')
    return redirect(url_for('show_products'))


@app.route('/updatesenni/<product_id>', methods=['GET'])
def senni_update(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    return render_template('show_updateproduct.html', product=product)


@app.route('/update/<product_id>', methods=['POST'])
def update_product(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    product.product_name = request.form['product_name']
    
    db.session.add(product)
    db.session.commit()
    flash('product was successfully update')
    return redirect(url_for('show_products'))
