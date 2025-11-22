import sqlite3

def execute_query(query, data=None):
    connect = sqlite3.connect("library.db")
    cursor = connect.cursor()
    if data:
        cursor.executemany(query, data)
    else:
        cursor.execute(query)
    connect.commit()
    connect.close()

def fetch_query(query, data=None):
    connect = sqlite3.connect("library.db")
    cursor = connect.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    connect.close()
    return results

execute_query("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    genre TEXT,
    available INTEGER DEFAULT 1 
)
""")

execute_query("""
CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    borrower TEXT,
    loan_date TEXT,
    return_data TEXT, 
    FOREIGN KEY(book_id) REFERENCES books(id)
)
""")

books_data = [
    (1, "1984", "Gearge Orwell", 1949, "Dystopia", 1),
    (2, "Harry Potter", "J.K. Rowling", 1997, "Fantasy", 1),
    (3, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 1),
    (4, "To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 1)
]
execute_query("INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?, ?, ?)", books_data)
loans_data = [
    (1, 1, "Alice", "2025-11-01", None),
    (2, 3, "Bob", "2025-11-10", None)
]
execute_query("INSERT OR IGNORE INTO loans VALUES (?, ?, ?, ?, ?)", loans_data)

issued_books = fetch_query("""
SELECT title, author
FROM books
WHERE id IN (SELECT book_id FROM loans WHERE return_data IS NULL)
""")
print("Книги в данный момент выданы: ")
for row in issued_books:
    print(row)

genre_counts = fetch_query("""
SELECT genre, COUNT(*) as count
FROM books
GROUP BY genre
""")
print("\nКоличество книг по жанрам: ")
for row in genre_counts:
    print(row)

execute_query("""
CREATE VIEW IF NOT EXISTS available_books AS
SELECT id, title, author, genre
FROM books
WHERE available = 1
""")

available_books = fetch_query("SELECT * FROM available_books")
print("\nДоступные книги : ")
for row in available_books:
    print(row)

