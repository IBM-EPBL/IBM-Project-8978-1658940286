from dataclasses import dataclass
from fileinput import filename
from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from keras import models
import warnings
import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt


warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
matplotlib.rcParams['axes.labelsize']=14
matplotlib.rcParams['xtick.labelsize']=12
matplotlib.rcParams['ytick.labelsize']=12
matplotlib.rcParams['text.color']='k'
import pickle
import os 
from PIL import Image
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
UPLOAD_PATH="get image"
UPLOAD_DIRECTORY=os.path.join(APP_ROOT,UPLOAD_PATH)
app.config['UPLOAD_DIRECTORY']=UPLOAD_DIRECTORY

#upload dataset
@app.route('/upload_file',methods=['POST'])
def upload_file(): 
        img = Image.open(request.files['file'].stream).convert("L")
        img = img.resize((28,28))
        img2arr = np.array(img)
        img2arr = img2arr.reshape(1,28,28,1)
        model = models.load_model('final_model.h5')
        #y_pred = model.predict_classes(img2arr)
        y_pred = np.argmax(model.predict(img2arr), axis=1)
        print(y_pred)
        if(y_pred == 0):
            return render_template("0.html",shoechase = str(y_pred))
        elif(y_pred == 1):
            return render_template("1.html",shoechase = str(y_pred))
        elif(y_pred == 2):
            return render_template("2.html",shoechase = str(y_pred))
        elif(y_pred == 3):
            return render_template("3.html",shoechase = str(y_pred))
        elif(y_pred == 4):
            return render_template("4.html",shoechase = str(y_pred))
        elif(y_pred == 5):
            return render_template("5.html",shoechase = str(y_pred))
        elif(y_pred == 6):
            return render_template("6.html",shoechase = str(y_pred))
        elif(y_pred == 7):
            return render_template("7.html",shoechase = str(y_pred))
        elif(y_pred == 8):
            return render_template("8.html",shoechase = str(y_pred))
        else:
            return render_template("9.html",shoechase = str(y_pred))
@app.route('/')
def home():
    return render_template("home.html")

    
if __name__=='__main__':
    app.run(debug=True)