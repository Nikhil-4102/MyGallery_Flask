from flask import Flask, render_template
import os
app=Flask(__name__)

img_dir=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=img_dir



@app.route('/')
def gallery():  
    img_list=os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html',img_list=img_list)


if __name__=='__main__':
    app.run(debug=True)