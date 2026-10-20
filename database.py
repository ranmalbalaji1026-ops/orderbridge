import sqlite3

def create_table():
    connection = sqlite3.connect("orderbridge.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending'
        )
    """)

    connection.commit()
    connection.close()




def save_order(customer_name, product_name, quantity):
    connection = sqlite3.connect("orderbridge.db")

    try:
        cursor = connection.cursor()

        cursor.execute(
            """INSERT INTO orders
            (customer_name, product_name, quantity, status)
            VALUES (?, ?, ?, ?)""",
            (customer_name, product_name, quantity, "Pending")
        )

        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()





def get_all_orders():
    connection = sqlite3.connect("orderbridge.db")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        return orders

    finally:
        connection.close()




def add_status_column():
    connection = sqlite3.connect("orderbridge.db")

    try:
        cursor = connection.cursor()
        cursor.execute("PRAGMA table_info(orders)")

        columns = [
            column[1] for column in cursor.fetchall()
        ]

        if "status" not in columns:
            cursor.execute(
                """ALTER TABLE orders
                   ADD COLUMN status TEXT NOT NULL
                   DEFAULT 'Pending'"""
            )

        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()




def update_order_status(order_id, new_status):
    connection = sqlite3.connect("orderbridge.db")

    try:
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE orders SET status = ? WHERE id = ?",
            (new_status, order_id)
        )

        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()



def get_order_by_id(order_id):
    connection = sqlite3.connect("orderbridge.db")

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM orders WHERE id = ?",
            (order_id,)
        )
        order = cursor.fetchone()
        return order

    finally:
        connection.close()




def delete_order(order_id):
    connection = sqlite3.connect("orderbridge.db")

    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM orders WHERE id = ?",
            (order_id,)
        )
        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()




