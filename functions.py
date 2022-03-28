from datetime import datetime

def format_date(data):
    return datetime.strptime(data, "%d-%m-%Y")
