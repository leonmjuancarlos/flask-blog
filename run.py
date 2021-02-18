# Flask code

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

posts = [1,1,1,1 ]


@app.route('/')
def index():
    data = {
        'num_posts': len(posts)
    }
    return render_template('index.html', **data)


@app.route('/p/<string:slug>/')
def show_post(slug):
    data = {
        'slug_title': slug
    }
    return render_template('post_view.html', **data)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    data = {
        'post_id': post_id
    }
    if post_id == None:
        data['post_id'] = 'más reciente'
    return render_template('admin/post_form.html', **data)


@app.route("/signup/", methods=["POST", "GET"])
def show_signup_form():
    if request.method == "POST":
        name = request.form['Username']
        email = request.form['Email']
        password = request.form['Password']

        next = request.args.get("next", None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html")


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
