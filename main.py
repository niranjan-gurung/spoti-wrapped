from flask import (
  Flask, 
  render_template, 
  request
)

from process_files import ProcessFiles
from plot_generator import PlotGen

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    files = request.files.getlist('file')
    
    pf = ProcessFiles(files)
    pg = PlotGen()

    return render_template('wrapped.html', 
                            tables=[pf.df.to_html(classes='data')],
                            img=pg.get_example_plot(),
                            total_mins=pf.get_total_mins_played())
  
  return render_template('index.html')
