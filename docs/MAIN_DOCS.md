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


## cart app

The cart app uses Django sessions (database backed) to get cart contents. I didn't use cookies because they get sent through every request which can slow response time while sessions only get sent when requested and the cart info doesn't have to be sent on every request.

session structure (dictionary): {product_id { name, price, quantity, size, image_location}}

## products app

This main part of the project. The main page is displayed here it contains the main models: products and stock. The views are: upload view, (single) product view and products view   

## User app / authentication

I used the Django authentication framework as its secure, follows best practices and intergrates seemlessly. Also it allowed me to focus more on developing the app. 

## misc

- static and media files are stored in /econ/ I didn't put much thought into where they are stored for development because in production they are servered through the web server.

