# population-treemap

U.S. population treemap from 2020 census data

## Findings so far

-This is where some key visualizations will go.

## Getting Started

Please read the [contributing documentation](contributing.md) before contributing.

You'll need an API key for accessing the 2020 Census data. Head to [api.census.gov/data/key_signup.html](https://api.census.gov/data/key_signup.html) to request a key.

Create a `config.py` file and add your key as a variable

```python
API_KEY = 'YOUR_API_KEY'
```

### Windows

In a terminal create and start a python virtual environment from your local machine

```terminal
\path\to\population-treemap> python -m venv venv
\path\to\population-treemap> .\venv\Scripts\activate
```

Install requirements in a virtual environment

```terminal
(venv) \path\to\population-treemap> python3 -m pip install -r requirements.txt
```

Deactivating the virtual environment

```terminal
(venv) \path\to\population-treemap> deactivate
```

### macOS & Linux(Ubuntu)

In a terminal, create and start a Python virtual environment from your local machine:

```terminal
/path/to/population-treemap$ python3 -m venv venv
/path/to/population-treemap$ source venv/bin/activate
```

Install requirements in the virtual environment:

```terminal
(venv) /path/to/population-treemap$ pip3 install -r requirements.txt
```

Deactivating the virtual environment

```terminal
(venv) /path/to/population-treemap$ deactivate
```
