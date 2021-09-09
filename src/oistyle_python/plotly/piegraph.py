import plotly.express as px
from basestyle import BaseStyle

class Pie:
    basestyle = BaseStyle()

    @classmethod
    def pie(
        cls,
        data,
        names,
        values,
        hole: float = 0.4,
        width = 750,
        height = 490,
        text_format: str = None,
        **kwargs
        ):

        fig = px.pie(
            data_frame=data, 
            names=names, 
            values=values, 
            width=width, 
            height=height, 
            hole=hole, 
            template = BaseStyle().get_base_template(),
            **kwargs
            )
        
        if text_format:
            fig.update_traces(texttemplate=text_format)
        
        return fig