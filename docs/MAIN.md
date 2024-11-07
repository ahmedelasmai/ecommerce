# main section of the documentation

## models

### products model

This stores the product a user uploads. It has a one to many relationship with

### stock model

Model for how much stock each product has. Each product has 3 sizes per stock: big, medium, small (e.g small: 100 items, medium: 80 items, large: 90 items). It has a a foreign key named 'Product' which references the Product model.


## cart app

The cart app uses Django sessions (database backed) to get cart contents. 

## products app

This main part of the project. The main page is displayed here it contains the main models: products and stock. The views are: upload view, (single) product view and products view   

## User app / authentication

I used the Django authentication framework as its secure, follows best practices and intergrates seemlessly. Also I wanted to focus more on developing the app. 
