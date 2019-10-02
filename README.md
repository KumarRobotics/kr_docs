# Introducing kr_docs

This repo is a collection of general documentation to consider when contributing to the KumarRobotics organization.

Click the following link to read the docs.

### [Kumar Robotics Github Documentation](http://kumar-robotics-github-documentation.readthedocs.org/en/master/)

## How to contribute

Contributing to `kr_docs` is easy.

If you are using Ubuntu, simply do:

```
sudo apt-get install python-sphinx python-sphinx-rtd-theme python-recommonmark
git clone https://github.com/KumarRobotics/kr_docs.git
cd kr_docs/docs
make html
xdg-open build/html/index.html
```
If build fails, install latest packages from pip
```
sudo apt install python-pip
sudo pip install sphinx sphinx-rtd-theme recommonmark
```

If you are using OSX and already have [Homebrew](http://brew.sh), simpliy do

```
brew install sphinx
sudo pip install sphinx_rtd_theme recommonmark
git clone https://github.com/KumarRobotics/kr_docs.git
cd kr_docs/docs
make html
open build/html/index.html
```

You will see your latest changes locally.
