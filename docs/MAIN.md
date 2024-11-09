# main section of the documentation


## models

#### products model

This stores the product a user uploads. It has a one to many relationship with the stock model

#### stock model

Model for how much stock each product has. Each product has 3 sizes per stock: big, medium, small (e.g small: 100 items, medium: 80 items, large: 90 items). It has a a foreign key named 'Product' which references the Product model.


## cart app

The cart app uses Django sessions (database backed) to get cart contents. I didn't use cookies because they get sent through every request which can slow response time while sessions only get sent when requested and the cart info doesn't have to be sent on every request.

## products app

This main part of the project. The main page is displayed here it contains the main models: products and stock. The views are: upload view, (single) product view and products view   

## User app / authentication

I used the Django authentication framework as its secure, follows best practices and intergrates seemlessly. Also it allowed me to focus more on developing the app. 

## architecture

I used the default Django project structure as I felt django cookiecutter had too many features that I didn't need 

## misc

- static and media files are stored in /econ/ I didn't put much thought into where they are stored for development because in production they are servered through the web server.
