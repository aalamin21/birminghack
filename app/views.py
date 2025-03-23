import os

from flask import render_template, request, send_from_directory, flash
from app import app
from app.forms import Form, DownloadForm
from script_gen import generate_script
from neuphonic import generate_audio
import hashlib

# For use in frontond
audio_file = None
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

        audio_file = generate_audio(script)
        audio_file_path = os.path.join('static', 'audio', audio_file)


        return render_template('result.html', script=script, title='Result', audio_file_path=audio_file_path)

    elif form.is_submitted():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, 'danger')  # or 'warning' for yellow

    return render_template('home.html', form=form, title='Home')

@app.route('/about')
def about():
    form = Form()
    return render_template('home.html', title='Home Page', form=form)

@app.route('/audio_testing')
def audio_testing():


    test_script='''Hey Brandon, remember that time you said you’d learn React? Good times, good times. It’s kind of like
     that legendary lost city of Atlantis – everyone talks about it, no one’s ever actually seen it. Look, I’m breaking 
     up with you… professionally. We’re stuck in this endless loop of me handing you perfectly sculpted backend APIs and 
     you handing me back… nothing. It’s like dating a mime trapped in a CSS box model – all style, no substance. I need 
     someone who can actually wrestle with divs, not just admire them from afar. My therapist says I need to set boundaries 
     and embrace self-care, and apparently self-care involves not pulling my hair out strand by strand waiting for a button 
     to magically appear on the page. So, yeah, this is me setting a boundary. A big, flashing neon, "Get thee to a JavaScript 
     tutorial" kind of boundary. I wish you the best… in finding a project that doesn't require a front-end. Maybe try backend 
     for ants? I hear they're pretty low-maintenance.'''


    audio_file = generate_audio(test_script)
    audio_file_path = os.path.join('static','audio', audio_file)
    return render_template('result'
    '.html', title='Audio Generator', audio_file_path=audio_file_path)

@app.route('/audio/<path:audio_file_path>', methods=['GET', 'POST'])
def download_file(audio_file_path):
    form = DownloadForm()
    if form.validate_on_submit():
        head_tail = os.path.split(audio_file_path)
        # file_name = head_tail[1] # Downloaded audio file name
        # file_dir = os.path.join('static', 'audio')
        print(audio_file_path)
        return send_from_directory(head_tail[0], head_tail[1], as_attachment=True, download_name='audio.wav')
    return render_template('download.html', title='Download', form=form, audio_file_path=audio_file_path)

