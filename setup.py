import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oistyle_python",
    version="0.0.1",
    author="Jorren Bosga",
    author_email="j.bosga@amsterdam.nl",
    description="Amsterdam OIS house style.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jbosga-ams/oistyle-python",
    project_urls={
        "Bug Tracker": "https://github.com/jbosga-ams/oistyle-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)