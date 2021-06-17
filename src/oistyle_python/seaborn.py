import json
from pathlib import Path
import sys
import urllib.request as request

with request.urlopen('https://raw.githubusercontent.com/jbosga-ams/oistyle/main/base_style.json') as response:
    data = response.read()
    base_style = json.loads(data)
colors = base_style["colors"]

base_template = {'axes.facecolor': 'white', 'axes.edgecolor': base_style['gridline_color'], 'axes.grid': False, 'axes.axisbelow': 'line', 
'axes.labelcolor': 'black', 'figure.facecolor': 'white', 'grid.color': base_style['gridline_color'], 'grid.linestyle': '-', 'text.color': 'black', 
'xtick.color': 'black', 'ytick.color': 'black', 'xtick.direction': 'out', 'ytick.direction': 'out',  'patch.edgecolor': 'black', 
'patch.force_edgecolor': False, 'image.cmap': 'viridis', 'font.family': ['sans-serif'],'font.sans-serif': [base_style['font']], 'xtick.bottom': False, 'xtick.top': False, 'ytick.left': False, 'ytick.right': False, 
'axes.spines.left': True, 'axes.spines.bottom': True, 'axes.spines.right': True, 'axes.spines.top': True}


bar_template = base_template


line_template = base_template
line_template['axes.grid'] = True