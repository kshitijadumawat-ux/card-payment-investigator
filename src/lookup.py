import csv, io, urllib.request

url = "https://raw.githubusercontent.com/kshitijadumawat-ux/card-payment-investigator/main/data/transactions.csv"
text = urllib.request.urlopen(url).read().decode("utf-8")
rows = list(csv.DictReader(io.StringIO(text)))


def get_transaction(transaction_id):
    """Return the matching transaction record, or None if it does not exist."""
    for row in rows:
        if row["transaction_id"] == transaction_id:
            return row
    return None


print(get_transaction("CARD-106"))
print(get_transaction("CARD-999"))
