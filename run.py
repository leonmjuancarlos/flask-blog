# Flask code
import os

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

posts = [1,1,1,1 ]


@app.route('/')
def index():
    return render_template('index.html', num_posts=len(posts))


@app.route('/p/<string:slug>/')
def show_post(slug):
    return render_template('post_view.html', slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template('admin/post_form.html', post_id=post_id)



"""
Para hacer esto, a una URL le podemos añadir 
secciones variables o parametrizadas con <param>. 
La vista recibirá <param> como un parámetro con ese 
mismo nombre. Opcionalmente se puede indicar un 
conversor (converter) para especificar el tipo de 
dicho parámetro así <converter:param>.

Por defecto, en Flask existen los siguientes 
conversores:

- string: Es el conversor por defecto. 
    Acepta cualquier cadena que no contenga el carácter ‘/’.
- int: Acepta números enteros positivos.
- float: Acepta números en punto flotante positivos.
- path: Es como string pero acepta cadenas con el carácter ‘/’.
- uuid:  Acepta cadenas con formato UUID.
"""
