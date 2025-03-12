from flask import Flask, render_template

app = Flask(__name__)

books = [
    {"id": 1213, "title": "1984", "author": "George Orwell", "year": 1825},
    {"id": 1214, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"id": 1215, "title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "year": 1943},
    {"id": 1216, "title": "Harry Potter and the Sorcerer’s Stone", "author": "J.K. Rowling", "year": 1997},
]

@app.route('/')
def index():
    return render_template('books.html', books=books, title="TOP 5 best-selling books of all time")

@app.route('/id/<int:book_id>')
def getBook(book_id):
    for book in books:
        if book["id"] == book_id:
            return render_template('book.html', book=book)
    return "Book not found!"

if __name__ == '__main__':
    app.run(debug=True)