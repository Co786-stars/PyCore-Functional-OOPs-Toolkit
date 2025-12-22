"""
Basic cmd commands that use to check Django is installed or not ?
> python -m pip install -upgrade pip
  by using this command we update the pip download package manager of python

> pip --version
  to check the version of pip


> python -m venv .venv
  To make sure our virtual environment is properly created.

> pip install -upgrade pip setuptools wheel
  To Reinstall standard libraries if needed


> pip show django
  by using this we see the version, location, summary, homepage... etc. about django if it is installed in system.

> where python
  to see the exact location of python executable file where it installed
  C:\Users\<YourName>\AppData\Local\Microsoft\WindowsApps\python.exe
  C:\Users\<YourName>\AppData\Local\Programs\Python\Python311\Scripts

   Note : - When command "django-admin" works in cmd ?
    → if we install python from microsoft/app store then the location of python is
      C:\Users\<YourName>\AppData\Local\Microsoft\WindowsApps\python.exe
      that doesn't give access to normal the Script folder where ( pip.exe and django-admin.exe live)

    → if we install python from python.org/downloads. then the location of python is
      C:\Users\<YourName>\AppData\Local\Programs\Python\Python311\Scripts
      that  give access to normal the Script folder where ( pip.exe and django-admin.exe live)

  C:\Users\<YourName>\AppData\Local\Microsoft\WindowsApps\python.exe
  is a Windows Store alias, not the actual Python installation folder. that’s why you couldn’t find Scripts
  or Python311 — the real installation isn’t there


> pip install django
  if nothing show then we use this command to install django package after installation python from python.org website
  because give access to normal the Script folder.

> django-admin startproject myproject
  creates a new Django project with default settings and structure
  simple steps that we follow to execute this command in cmd : -
  create a new  directory  and open in cmd and use this command.
  suppose we create directory "xyz" then  C:\Users\<YourName>\xyz>django-admin startproject MyprojectName

"""


# Quick summary : -
# python -m pip install --upgrade pip        → updates pip to the latest version
# pip --version                              → checks the installed pip version
# python -m venv .venv                       → creates a virtual environment named .venv
# pip install --upgrade pip setuptools wheel → upgrades/reinstalls essential Python packaging tools
# pip show django                            → displays details if Django is installed (version, location, etc.)
# where python                               → shows the exact location of the Python executable
# pip install django                         → installs the Django framework
# django-admin startproject myproject        → creates a new Django project with default settings and structure


