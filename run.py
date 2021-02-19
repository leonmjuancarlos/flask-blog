# Flask code
import sys
from forms import PostForm, RegistrationForm
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

POSTS = [
    {
        'title': "Titulo H1",
        'slug': 'test1',
        'content': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    },
    {
        'title': "Titulo H1",
        'slug': 'test2',
        'content': 'jsadfljljlsadjldfjdsaj sadfjsadjjfls jasdlfjlasjdjf jsadlkfjlskdajlk ljsadlkjfñlas'
    }
]

app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'


@app.route('/')
def index():
    data = {
        'num_posts': len(POSTS)
    }
    return render_template('index.html', **data)


@app.route('/p/<string:slug>/')
def show_post(slug):
    data = {
        'slug_title': slug
    }

    # Verify that url slug correspond to a existing post
    for dicc in POSTS:
        for k, v in dicc.items():
            if v == slug:
                return render_template('post_view.html', **dicc)

    return redirect(url_for("index"))


@app.route("/admin/post/", methods=["POST", "GET"])
# @app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    data = {
        'post_id': post_id
    }
    """ if post_id == None:
        data['post_id'] = 'más reciente' """
    form = PostForm()
    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        slug = form.slug.data
        content = form.content.data
        data['title'] = title
        data['slug'] = slug
        data['content'] = content

        return redirect(url_for('index'))

    return render_template('admin/post_form.html', form=form, **data)


@app.route("/signup/", methods=["POST", "GET"])
def show_signup_form():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        next = request.args.get("next", None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=form)






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
