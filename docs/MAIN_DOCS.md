# main section of the documentation

# todo: add contents ❗

## architecture

I used the default Django project structure 

![System Design](system%20design.svg)

## models

#### products model

This stores the product a user uploads. It has a one to many relationship with the stock model

#### stock model

Model for how much stock each product has. Each product has 3 sizes per stock: big, medium, small (e.g small: 100 items, medium: 80 items, large: 90 items). It has a a foreign key named 'Product' which references the Product model.


## econ app

This app is the starting app that has the settings.py and wsgi.py file and is the central point for routing incoming requests.

## cart app

The cart app uses Django sessions (database backed) to get cart contents. I didn't use cookies because they get sent through every request which can slow response time while sessions only get sent when requested and the cart info doesn't have to be sent on every request.

session (python dictionary) structure: `{product_id { name, price, quantity, size, image_location}}`

## products app

This main part of the project. The main page is displayed here it contains the main models: products and stock. The views are: upload view, product view and products view   

## User app / authentication

I used the Django authentication framework as its secure, follows best practices and intergrates seemlessly. Also it allowed me to focus more on developing the app. 

## misc

- Static and media files are stored in /econ/ I didn't put much thought into where they are stored for development because in production they are served through the web server.
- If you installed requirements.txt with a virtual enviroment active. Your virtual enviroment must be active when running or testing the app because of stripe. 

