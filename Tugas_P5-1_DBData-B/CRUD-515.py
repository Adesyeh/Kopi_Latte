import sqlite3
 
conn = sqlite3.connect('cars51.db')
c = conn.cursor()
c.execute("""INSERT INTO cars51 (ID, BRAND, MODEL, PRICE) VALUES ("172", "TOYOTA", "FORTUNER", "550")""")
conn.commit()
c.close()