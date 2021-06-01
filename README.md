# oistyle - the OIS styling library - Python Edition

## Why oistyle?
To standardize OIS styling across programming languages and frameworks. Our MS Office stack has great templates for styling, but for programming languages such as python, R, and javascript, no _common_ templates exist. But, if you've ever had to make publication-ready visualizations and you were too proud to copy your data to Excel, chances are that you've fiddled around with OIS styling yourself. 

This repo aims to bring together all these separate styling efforts. The goal is to provide importable templates for most if not all of the programming languages and visualization libraries we use at OIS, and that these templates all use the same source for basic styling. 

Here's how it works: this set of repos provides the styling basics and a framework so that the templates are installable as a library in various languages, and we rely on contributors to add templates for new visualisation tools. So if you have a template lying around: make a pull request! Also read the instructions for contributing below. 

Find usage examples and more at the [main oistyle repo](https://github.com/jbosga-ams/oistyle).


## What's in oistyle-python?
Right now `oistyle_python` contains templates for `plotly` and `seaborn`. 

## Usage
In your preferred environment, run 

`pip install git+https://github.com/jbosga-ams/oistyle-python.git`

You can now import from the `oistyle_python` namespace like so:

`from oistyle_python.plotly import colors, line_chart_template`

See the [main oistyle repo](https://github.com/jbosga-ams/oistyle/examples) for example notebooks. 

__Note for Linux users__: make sure you have the Corbel font installed. You can do so via [one of these methods](https://www.stugon.com/install-microsoft-fonts-ubuntu/#:~:text=%20How%20to%20Install%20Microsoft%20Fonts%20in%20Ubuntu,Install%20Microsoft%20Fonts%20Using%20Software%20Center%20More%20).

## Contributing
Contributing to this styling library is highly encouraged. 
If you'd like to contribute in one of the languages already present here, navigate to the relevant submodule repository and make a pull request there. If your preferred framework/language isn't here yet, feel free to make a new repository and build it yourself. 

The only request is to use the `base_style.json` file provided [here](https://raw.githubusercontent.com/jbosga-ams/oistyle/main/base_style.json) to ensure styling consistency between languages. For now, the way to go is to load the json directly from its url into your own library. This makes sure it's loaded whenever your library is imported by a user, which ensures the styling stays up to date. 

Be sure to get in touch with the maintainers of `oistyle` when you've made your implementation so that we can add your repo as a submodule.

Want to get started with contributing, but don't feel like taking on a whole library by yourself? Check out the issue page!
