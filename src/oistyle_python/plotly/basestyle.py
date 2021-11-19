import requests
from requests import ConnectionError
import plotly.graph_objects as go
import json

class BaseStyle:
    style_url = "https://raw.githubusercontent.com/jbosga-ams/oistyle/main/base_style.json"
    
    def __init__(self) -> None:
        self.grab_styling()
        
    def grab_styling(self, style_path: str = None) -> None:
        if not style_path:
            try:
                res = requests.get(self.style_url).json()
            except ConnectionError:
                raise Exception("Failed grabbing json with style-info, try supplying style_path")
        else:
            res = json.loads(style_path)

        for k, v in res.items():
            setattr(self, k, v)
    
    def _get_axis_format(self) -> dict:
        self.gridline_color = "#dbdbdb" # Jorren vragen om deze aan te passen
        
        return {
            "zerolinecolor": self.gridline_color,
            "gridcolor": self.gridline_color,
            "gridwidth": self.gridline_width,
            "showline": True,
            "linewidth": self.gridline_width,
            "linecolor": self.gridline_color,
#             "mirror": True,
            "showgrid": False,
        }
    
    def _get_base_template_layout(self) -> go.layout.Template:
        return go.layout.Template(           
            layout={
                "font": {"family": self.font, "size": self.font_size},
                "plot_bgcolor": self.plot_bgcolor,
                "colorway": self.colors['darkblue_lightblue_gradient_5'],
                "separators": "," # Jorren vragen om deze toe te voegen
                }
            )
    
    def get_base_template(
        self, 
        graph_type: str = None, 
        orientation: str = None, 
        colors: str = None
        ) -> go.layout.Template:
        """[summary]

        Args:
            graph_type (str, optional): Pick 'bar', 'line' or 'bar'. Defaults to None.
            orientation (str, optional): [description]. Pick horizontal ('h') or vertical 'v'. Defaults to None.
            colors (str, optional): Set basecolors. Defaults to None.

        Raises:
            ValueError: [description]

        Returns:
            [type]: [description]
        """        
        base_template = self._get_base_template_layout()              
        axis_format = self._get_axis_format()
        
        if graph_type == "bar":       
            if orientation in ["v", "vertical"]:
                base_template.layout.xaxis.update(axis_format)
                base_template.layout.yaxis.update(zeroline = False)
            elif orientation in ["h", "horizontal"]:
                base_template.layout.yaxis.update(axis_format)
                base_template.layout.xaxis.update(zeroline = False)
            else:
                raise ValueError("Orientation ('v'/'vertical' or 'h'/'horizontal') should be supplied with graph_type=='bar'")
                
        elif graph_type == "line":
            base_template.layout.xaxis.update(axis_format)
            base_template.layout.yaxis.update({"showgrid": True})   

        if colors:
            base_template.layout.update({"colorway": colors})
                
        return base_template

    def get_ois_colors(self, colorscale):
        colorscale = self.colors.get(colorscale, [])
        if not colorscale:
            raise Exception(f"Kies uit {self.colors.keys()}")

        return colorscale