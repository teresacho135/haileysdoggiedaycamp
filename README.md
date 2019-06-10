
# Hailey's Dog Camp

https://haileys-dog-camp.herokuapp.com/

A business profile website built with Django and Postgres streamlined to serve both Profile and Auth to users. My objective for this website was to create an simple and easy to navigate landing for users to understand Hailey's business. If the users are clients of Hailey's then this website would serve as an organizational website for both clients and Hailey to cater to the needs of the dogs as well as business functionality to monitor invoices as well as Campers('dogs') that are current or prospective. I wanted clients to register their profiles and within their profiles, they could attach their dogs to their profile which could be served to Hailey to obtain information about said 'Camper.' Information about the camper would range from age to medicine instructions and emergency veternarian information. By creating this website, I hope to see that Hailey would be able to showcase her business as well as cater to her current clients. 

## Technologies Used

Front End:

1. Bootstrap + Tachyon
2. HTML + CSS
3. Crispy Forms for Django
4. Django + Jinja
5. Unsplashed Images

Back End:

1. Postgres
2. Django Fixtures
3. DBGlass
4. Python

Deployment:

Heroku

https://github.com/teresacho135/haileysdoggiedaycamp

## Installlation Steps

1. Django
2. Django Extentsions
3. Changing Databses to serve postgresql
4. Install Crispy Forms

## ERD, Wireframe, and User Stories

https://trello.com/b/tXQnMYr5/haileys-doggie-daycamp

## Unsolved Problems 

One of the hardest problems that I strugged with was styling forms that were automatically served through Django and especially styling and forms that were imported into .html templates. The only way I could solve it was using devtools in Chrome to target specific div's HOWEVER, it would not be sematic styling within HTML and I would be blindly styling/trial and error CSS that would take so much time. Another issue I struggled with was serving specific views for profile's and their linked campers. 

Finally, I was not able to reach Auth in terms of views outside the Auth page that Django already serves. I wanted to create and superuser restricted content that would only pertain to Hailey. This is future goals that I definitely hope to finish. 
