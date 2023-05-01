import sqlite3

# Maak verbinding met de database
conn = sqlite3.connect("my_database.sqlite")
cursor = conn.cursor()

# Maak de tabel 'users' aan als deze nog niet bestaat
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# Voeg wat gegevens toe
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))

# Commit de wijzigingen
conn.commit()

# Vraag gegevens op
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
print("All users:")
for user in all_users:
    print(user)

# Vraag gegevens op met een voorwaarde
cursor.execute("SELECT * FROM users WHERE age > 25")
older_users = cursor.fetchall()
print("\nUsers older than 25:")
for user in older_users:
    print(user)

# Sluit de verbinding
conn.close()
