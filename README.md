# My Ecommerce Website

Ecommerce website built using Django.

[Live Website](https://ahmedelasmai.eu.pythonanywhere.com/products/)

## To Do
- finish off tests / better tests
- examples of clean code
- show Go4 patterns

## Content

- [Ecommerce](#my-ecommerce-website)
- [Introduction](#introduction)
  - [Repo Structure](#repo-structure)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Documentation](#documentation)
- [How to Test](#how-to-test)

# Introduction

### Why I Chose Django

tl;dr

I prefer opinionated frameworks because they make learning backend development easier, I'm still learning so without having a structure I can rely on i might miss imporant best practices and details (this happened to me with flask) and if I do overlook a detail there might be an problem somwhere and im forced to learn said detail. It also makes it easy to follow best practices. I also prefer having common features like ORM and authentication already included, so I can focus on building the application. Also it makes it easier for me to work on other projects that also use these features. Django enforce best practices, which is very important.

- Experss.js: I didn't chose this because Its lighweight and Django's ORM is far more mature compared to prisma.

- Flask: similar to Express I prefer Django's Opinionated approach for this project

- Ruby on rails: I didn't choose ruby because from what I researched its not being used as much these days.

- ASP.NET: I was seriously considering this framework as it has very good preformance and scalability, used alot in enterprise and its backed by microsoft

- spring: similar to ASP.NET

## Project Structure

The vanilla Django project structure is used.

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
2. **Clone the repo:**

   ```bash
   git clone --single-branch -b main https://github.com/jacketoff/ecommerce
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
   ⚠️(the virutal enviroment must be active when starting the server)
   ```bash
   python manage.py runserver
   ```

8. **Access the Application:**
   - Open your web browser and go to `http://127.0.0.1:8000/` to view your application.
   - If you created a superuser, you can access the admin panel at `http://127.0.0.1:8000/admin/`.

(optional) 8. **stripe checkout**
   - sign up for stripe and copy the public and private keys.
   - go to root project directory (the directory with manage.py) and create a .env file
   - paste you keys: 
   ```
   STRIPE_PUBLIC_KEY=your_public_key
   STRIPE_SECRET_KEY=your_secret_key
   ```
   - add in base_url for localhost to .env (http://127.0.0.1:8000 is the default url)
   ```
   BASE_URL=http://127.0.0.1:8000
   ```
# Documentation

[Read more](./docs/MAIN_DOCS.md)

# How to Test

[Read more](./docs/TESTING.md)
