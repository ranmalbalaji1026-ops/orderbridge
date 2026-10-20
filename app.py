import sqlite3
from flask import Flask, render_template, request, redirect
from database import save_order, get_all_orders, update_order_status, get_order_by_id, delete_order,add_status_column
app = Flask(__name__)



@app.route("/add-order", methods=["GET", "POST"])
def add_order():
    if request.method == "POST":
        customer_name = request.form.get("customer_name", "").strip()
        product_name = request.form.get("product_name", "").strip()
        quantity = request.form.get("quantity", "").strip()

        if not customer_name or not product_name or not quantity:
            return "Error: All fields are required.", 400

        try:
            quantity = int(quantity)
            if quantity < 1:
                return "Error: Quantity must be at least 1.", 400
        except ValueError:
            return "Error: Quantity must be a whole number.", 400

        save_order(customer_name, product_name, quantity)
        return redirect("/")

    return render_template("add_order.html")




@app.route("/")
def home():
    all_orders = get_all_orders()

    search_query = request.args.get("search", "").strip().lower()
    status_filter = request.args.get("status", "All")

    total_orders = len(all_orders)
    pending_orders = sum(
        1 for order in all_orders if order[4] == "Pending"
    )
    completed_orders = sum(
        1 for order in all_orders if order[4] == "Completed"
    )

    orders = all_orders

    if search_query:
        orders = [
            order for order in orders
            if search_query in order[1].lower()
            or search_query in order[2].lower()
        ]

    if status_filter in ["Pending", "Completed"]:
        orders = [
            order for order in orders
            if order[4] == status_filter
        ]

    return render_template(
        "index.html",
        total_orders=total_orders,
        pending_orders=pending_orders,
        completed_orders=completed_orders,
        orders=orders
    )



@app.route("/complete-order/<int:order_id>", methods=["POST"])
def complete_order(order_id):
    update_order_status(order_id, "Completed")
    return redirect("/")


@app.route("/delete-order/<int:order_id>", methods=["POST"])
def remove_order(order_id):
    delete_order(order_id)
    return redirect("/")



@app.route("/edit-order/<int:order_id>", methods=["GET", "POST"])
def edit_order(order_id):
    order = get_order_by_id(order_id)

    if order is None:
        return "Order not found", 404

    if request.method == "POST":
        customer_name = request.form.get("customer_name", "").strip()
        product_name = request.form.get("product_name", "").strip()
        quantity = request.form.get("quantity", "").strip()

        if not customer_name or not product_name or not quantity:
            return "Error: All fields are required.", 400

        try:
            quantity = int(quantity)

            if quantity < 1:
                return "Error: Quantity must be at least 1.", 400

        except ValueError:
            return "Error: Quantity must be a whole number.", 400

        
        connection = sqlite3.connect("orderbridge.db")

        try:
            cursor = connection.cursor()

            cursor.execute(
                """UPDATE orders
                   SET customer_name = ?, product_name = ?, quantity = ?
                   WHERE id = ?""",
                (customer_name, product_name, quantity, order_id)
            )

            connection.commit()

        except sqlite3.Error:
            connection.rollback()
            raise

        finally:
            connection.close()


        return redirect("/")

    return render_template("edit_order.html", order=order)






if __name__ == "__main__":
    from database import create_table

    create_table()
    add_status_column()

    app.run(debug=True)
