
# OrderBridge — Order Management System

OrderBridge is a web-based order management application built using Python, Flask, and SQLite. It helps users manage customer orders through a simple dashboard.

## Features

- Dashboard with total, pending, and completed order counts
- Add new orders
- View all orders
- Edit existing orders
- Mark orders as completed
- Delete orders with a confirmation prompt
- Search orders by customer or product name
- Filter orders by status
- Input validation for order forms
- Responsive interface

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- Git and GitHub

## Project Structure

```text
OrderBridge/
├── app.py
├── database.py
├── templates/
│   ├── index.html
│   ├── add_order.html
│   └── edit_order.html
├── static/
│   └── css/
│       └── style.css
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ranmalbalaji1026-ops/orderbridge.git
   ```

2. Enter the project directory:

   ```bash
   cd orderbridge
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment on macOS or Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install Flask:

   ```bash
   pip install Flask
   ```

6. Start the application:

   ```bash
   python app.py
   ```

7. Open the local address displayed in the terminal, usually:

   http://127.0.0.1:5000/

## Database

OrderBridge uses SQLite. The database file is created locally when the application initializes the database schema. Existing local order data is not included in this repository.

## Future Improvements

- User authentication
- Order sorting and pagination
- Improved error pages
- Deployment to a hosting platform

## Author

**OrderBridge Project**

Built as a learning project to practice Python web development, Flask routing, database operations, and frontend styling.
