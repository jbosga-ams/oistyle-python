# oistyle - the OIS styling library


## Why oistyle?
To standardize OIS styling across programming languages and frameworks. Our MS Office stack has great templates for styling, but for programming languages such as python, R, and javascript, no _common_ templates exist. But, if you've ever had to make publication-ready visualizations and you were too proud to copy your data to Excel, chances are that you've fiddled around with OIS styling yourself. 

This repo aims to bring together all these separate styling efforts. The goal is to provide importable templates for most if not all of the programming languages and visualization libraries we use at OIS, and that these templates all use the same source for basic styling. 

Here's how it works: this repo provides the styling basics and a framework so that the templates are installable as a library in various languages, and we rely on contributors to add templates for new visualisation tools. So if you have a template lying around: make a pull request! Also read the instructions for contributing below. 


## What's in oistyle?
Right now `oistyle` contains templates for python plotly, python seaborn, and js plotly. 

## Usage

### Python
In your preferred environment, run 

`pip install git+https://github.com/jbosga-ams/oistyle.git`

You can now import from the `oistyle.python` namespace like so:

`from oistyle.python.plotly import colors, line_chart_template`

See `src/examples/python_plotly.ipynb` for specific `plotly` usage and examples. 

__Note for Linux users__: make sure you have the Corbel font installed. You can do so via [one of these methods](https://www.stugon.com/install-microsoft-fonts-ubuntu/#:~:text=%20How%20to%20Install%20Microsoft%20Fonts%20in%20Ubuntu,Install%20Microsoft%20Fonts%20Using%20Software%20Center%20More%20).

## Contributing



## To do

MVP: 
- R




Inhoud: 
- R markdown?
- More examples
- axis line vs gridline formatting
- Percentage mark at right position


Issues
- Fix Corbel font for seaborn on linux (check [this link](https://scentellegher.github.io/visualization/2018/05/02/custom-fonts-matplotlib.html))
