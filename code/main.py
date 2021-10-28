from flask import Flask, request, jsonify
import os.path

from save_text import take_text, declare_list
from upload_drive import upload, authoriseDrive

app = Flask(__name__)

@app.route('/home')
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
    declare_list()
    return jsonify(data)

@app.route('/taketext', methods=['GET', 'POST'])
def audio_to_text():

    if request.method == 'POST':
        text = request.form['text']

        return {"message": take_text(text)}
    else:
        return {"message": "POST an audio file."}

@app.route('/savefiletodrive', methods=['GET', 'POST'])
def saveToDrive():

    if request.method == 'POST':

        #flag  is a bool
        flag = request.form['flag']

        if flag:
            str = upload()
            return {"message": str}

        else: 
            return {"message": "Flag False."}

    return {"message": "Please POST with flag: True to upload created text file."}

if __name__ == '__main__':
    app.debug=True
    app.run()