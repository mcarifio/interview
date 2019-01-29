# Interviewpy [![Build Status](https://travis-ci.org/mcarifio/interviewpy.svg?branch=master)](https://travis-ci.org/mcarifio/interviewpy)



Interview questions posed and solved. Sometimes after the fact. Think of this as the adult version of posting college
rejection notices. I had a fair amount of those too.

## Layout

I try to do interview questions in python3 to speed things along for me and the interviewer. It hasn't always worked.

The repo uses [pyenv](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv) for the environment and 
[poetry](https://poetry.eustace.io/docs/) for the local (project venv) modules. In this way, the global environment should remain pristine.
[Pycharm](https://www.jetbrains.com/pycharm/) doesn't have builtin support for `pyproject.toml` files (but does for `pipenv Pipfile`) 
so either I build at the command line or run `pytest` independent of `poetry`.

This project uses the [python guide structure recommendations](https://docs.python-guide.org/writing/structure/) with `interview` as "the module". It puts `tests` at the project top level as
recommended by `pytest`. Of course, it would be nice if we could all coordinate these conventions. Until then, make your own. 


