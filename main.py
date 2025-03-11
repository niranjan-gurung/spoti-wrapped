from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from matplotlib.figure import Figure
from io import BytesIO
import base64
import json

# from contextlib import ExitStack

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
  #   """TODO: open multiple files

  #     files = request.files.getlist('file')
  #     fnames = []
  #     for name in files:
  #       name.save(name.filename)
  #       fnames.append(name.filename)
  #     with ExitStack() as stack:
  #       files = [
  #         stack.enter_context(open(fname)) for fname in fnames
  #       ]
  #       print(files)
  #       return render_template('test.html', data=files[0].buffer.read())
  #   """

    file = request.files['file']

    if file:
      file.save(file.filename)
      with open(file.filename, encoding='utf8') as f:
        d = json.load(f)    # serialize file object -> json

        """
        plot data points on graph, will be loaded as img.
        plot demo line for now.
        """
        fig = Figure()
        ax = fig.subplots()
        ax.plot([1, 2])
        
        buf = BytesIO() # Save it to a temporary buffer.
        fig.savefig(buf, format="png")
        
        d = base64.b64encode(buf.getbuffer()).decode("ascii") # Embed the result in the html output.
        return render_template('test.html', data=d)

  return render_template('index.html')
