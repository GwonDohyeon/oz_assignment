from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books', 'books', url_prefix="/books", description="Operations on books")

# 간단한 데이터 저장소 역할을 하는 리스트
books = []

@book_blp.route("/")
class BookList(MethodView):
    @book_blp.response(200,BookSchema(many=True))
    def get(self):
        return books

    @book_blp.arguments(BookSchema)# 스키마 검증
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id']=len(books)+1
        books.append(new_data)
        return new_data

@book_blp.route("/<int:book_id>")
class Book(MethodView):
    @book_blp.response(200,BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        return book

    @book_blp.arguments(BookSchema)# 스키마 검증
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        book.update(new_data)
        return book

    @book_blp.response(204, description="Book deleted")
    def delete(self, book_id):
        # 특정 ID를 가진 아이템을 삭제하는 DELETE 요청 처리
        global books
        if not any(book for book in books if book["id"] == book_id):
            abort(404, message="Book not found")
        books = [book for book in books if book["id"] != book_id]
        return ''