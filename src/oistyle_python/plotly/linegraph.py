import plotly.express as px
from basestyle import BaseStyle

class Line:
    basestyle = BaseStyle()

    @classmethod
    def line(
        cls,
        data,
        x,
        y,
        color: None,
        width = 750,
        height = 490,
        **kwargs
        ):

        fig = px.line(
            data_frame=data, 
            x=x,
            y=y,
            color=color,
            width=width, 
            height=height, 
            template = BaseStyle().get_base_template(),
            **kwargs
            )
        
        return fig