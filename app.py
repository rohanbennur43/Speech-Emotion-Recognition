from flask import Flask, render_template, request, redirect, url_for

from tensorflow import keras
import librosa
import numpy as np

#from werkzeug import secure_filename
app = Flask(__name__)

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('upload_file'))
    return render_template('login.html', error=error)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      f.save("static/abc.wav")
      #return 'file uploaded successfully'

      model=keras.models.load_model("capstone_cnn.h5")
      audio_file="static/abc.wav"

      def extract_mfcc(file_name):
        scale,sr=librosa.load(file_name)
        S=librosa.feature.mfcc(scale)
        S=np.resize(S,new_shape=(20,500))
        S=np.array(S)
        return S

      mfcc_data=[]
      mfcc_data.append(extract_mfcc(audio_file))

      expressions = ["The clip belonged to a 4","The clip belonged to a 6","The clip belonged to a wicket"]
      a = expressions[np.argmax(model.predict(np.expand_dims(mfcc_data, -1)))]
      return render_template('result.html',result=a)

if __name__ == '__main__':
   app.run(debug = True)
