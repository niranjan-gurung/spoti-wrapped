from functools import reduce
from operator import add

import pandas as pd
import numpy as np

class ProcessFiles:
  def __init__(self, files=None):
    self.df = pd.DataFrame()
    for file in files:
      single_file_data = pd.read_json(file)
      self.df = pd.concat([self.df, single_file_data], axis=0)
      self.ms_played: pd.Series = self.df.msPlayed

  def get_total_mins_played(self) -> int:
    # total ms played in mins:
    self.total_ms = reduce(add, self.ms_played)
    return int(self.total_ms / 60000)
  
  def get_top_artists(self):
    return self.df.groupby('artistName')\
            .agg({'msPlayed': np.sum})\
            .sort_values(by=['msPlayed'], ascending=True)