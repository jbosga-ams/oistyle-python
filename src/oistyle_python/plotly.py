import json
from pathlib import Path
import sys
import plotly.graph_objects as go
import urllib.request as request

with request.urlopen('https://raw.githubusercontent.com/jbosga-ams/oistyle/main/base_style.json') as response:
    data = response.read()
    base_style = json.loads(data)

colors = base_style["colors"]
    

base_template = go.layout.Template(    
    layout=dict(
        font=dict(family=base_style["font"], size=base_style["font_size"]),
        plot_bgcolor=base_style["plot_bgcolor"], 
        xaxis=dict(zerolinecolor=base_style["gridline_color"], gridcolor=base_style["gridline_color"], gridwidth=base_style["gridline_width"], 
                    showline=True, linewidth=base_style["gridline_width"], linecolor=base_style["gridline_color"], mirror=True, showgrid=False),
        yaxis=dict(zerolinecolor=base_style["gridline_color"], gridcolor=base_style["gridline_color"], gridwidth=base_style["gridline_width"], 
                    showline=True, linewidth=base_style["gridline_width"], linecolor=base_style["gridline_color"], mirror=True, showgrid=False),
        colorway=colors['darkblue_lightblue_gradient_5'],
    )
)


bar_chart_template = base_template

line_chart_template = base_template
line_chart_template.layout.yaxis.showgrid=True