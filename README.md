# microblog_server_with_tests
A microblog server written in Django with both unit and functional tests. 


## Requirements

`python3.6`  
`firefox`  
`geckowebdriver`  
`selenium`  
`django`  

## Setup

#### Mac OS X setup (Recommended)
- `brew update`
- `brew install geckodriver`
- `brew install python3`
- `pip3 install virtualenv`
- `python3 -m venv microblog/`
- `source microblog_packages/bin/activate`
- OPTION A:  `pip install django, selenium`
- OR OPTION B: `pip install -r requirements.txt`

#### For Windows 10 Windows Subsystem for Linux (WSL) only. (8/19/17)
The following instructions were adapted from http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/ and https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu.  

You'll need an xserver to run the functional tests. Xming is popular. 
THIS IS NOT RECOMMENDED.  

*install python 3.6 using a ppa (or compile it yourself from source)*
- `sudo add-apt-repository ppa:jonathonf/python-3.6`
*Create a method to switch between python3.5 (used by ubuntu internally, removing will break OS installation) and your newly-installed python3.6*
- `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1`
- `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2`
*Switch default python3 to python3.6*
- `sudo update-alternatives --config python3`
*Install virtualenvironment package (The use of a venv is optional, but recommended)*
- `sudo apt install python3.6-venv`
- `pip3 install virtualenv`
*Install geckodriver (for functional tests)*
- `wget [url to geckodriver source]` https://github.com/mozilla/geckodriver/releases
- `tar -xvzf geckodriver`
- `chmod +x gecokdriver`
- `sudo mv geckodriver /usr/local/bin/`
*Setting up the virtual environment*
- `mkdir packages`
- `python3 -m venv packages/`
- `source packages/bin/activate`
- `pip install "django<1.12" "selenium<4"`

