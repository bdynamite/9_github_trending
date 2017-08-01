# Github Trends

displays 20 most rated repo from GitHub with issues

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart


Example of script launch on Linux, Python 3.5:

```#!bash

$ python github_trending.py

# output example
********************
Repository "trust"
url: https://github.com/ncase/trust
issues: 7
Github→GitHub https://api.github.com/repos/ncase/trust/issues/14
Grudger wins instead of the copycat https://api.github.com/repos/ncase/trust/issues/13
...
...
Unable to clone the repo https://api.github.com/repos/ncase/trust/issues/12
Cyrillic fonts https://api.github.com/repos/ncase/trust/issues/10
********************
Repository "open-source-flash"
url: https://github.com/pakastin/open-source-flash
issues: 16
Flash spec is already open source right?  https://api.github.com/repos/pakastin/open-source-flash/issues/36
...
...


```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
