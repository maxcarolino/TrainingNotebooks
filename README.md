# KLab Cyscorpion Training Notebooks

Feb 1, 2016

These Jupyter (iPython) notebooks are used internally at Klab Cyscorpions for Python training. We are making them publicly available so that anyone can benefit from them, even students or non-employees. Feel free to star, clone or fork the repo for your own use. If you feel that something can be improved, feel free to open up an issue with the notebook name in the title for easy identification. We also welcome pull requests.

The main requirements for using these notebooks are:

* Python 3.x
* pip
* Jupyter
* git

## Python

If you don't have **Python 3** installed yet, please download it from [Python.org](https://www.python.org/).

You can check if Python is installed by typing `python` in the command line. If it goes to the Python interpreter, then you already have Python installed. You can check the version from the very first line after your command. You should see something like:

```
Python 3.5.1 (default, Dec  7 2015, 11:24:55)
Type "copyright", "credits" or "license" for more information.
>>>
```

## Pip

If you already have Python installed, make sure you have the python package manager, **pip**. If you need to install pip, just follow the instructions from the [pip documentation](https://pip.pypa.io/en/stable/installing/).

You can check if pip is installed by typing `pip` in the command line. If it gives you the help screen, then you already have pip:

```
Usage:   
  pip <command> [options]

Commands:
...
```

## Jupyter

Then just `pip3 install jupyter`. Please refer to the [Jupyter documentation](http://jupyter.readthedocs.org/en/latest/install.html#using-pip) if you encounter any problems.

> Some of Jupyter’s dependencies may require compilation, in which case you would need the ability to compile Python C-extensions. This means a C compiler and the Python headers. On Debian-based systems (e.g. Ubuntu), you can get this with:

> `apt-get install build-essential python3-dev`

> And on Fedora-based systems (e.g. Red Hat, CentOS):

> `yum groupinstall 'Development Tools'`

> `yum install python3-devel`

> (Use python instead of python3 for legacy Python 2.)

## Git

I assume you already have git installed. Just in case you don't, please refer to the instructions in the [Git documentation](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Once you already have Jupyter installed, you just need to clone this repository by typing:

`git clone https://github.com/KLabCyscorpions/TrainingNotebooks.git`

Enter your github credentials when asked and you should have a local copy of the repository. 

## Notebook

To open the notebooks, just type `ipython notebook`. You should be redirected to a browser page with links to folders of training notebooks.

Browse the TrainingNotebooks subdirectories. Notebooks have a `.ipnb` extension.
