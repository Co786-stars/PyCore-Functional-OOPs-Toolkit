"""
Basic cmd commands that use to check Django is installed or not ?
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
  # need to read about this command ..
"""