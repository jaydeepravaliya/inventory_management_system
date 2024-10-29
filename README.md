# Convenience Store Inventory Management System

## Overview
This project is a Django-based inventory management system designed specifically for a convenience store. It utilizes Django REST Framework (DRF) to provide a RESTful API for managing products, categories, and suppliers.

## Features
- Product CRUD operations
- Category and supplier management
- Admin-only access for creating, editing, and deleting products
- RESTful API endpoints for integration with front-end applications

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jaydeepravaliya/inventory_management_system.git
cd inventory_management_system


Create a Virtual Environment:

It is recommended to create a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
Activate the Virtual Environment:

In your terminal, run:

bash
Copy code
venv\Scripts\activate
Install Requirements:

Install the necessary packages:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

Set up the database by running:

bash
Copy code
python manage.py migrate
Create a Superuser:

To access the admin panel, create a superuser account:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up your superuser credentials.

Run the Server:

Start the development server:

bash
Copy code
python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.

Usage