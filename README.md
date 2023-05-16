# Hospital Nurse Mediator

Hospital Nurse Mediator is a Django-based web application that facilitates communication and coordination between hospitals, nurses, and mediators. It provides a platform for managing user accounts, scheduling, and information exchange.

## Features

- User registration and authentication
- User roles and permissions management (Hospitals, Nurses, Mediators)
- Hospital account management
- Nurse account management
- Mediator account management
- Schedule management
- Information exchange and communication between users

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/manishkrojha0/Hospital_Nurse_Mediator.git

2. Navigate to the project directory:
   ```bash 
   cd Hospital_Nurse_Mediator
3. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate or myenv/Scripts/activate
4. Install the project dependencies:
   ```bash
    pip install -r requirements.txt
5. Apply database migrations:
   ```bash
   python manage.py migrate
6. Test cases
   ```bash
   python manage.py test
   
7. Deployment
   1. Deployed the project on render.
   2. Deployment base url -  ``` bash https://mydoc.onrender.com
   3. Refer the Postman API collections to understand the apis.
 
# Hospital Nurse Mediator API Documentation
## Introduction
- The Hospital Nurse Mediator API provides endpoints for managing users in a healthcare system, including hospitals, nurses, and mediators. This documentation      describes the available API endpoints, their request/response formats, and authentication requirements.

# Base URL
- The base URL for all API endpoints is: https://api.example.com

# Authentication
- Authentication is required to access most of the API endpoints. The API uses token-based authentication. To authenticate, include the token in the Authorization header of each request.

``` bash
   Authorization: Bearer <access_token>  
   ````
# Postman Collections 
- curl this url in your postman or simply paste this url - https://manishkrojha0.pythonanywhere.com/url-hasher/click/9xq57zqg/
   
# Acknowledgements
  ## Django
  ## Django REST Framework
  ## Simple JWT
  ## PostgreSQL
# Contact
  For any questions, issues, or inquiries, please contact manishkrojha0@gmail.com.

Feel free to customize the README file based on your project's specific details, including any additional sections or information you'd like to include.
