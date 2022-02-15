# sign_image

_Simple shell application for image signing with Python._

## Starting

_These instructions will allow you to get a working copy of the project on your local machine._


### Pre requirements 📋

_Before starting, you need to make sure you have an environment with Python3, Virtualenv, libfreetype6, libfreetype6-dev, PIP and git, in order to perform the installation process and run the application._

```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install virtualenv
sudo apt-get install python3-virtualenv
sudo apt-get install libfreetype6
sudo apt-get install libfreetype6-dev
sudo apt-get install git
```

### Installation 🔧

_All the console instructions below are intended to be executed in environments with Linux distributions, but it should be noted that they may vary depending on the distribution and can also be carried out in a similar way in Windows and OS X environments.:_

1. Clone the project repository in the directory of your choice:

```
https://github.com/jsolorzano/sign_image.git
```

2. Activate the virtual environment contained in the project:

```
source ../sign_image/myvenv/bin/activate
```
_This step is very important to do before moving on to the next ones, since you must have your virtualenv active for the application to work._
_You will know you have virtualenv started when you see that the command line in your console has the prefix (myvenv)._



## Execution 🚀

_Once all the previous steps have been carried out, you will be ready to run the application._

```
cd ../sign_image/
python3 main.py
```
_If you have reached this point, you will have a menu available with two options; one (S) to sign the image containing the project with a name and another (E) to exit the application._



---
⌨️ por [jsolorzano](https://github.com/jsolorzano)
