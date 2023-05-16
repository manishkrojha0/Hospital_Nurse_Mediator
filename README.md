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
   2. Deployment base url -
      ```bash
       https://mydoc.onrender.com
   4. Refer the Postman API collections to understand the apis.
 
# Hospital Nurse Mediator API Documentation
## Introduction
- The Hospital Nurse Mediator API provides endpoints for managing users in a healthcare system, including hospitals, nurses, and mediators. This documentation      describes the available API endpoints, their request/response formats, and authentication requirements.

# Base URL
- The base URL for all API endpoints is: https://mydoc.onrender.com

# Authentication
- Authentication is required to access most of the API endpoints. The API uses token-based authentication. To authenticate, include the token in the Authorization header of each request.

``` bash
   Authorization: Bearer <access_token>  
   ````
# Postman Collections 
- curl this url in your postman or simply paste this url - https://rb.gy/co6c2

# Dockerisation of this project
- Follow these steps to dockerise.
  1. Docker: Install Docker
  2. Docker Compose: Install Docker Compose
  3. Clone the repository to your local machine:
     ```bash
     git clone https://github.com/manishkrojha0/Hospital_Nurse_Mediator.git
  4. Navigate to the project directory:
     ```bash
     cd Hospital_Nurse_Mediator
  5. Build the Docker image:
     ```bash
     docker build -t hospital-nurse-mediator .
  6. Run the Docker container:
     ``bash
     docker run -d -p 8000:8000 hospital-nurse-mediator
  7. Access the application:
     Open your web browser and visit http://localhost:8000 to access the Hospital Nurse Mediator application.
   
# Acknowledgements
  - Django
  - Django REST Framework
  - Simple JWT
  - PostgreSQL

# Contact
  For any questions, issues, or inquiries, please contact manishkrojha0@gmail.com.

Feel free to customize the README file based on your project's specific details, including any additional sections or information you'd like to include.
