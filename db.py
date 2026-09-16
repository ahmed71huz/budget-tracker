import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "budget.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            type        TEXT NOT NULL,
            category    TEXT NOT NULL,
            amount      REAL NOT NULL,
            date        TEXT NOT NULL,
            description TEXT
        )
        """
    )
    conn.commit()
    conn.close()
def create_transaction(data):
    conn = get_connection()
    conn.execute(
        """
        INSERT INTO transactions (type, category, amount, date, description)
        VALUES (?, ?, ?, ?, ?)
        """,
        (data["type"], data["category"], data["amount"], data["date"], data["description"]),
    )
    conn.commit()
    conn.close()


def list_transactions():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM transactions ORDER BY date DESC").fetchall()
    conn.close()
    return [dict(row) for row in rows]

def delete_transaction(tx_id):
    conn = get_connection()
    conn.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
    conn.commit()
    conn.close()

def get_transaction(tx_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM transactions WHERE id = ?", (tx_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def update_transaction(tx_id, data):
    conn = get_connection()
    conn.execute(
        """
        UPDATE transactions
        SET type = ?, category = ?, amount = ?, date = ?, description = ?
        WHERE id = ?
        """,
        (data["type"], data["category"], data["amount"], data["date"], data["description"], tx_id),
    )
    conn.commit()
    conn.close()
def get_stats():
    conn = get_connection()

    income = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE type = 'income'"
    ).fetchone()[0]

    expense = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM transactions WHERE type = 'expense'"
    ).fetchone()[0]

    by_category = conn.execute(
        """
        SELECT category, SUM(amount) as total
        FROM transactions
        WHERE type = 'expense'
        GROUP BY category
        ORDER BY total DESC
        """
    ).fetchall()

    conn.close()

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense,
        "by_category": [{"category": row["category"], "total": row["total"]} for row in by_category],
    }
    