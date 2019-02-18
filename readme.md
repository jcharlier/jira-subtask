# Jira Subtask

Automate the process of creating subtasks into jira after a planning meeting.


## Getting Started

Just clone the repo and run the main file ``main.py``. 

The dependencies should be installed either via your package manager, [pip](https://pypi.org/project/pip/), or [anaconda](https://www.anaconda.com/download/)
This project was built on Python 3 and I personally use and recommend anaconda to manage your python and dependencies for any OS.

## Prerequisites

If you run the project, python may complain about some missing libraries.
Normally your system will miss ``PyQt5``, and ``jira``

Just install them either via your package manager or pip, or anaconda

Example for ubuntu 18.04:
```
sudo apt install python3-pip
sudo pip3 install jira PyQt5 lxml pip install beautifulsoup4
```


or if you use anaconda:
```
conda install -c conda-forge jira
conda install -c conda-forge qtpy
conda install -c conda-forge lxml
conda install -c conda-forge beautifulsoup4

```
You may need to install some other packages depending on your system, but you're on your own with that ;)

## Installing

Download the source code

```
git clone https://github.com/jcharlier/jira-subtask.git
cd jira-subtask
```

Run the software by running the command:
```
python3 ./main.py
```

press ``CTRL+J`` or click ``Menu->Credenciais Jira`` to add your Jira credentials (email, token, url)

## Usage

Copy your story data from a spreadsheet (we use google) using this layout:
```
| Parent Story Key | Title | Description | Dev Points | QA Points |
```
Paste the actual table, it will look like an html table in the preview, then press ``Iniciar``

The app will connect using your credentials to the supplied jira, and create one dev task and one qa task for each line where there are points supplied. 


## Built With

* [PyQt5](http://pyqt.sourceforge.net/Docs/PyQt5/) - Graphical framework for python
* [Qt Designer](http://doc.qt.io/qt-5/qtdesigner-manual.html/) - Tool for designing and building GUIs from Qt components

## Authors

* **Jean Charlier** - *Initial work* - [jcharlier](https://github.com/jcharlier)

## License

This project is licensed under the Mobly Software License (?) *check with the repo owner before anything :)*