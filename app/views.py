from flask import render_template, request
from app import app
from app.forms import Form
from script_gen import generate_script

@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        occasion = request.form.get("occasion", "Break Up")
        name = form.name.data
        details = form.details.data
        rudeness = int(form.rudeness.data)

        # Generate the script
        script = generate_script(occasion, name, details, rudeness)

        return render_template('result.html', script=script, title='Result')

    return render_template('home.html', form=form, title='Home')

@app.route('/about')
def about():
    form = Form()
    return render_template('home.html', title='Home Page', form=form)