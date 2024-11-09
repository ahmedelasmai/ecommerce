# my ecommerce website

ecommerce website built using django

[website](https://ahmedelasmai.eu.pythonanywhere.com/products/)

## Content

- [ecommerce](#my-ecommerce-website)
- [Introduction](#introduction)
  - [Goals](#goals)
  - [Repo Structure](#repo-structure)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [running the project](#running-the-project)
- [Documentation](#documentation)
- [How to test](#white_check_mark-how-to-test)
- [Contribute](#contribute)
- [Bugs and Issues](#bugs-and-issues)
- [License](#license)
- [Code of conduct](#code-of-conduct)

# Introduction

todo

## Goals

- todo

## Project Structure

The vanilla Django project structure is used.

:warning: use production branch to deploy in production enviroment

## Requirements

- python 3.9 or higher
- sqlite 
- Git
- virtualenv (recommended)

## Installation

To install the packages in your project follow these steps:

1. (recommended) create a virtual enviroment using virtual enviroment (The example is on windows. mac is only slightly different) 
  1. ```bash
   python -m venv venv
   ```
  2. ```bash
     venv\Scripts\activate
     ```
2. **clone the repo. You can choose between the development branch or production ready one** 

```bash
   git clone --single-branch -b main https://github.com/jacketoff/ecommerce
   ```
```bash
   git clone --single-branch -b production https://github.com/jacketoff/ecommerce
   ```

```bash
cd ecommerce
```
3. **install requirements.txt**
```bash
pip install -r requirements.txt
```

4. **set up the database**
```bash
    cd ecom
     python manage.py migrate
     ```
5. **Create a Superuser (Optional)**
   - If you need access to the Django admin panel, create a superuser:
     ```bash
     python manage.py createsuperuser
     ```

6. **run on local server**
```bash
python manage.py runserver
```

7. **Access the Application**
   - Open your web browser and go to `http://127.0.0.1:8000/` to view your application.
   - If you created a superuser, you can access the admin panel at `http://127.0.0.1:8000/admin/`.

# Documentation

[Read more](./docs/)

# How To Test

[Read more](./docs/TESTING.md)

# Contribute

[Read more](./docs/CONTRIBUTE.md)

# Bugs and Issues

If you would like to open an issue, you can gladly use [this page](https://github.com/jacketoff/ecommerce/issues).
But please, have a look at the [Contribute](./docs/CONTRIBUTE.md) page before filing a bug.

# License

[GPL-3.0 LICENSE](./LICENSE.md)

# Code of Conduct

You can find the [Code of Conduct here](./docs/CODE_OF_CONDUCT.md)
