import io

from openpyxl import Workbook


def export_to_excel(transactions):
    wb = Workbook()
    ws = wb.active
    ws.title = "Transactions"

    ws.append(["Date", "Type", "Category", "Amount", "Description"])

    for t in transactions:
        ws.append([t["date"], t["type"], t["category"], t["amount"], t["description"]])

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer
