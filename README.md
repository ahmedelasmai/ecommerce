# My Ecommerce Website

Ecommerce website built using Django.

[Website](https://ahmedelasmai.eu.pythonanywhere.com/products/)

## Content

- [Ecommerce](#my-ecommerce-website)
- [Introduction](#introduction)
  - [Goals](#goals)
  - [Repo Structure](#repo-structure)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Documentation](#documentation)
- [How to Test](#how-to-test)
- [Contribute](#contribute)
- [Bugs and Issues](#bugs-and-issues)
- [License](#license)
- [Code of Conduct](#code-of-conduct)

# Introduction

_TODO_

## Goals

- _TODO_

## Project Structure

The vanilla Django project structure is used.

> :warning: Use the production branch to deploy in a production environment.

## Requirements

- Python 3.9 or higher
- SQLite 
- Git
- Virtualenv (recommended)

## Installation

To install the packages in your project, follow these steps:

1. (Recommended) Create a virtual environment using virtualenv (The example is for Windows; Mac is only slightly different):
   1. 
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. **Clone the repo. You can choose between the development branch or the production-ready one:**

   ```bash
   git clone --single-branch -b main https://github.com/jacketoff/ecommerce
   ```
   OR
   ```bash
   git clone --single-branch -b production https://github.com/jacketoff/ecommerce
   ```

   ```bash
   cd ecommerce
   ```
3. **Install requirements.txt:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   cd ecom
   python manage.py migrate
   ```
5. **Create a Superuser (Optional):**
   - If you need access to the Django admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run on local server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   - Open your web browser and go to `http://127.0.0.1:8000/` to view your application.
   - If you created a superuser, you can access the admin panel at `http://127.0.0.1:8000/admin/`.

# Documentation

[Read more](./docs/)

# How to Test

[Read more](./docs/TESTING.md)

# Contribute

[Read more](./docs/CONTRIBUTE.md)

# Bugs and Issues

If you would like to open an issue, you can gladly use [this page](https://github.com/jacketoff/ecommerce/issues). But please, have a look at the [Contribute](./docs/CONTRIBUTE.md) page before filing a bug.

# License

[GPL-3.0 LICENSE](./LICENSE.md)

# Code of Conduct

You can find the [Code of Conduct here](./docs/CODE_OF_CONDUCT.md)
