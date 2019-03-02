from flask import Flask
from flask_cors import CORS

from flask import request
from pybeep.pybeep import PyVibrate, PyBeep


import os
import subprocess

app = Flask(__name__)
CORS(app)

os.chdir('/home/wint3rmute')

@app.route('/')
def hello():
    return 'Hello, World!'



@app.route('/command', methods=['POST'])
def parse_request():
    data = request.get_data().decode('utf-8')
    print('####' + data)

    if 'rm ' in data:
        PyBeep().beep()
        return 'Nie no bez takich xD'

    if 'cd' in data:
        return 'sorry, cd nie dziala bo mi sie nie chcialo emulowac calego shella xD jak jestes dobry to poradzisz sobie bez niego ;*'

    try:
        stream = subprocess.Popen(
            data.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True)
        output = stream.communicate(timeout=5)

        if stream.returncode == 0:
            PyVibrate().beep()

        return output[0].decode('utf-8') + output[1].decode('utf-8')

    except Exception as e: return(str(e))

    return 'wtf'
app.run(debug=False)
