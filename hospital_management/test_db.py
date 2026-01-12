from db import get_connection

con = get_connection()
if con:
    print("✅ Database connected")
    con.close()
else:
    print("❌ Database not connected")
