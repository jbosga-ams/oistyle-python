FROM jupyter/r-notebook:latest


COPY requirements.txt .
RUN pip install -r requirements.txt
RUN jupyter labextension install jupyterlab-plotly@4.14.3
