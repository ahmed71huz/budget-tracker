from flask import Flask, render_template, request, redirect, url_for, send_file

import db
import excel_export

app = Flask(__name__)
db.init_db()  # Initialize the database when the app starts

@app.route("/")
def home():
    transactions = db.list_transactions()
    return render_template("index.html", transactions=transactions)

@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        db.create_transaction(request.form)
        return redirect(url_for("home"))
    return render_template("add.html")
@app.route("/delete/<int:tx_id>", methods=["POST"])
def delete_transaction(tx_id):
    db.delete_transaction(tx_id)
    return redirect(url_for("home"))
@app.route("/edit/<int:tx_id>", methods=["GET", "POST"])

def edit_transaction(tx_id):
    if request.method == "POST":
        db.update_transaction(tx_id, request.form)
        return redirect(url_for("home"))
    transaction = db.get_transaction(tx_id)
    return render_template("edit.html", t=transaction)
@app.route("/dashboard")

def dashboard():
    stats = db.get_stats()
    return render_template("dashboard.html", stats=stats)
@app.route("/export")

def export():
    transactions = db.list_transactions()
    buffer = excel_export.export_to_excel(transactions)
    return send_file(
        buffer,
        as_attachment=True,
        download_name="budget_report.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
if __name__ == "__main__":
    app.run(debug=True)

