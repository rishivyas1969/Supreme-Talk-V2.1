from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os.path

from speechToText import convert
from upload_drive import upload, authoriseDrive

app = Flask(__name__)

@app.route('/')
def home():
    authoriseDrive()
    if os.path.exists('token.json'):
        msg = "Authorized Well."
    else:
        msg = "Not Authorized!"
    data = {
        "name": "Supreme Talk",
        "version": 1.2,
        "message": msg
    }
    return jsonify(data)

@app.route('/audiototext', methods=['GET', 'POST'])
def audio_to_text():

    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename('uploaded'+file.filename))

        return {"text": convert('uploaded'+file.filename),
        "message": "converted"}
    else:
        return {"text": "None",
            "message": "POST an audio file."}

@app.route('/savefiletodrive', methods=['GET', 'POST'])
def saveToDrive():

    if request.method == 'POST':

        #flag  is a bool
        flag = request.form['flag']

        if flag:
            upload()

if __name__ == '__main__':
    app.debug=True
    app.run()