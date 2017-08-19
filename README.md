# microblog_server_with_tests
A microblog server written in Django with both unit and functional tests. 

## Setup

#### For Windows 10 Windows Subsystem for Linux (WSL) only.
The following instructions were adapted from http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/

- install python 3.6 using a ppa (or compile it yourself from source)
- sudo add-apt-repository ppa:jonathonf/python-3.6
- Create a method to switch between python3.5 (used by ubuntu internally, removing will break OS installation) and your newly-installed python3.6
- `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1`
- `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2`
- Switch to python3.6
- `sudo update-alternatives --config python3`
- Install virtualenvironment package (optional, but recommended)
- `sudo apt-get install python3.6-venv`
- `pip3 install virtualenv`
