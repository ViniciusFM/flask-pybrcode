from flask import Flask, render_template
from pybrcode.pix import generate_simple_pix
from pybrcode.exceptions import PixInvalidKeyException, PixInvalidPayloadException

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/brcode/<value>/<key>/<name>")
def brcode_return(value, key, name):
    try:
        pix = generate_simple_pix(
            fullname=name,
            key=key,
            city='Patos de Minas', 
            value=float(value))
    except PixInvalidKeyException as e:
        return f'Error! Wrong key format {str(e)}', 400
    except PixInvalidPayloadException as e:
        return f'Error! Something went wrong with the payload {str(e)}', 400
    return pix.toSVG(), 200
