# Immutable Objects in Python

The code in this repository demonstrates three ways of defining (near) immutable objects in Python.
The tests illustrate some commonalities and differences.

## Getting Started

I use [pyenv](https://github.com/pyenv/pyenv) and [pipenv](https://pypi.python.org/pypi/pipenv) to easily switch between projects using different Python versions and dependencies.
If that's not your thing, you can just run `pip install attrs` and `pip install pytest` and ignore everything below.

1. Install [pyenv](https://github.com/pyenv/pyenv), a tool for managing [Python](https://www.python.org/) versions.
1. The file `.python-version` in the root folder specifies the Python version required for this project.
  Navigate to the root folder and execute `pyenv install` to install this Python version.
1. Install [pipenv](https://pypi.python.org/pypi/pipenv) by executing `pip3 install pipenv`.
  There's an [issue related to language and region settings](https://github.com/kennethreitz/pipenv/issues/538) that you might run into, but it's easy to resolve.
1. Create a new virtual environment with all dependencies by executing `pipenv install --dev --ignore-pipfile`.
  The flag `ignore-pipfile` is used to indicate that the exact versions of the dependencies as specified in `Pipfile.lock` should be installed.
  The flag `dev` is used to also install development dependencies.

  If you run into issues due to an existing virtual environment for this project, delete that environment by executing `pipenv --rm`.

## Activating the virtual environment

Before executing any of the commands below, you need to activate the virtual environment.
You can do so by executing `pipenv shell`.
Your command prompt should now indicate that you've activated the virtual environment.
It can be deactivated by executing `exit`.

## Tests

Execute `pytest` to run all tests once.
Execute `pytest-watch` to run all tests whenever a file changes.

## Linting

Execute `flake8` to lint all code.

## Code formatting

Execute `black .` to format all code.
