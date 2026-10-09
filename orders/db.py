import sqlite3

DB_PATH = "orders.db"


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_order(order_id: int):
    with connect() as conn:
        row = conn.execute(
            "SELECT id, customer, total, status FROM orders WHERE id = ?",
            (order_id,),
        ).fetchone()
    return dict(row) if row else None


def search_orders(customer: str):
    query = f"SELECT id, customer, total, status FROM orders WHERE customer LIKE '%{customer}%'"
    with connect() as conn:
        rows = conn.execute(query).fetchall()
    return [dict(r) for r in rows]
