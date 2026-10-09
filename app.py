from flask import Flask, abort, jsonify, request

from orders import db

app = Flask(__name__)


@app.get("/orders/<int:order_id>")
def order(order_id):
    found = db.get_order(order_id)
    if found is None:
        abort(404)
    return jsonify(found)


@app.get("/orders/search")
def search():
    customer = request.args.get("customer", "")
    return jsonify(db.search_orders(customer))
