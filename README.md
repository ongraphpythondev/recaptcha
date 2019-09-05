# reCaptcha

reCaptcha provides additional security to websites to protect the website to be used by bots.

django-recaptcha supports Google reCAPTCHA V2 - Checkbox (Default), Google reCAPTCHA V2 - Invisible and Google reCAPTCHA V3.

This application uses Google reCAPTCHA V2.

## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+
* [Virtual Environment](https://pypi.org/project/virtualenv/)

To install virtual environment on your system use:

```bash
pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)
```
* ReCaptcha Public Key
* ReCaptcha Private Key


To get the message application to work you would need to [register](https://www.google.com/recaptcha/admin/create) your website on [google recaptcha](https://developers.google.com/recaptcha/intro) to get a private and a public key for your application.
## Installation:

```bash
git clone https://github.com/ongraphpythondev/recaptcha.git

cd recaptcha

virtualenv venv
      or
virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# install required packages for the project to run
pip install -r requirements.txt
```
In Project directory's recaptcha/settings.py file you would need to change

```python

RECAPTCHA_PUBLIC_KEY = '<your ReCaptcha public key>'
RECAPTCHA_PRIVATE_KEY = '<your ReCaptcha private key>'
```


## Running:

To run the development server after installation:
```bash
# activate the virtual environment
venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# run server
python manage.py runserver
```
