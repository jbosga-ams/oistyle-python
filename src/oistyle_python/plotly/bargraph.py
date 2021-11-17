import plotly.express as px
from oistyle_python.plotly.basestyle import BaseStyle
import pandas as pd


class Bar:
    basestyle = BaseStyle()

    @classmethod
    def bar(
        cls,
        data,
        x: str,
        y: str,
        color: str = None,
        color_discrete_sequence: list = None,
        orientation: str = None,
        barmode=None,
        width=750,
        height=490,
        **kwargs
    ):
        fig = px.bar(
            data_frame=data,
            x=x,
            y=y,
            color=color,
            template=cls.basestyle.get_base_template(
                'bar', orientation=orientation),
            width=width,
            color_discrete_sequence=color_discrete_sequence,
            height=height,
            barmode=barmode,
            **kwargs
        )

        fig.update_layout(
            dict(xaxis_title_text='', yaxis_title_text='', legend_title_text=''))

        return fig

    @classmethod
    def stacked_single(
        cls,
        data,
        x: str,
        y: str,
        color: str = None,
        color_discrete_sequence: list = None,
        orientation='v',
        **kwargs
    ):
        fig = cls.bar(
            data=data,
            x=x,
            y=y,
            color=color,
            color_discrete_sequence=color_discrete_sequence,
            barmode="relative",
            orientation=orientation,
            **kwargs
        )

        if orientation == 'v':
            fig.update_xaxes(showticklabels=False)
        if orientation == 'h':
            fig.update_yaxes(showticklabels=False)

        return fig

    @classmethod
    def stacked_multiple(
        cls,
        data,
        x: str,
        y: str,
        color: str = None,
        color_discrete_sequence: list = None,
        orientation='v',
        **kwargs
    ):
        fig = cls.bar(
            data=data,
            x=x,
            y=y,
            color=color,
            color_discrete_sequence=color_discrete_sequence,
            barmode="stack",
            orientation=orientation,
            **kwargs
        )

        return fig

    @classmethod
    def grouped(
        cls,
        data,
        x: str,
        y: str,
        color: str = None,
        color_discrete_sequence: list = None,
        orientation='v',
        **kwargs
    ):

        fig = cls.bar(
            data=data,
            x=x,
            y=y,
            color=color,
            color_discrete_sequence=color_discrete_sequence,
            barmode="group",
            orientation=orientation,
            **kwargs
        )

        return fig

    @classmethod
    def single(
        cls,
        data,
        x: str,
        y: str,
        color_discrete_sequence: list = None,
        orientation='v',
        **kwargs
    ):

        fig = cls.bar(
            data=data,
            x=x,
            y=y,
            color_discrete_sequence=color_discrete_sequence,
            orientation=orientation,
            **kwargs
        )

        if orientation == "h":
            fig.update_yaxes(automargin=True)

        return fig


    @classmethod
    def likert(
        cls,
        data,
        x: str,
        y: str,
        color: str = None,
        color_discrete_sequence: list = None,
        orientation='v',
        greys = None,
        order = None,
        **kwargs
    ):
        if order:
            data[x] = pd.categorical(data[x])



        fig = cls.bar(
            data=data,
            x=x,
            y=y,
            color=color,
            color_discrete_sequence=color_discrete_sequence,
            barmode="stack",
            orientation=orientation,
            **kwargs
        )

        return fig
