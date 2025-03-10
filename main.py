from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def file_upload():
  f = request.files.getlist('file')   # reads multiple file uploads - returns list
  l = []
  for item in f:
    l.append(item.filename)
  
  return redirect(url_for('stats', fileList=l))

@app.route('/stats/<fileList>')
def stats(fileList):
  return render_template('test.html', files=fileList)
