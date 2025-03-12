from matplotlib.figure import Figure
from io import BytesIO
import base64

class PlotGen:
  def __init__(self):
    """plot example data points on graph, will be loaded as img"""
    self.fig = Figure()
    self.ax = self.fig.subplots()
    self.ax.plot([1, 2])
    self.buf = BytesIO()
    self.fig.savefig(self.buf, format="png")
    self.graph = base64.b64encode(self.buf.getbuffer()).decode("ascii")
  
  def get_example_plot(self) -> str:
    return self.graph