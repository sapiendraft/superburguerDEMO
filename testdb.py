from django.db import connections
from django.db.utils import OperationalError
db_conn = connections["DEFAULT"]
try:
    c = db_conn.cursor()
except OperationalError:
    connected = False
else:
    connected = True