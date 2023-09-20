# COMP0035 2023-24 Coursework

## Setup instructions

The structure of the code in this repository follows the guidance given
in [Python Packaging](https://packaging.python.org/tutorials/packaging-projects/).

Please complete the steps below.

### 1. Make sure you understand the files in the repo

Aside from the coursework starter files, there are some essential files that you need to set up your project's code.
These are:

- [`.gitignore`](.gitignore) this file lists files that should not be tracked by source code control. This includes
  standard Python packages and configuration files for your IDE. Other developers only need your code, they will have
  their own IDE config and their own version of Python packages.
- [`README.md`](README.md) this file tells other developers useful information about your project. Check out this
  example for the [Python pandas package](https://github.com/pandas-dev/pandas). You should always have
  a [README.md and this documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
  explains why and how to create one.
- [`requirements.txt`](requirements.txt) this file lists any Python packages that your project needs in order for the
  code to run.
  The [documentation explains the file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/), at
  its simplest you list the names of the packages in the format they are in the PyPi index; with one on each line.
- [`pyproject.toml`](pyproject.toml) this file contains metadata (info about your project) needed by Python tools that
  are used to build your code as a package. More
  on [pyproject.toml here](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata)
  .
- [`LICENSE`](LICENSE) this file is optional
  though [GitHub guidance recommends you include a license](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
  . It tells other developers what rights they have to use/adapt your code.

### 1. Clone the project from GitHub to your IDE (VS Code, PyCharm etc).

Find the documentation for how to do this in the documentation for your particular IDE.

- [Cloning a repository - VS Code](https://code.visualstudio.com/docs/sourcecontrol/github#_cloning-a-repository)
- [Check out a project (clone) - PyCharm](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)

### 2. Create and activate a Python virtual environment in the directory of the project

There are several tools that allow you to create Python virtual environment in a project such as Python venv, pipenv and
poetry. You may use any.

`venv` comes with Python so the following should work for all.

#### Create a virtual environment

To create a virtual environment, open the Terminal in your IDE (VS Code, PyCharm). Check that you are in the directory
of the project, if not, navigate to it.

Enter
the [code](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
to create the "venv" in the Terminal.

- Unix/macOS `python3 -m venv .venv`
- Windows `py -m venv .venv`

The code `python3 -m venv .venv` means:

- `python3 -m` is the macOS version of the code to run a python module
- `venv` is the Python package or module that will be used to create a virtual environment
- `.venv` is the name of the folder or directory within your project that the virtual enviornment will be created in.
  The `.` makes it a hidden folder; useful as you do not want to make manual changes to this folder. By convention call
  this folder `env`, `venv`, `.env` or `.venv`. By adhering to this naming convention the `.gitignore` for this project
  will then exclude it from source code control (which is what you want in this case).

The command will take a few minutes to complete.

#### Activate an environment

You now need to activate the virtual environment for the current project.

VS Code usually prompts to ask if you want to activate the environment; which you should accept.

Check if the environment has been activated. You can confirm you’re in the virtual environment by checking the location
of your Python interpreter:

- Unix/macOS `which python`
- Windows `where python`

For a visual clue, the command prompt in your Terminal in VSCode and PyCharm has an indicator with the name of the
virtual environment folder in brackets at the start. In the following example it
is `(.venv)`: `(.venv) yourcomputername:yourreponame yourusername$`

If the virtual environment is not activated then activate it by
entering [code in the Terminal](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment)
. In the following replace `env` with the folder name you created the virtual environment in.

- Unix/macOS: `source env/bin/activate`
- Windows: `.\env\Scripts\activate`

### 3. Install the dependencies in the environment

For the coursework1 you will need pandas. For coursework2 you will need pytest.

There are several tools that allow you to manage dependencies in a project such as pip, poetry, pipenv. `pip` is
sufficient for this project, though you can use others if you prefer.

We use two techniques in this course using the [`pip install` command](https://pip.pypa.io/en/stable/cli/pip_install/).
The first installs several packages at once. The second installs one package (though you can install several at a time).

- `pip install -r requirements.txt` installs all the packages listed in a file named `requirements.txt`
- `pip install pandas` installs the specified package, in this example `pandas`; or this example installs pandas and
  pytest:
  `pip install pandas pytest`

Find
the [correct syntax for your operating system](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#using-requirements-files)
and then use it to install the packages from requirements.txt in your virtual environment.

Other useful `pip` commands are:

- [`pip list`](https://pip.pypa.io/en/stable/cli/pip_list/) which lists the packages that have been installed and their
  versions
- `pip install --upgrade <name of package to updagrade>` to upgrade to the latest version of one or more packages
- [`pip freeze > requirements.txt`](https://pip.pypa.io/en/stable/cli/pip_freeze/) to create a requirements.txt file
  with all the packages installed in your venv

### 4. Install the code in this repo in your environment

This is needed for coursework 2.

Installing your code as a package in the following way means that any changes you make to the code will affect the
installed package without needing to re-install it.

This process requires a configuration file about the project such as `pyproject.toml`, `setup.cfg` or `setup.py`.

This repository has a `pyproject.toml` configuration file. For more detail on
this [refer to the documentation](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

Enter
the [code for your operating system](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-from-source)
in the Terminal of the project's root folder in your IDE.

`pip install --editable .` or `pip install -e .` - the `.` refers to anything in the current directory tree in the
command prompt of the terminal. It should be the project root.