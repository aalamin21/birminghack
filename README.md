# birminghack

## That's Awkward app


### Initialise environment

```
pip install -r requirements.txt
```

Create a `.env` file in the base directory and add:
```
GEMINI_API_KEY=<YOUR GEMINI API KEY>
NEUPHONIC_API_KEY=<YOUR NEUPHONIC API KEY>
```
Create a `.flaskenv` file in the base directory and add:
```
FLASK_APP = run.py
FLASK_ENV = development
FLASK_DEBUG = 1
FLASK_KEY = <SOME RANDOMLY GENERATED KEY>
```

### Run flask

```
flask run
```

### Fill Form
> Occasion: Occasion of awkward interaction
> Name: Name of who the message is directed to
> Details: Extra details about the message or the situation
> Rudeness: 1-10 How harsh does the message need to be
> Language: Output Language
> 
> Output: Message Script and a voice generated audio with an option to download .wav file