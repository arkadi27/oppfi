Apily is a python based framework for testing REST apis. 

# Installation

The very first step is to install python 3 on your machine. All the tests have been using python 3; test execution with python 2 should be fine.

# virtualenv
virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

It can be used standalone, in place of Pipenv.

Install virtualenv via pip:
$ Switch to super user account prior to virtualenv installation by calling sudo su

$ **pip3 install virtualenv** - Might need to install pip first

Test your installation:

$ **virtualenv --version**


*  Create a virtual environment for a project:

    $ **cd project_folder**


    $ **virtualenv venvName**

    virtualenv venvName will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. venvName can be anything; omitting the name will place the files in the current directory instead.
    

*  To begin using the virtual environment, it needs to be activated:

    $ **source venv/bin/activate**
    
    The name of the current virtual environment will now appear on the left of the prompt (e.g. (venvName)Your-Computer:project_folder UserName$) to let you know that it’s active. From now on, any package that you install using pip will be placed in the venvName folder, isolated from the global Python installation.

For Windows, the same command mentioned in step 1 can be used to create a virtual environment. However, activating the environment requires a slightly different command.


Assuming that you are in your project directory:


**C:\Users\SomeUser\project_folder> venvName\Scripts\activate**

# Usage Example

To be able to run tests, follow these steps:

* your virtual environment should have been actived from steps above
*  **pip3 install -r requirements.txt** - command to install needed dependencies
*  **pytest src/test/ --html=reports/TestResults.html -vv -n 2** - this for example will run tests for inside src/test directory, where -n is the number of parallel executions

# Note
Fixtures starting with l_ are local fixtures. Meaning you'll find them in the conftest.py file located in the same directory as the service name. For example l_get_posts can be found in /posts directory. Fixtures starting with g_ are global fixtures and are located in the src/test directory in the conftest.py file.

Failing test cases are due to non valide operations returning status codes different than 405.

If you are done working in the virtual environment for the moment, you can deactivate it:

$ **deactivate**

# Useful Links
*  [pytest](https://docs.pytest.org/en/latest/)
*  [virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)
*  [requests http library](https://3.python-requests.org/)
*  [pytest fixtures](https://docs.pytest.org/en/latest/fixture.html)
