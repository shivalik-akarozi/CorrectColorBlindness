from flask import Flask, render_template, request
import cv2
import numpy as np
import cv2

from recolor import Core








app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/after', methods=['GET', 'POST'])
def after():

    global model, resnet, vocab, inv_vocab

    img = request.files['file1']

    img.save('static/file.jpg')



    
    image = cv2.imread('static/file.jpg')
    

    image = cv2.resize(image, (900,450))
    
    
    Core.correct(input_path='static/file.jpg',
                 return_type='save',
                 save_path='static/file1.jpg',
                 protanopia_degree=0.9,
                 deutranopia_degree=0.0)

    return render_template('after.html', data="hello")

if __name__ == "__main__":
    app.run(debug=True)

