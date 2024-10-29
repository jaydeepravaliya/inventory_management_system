# Convenience Store Inventory Management System

## Overview
This project is a Django-based inventory management system designed specifically for a convenience store. It utilizes Django REST Framework (DRF) to provide a RESTful API for managing products, categories, and suppliers.

## Features
- Product CRUD operations
- Category and supplier management
- Admin-only access for creating, editing, and deleting products
- RESTful API endpoints for integration with front-end applications

## Installation

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/jaydeepravaliya/inventory_management_system.git
cd inventory_management_system
```

### 2. Create a Virtual Environment
It’s recommended to create a virtual environment to manage dependencies:
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
Activate the virtual environment:

For Windows:
```bash
venv\Scripts\activate
```

For macOS and Linux:
```bash
source venv/bin/activate
```
### 4. Install Requirements
Install the necessary packages:
```bash
pip install -r requirements.txt
```

### 5. Run Migrations
Set up the database by running:

```bash
python manage.py migrate
```

### 6. Create a Superuser
To access the admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```
Follow the prompts to set up your superuser credentials.

### 7. Run the Server
Start the development server:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`

### Usage
Once the server is running, you can:
- Access the admin panel at `/admin/` to manage products, categories, and suppliers.
- Use the RESTful API endpoints for integration with front-end applications.

### API Endpoints
Here are some key endpoints:

- Product List: 'GET /api/products/`
- Product Detail: `GET /api/products/<id>/`
- Create Product: `POST /api/products/`
- Update Product: `PUT /api/products/<id>/`
- Delete Product: `DELETE /api/products/<id>/`

### Contributing
- Contributions are welcome! Please feel free to open an issue or submit a pull request.









