import mysql.connector

try:
  my_db = mysql.connector.connect(
  host = "localhost",
  username = "root",
  password = "Abel0916addis,80",
  )
  
  if my_db.is_connected():
    my_cursor = my_db.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("'alx_book_store' created successfully!")
except mysql.connector.Error as e:
  print(f"Error connecting to MySQL: {e}")

finally:
  if my_db.is_connected():
    my_cursor.close()
    my_db.close()