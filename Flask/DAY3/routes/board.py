from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Board
from models import User
from schemas import BoardSchema

board_blp = Blueprint('Boards', __name__, description='Operations on boards', url_prefix='/board')

@board_blp.route('/')
class BoardList(MethodView):
    
    """
    def get(self):
        boards = Board.query.all()
        return jsonify([{"user_id": board.user_id, 
                         "id": board.id,
                         "title": board.title, "content": board.content, "author": board.author.name} for board in boards])
    """
    @board_blp.response(200,schema=BoardSchema(many=True))
    def get(self):
        boards = Board.query.all()
        return boards
    
    """
    def post(self):
        data = request.json
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        db.session.add(new_board)
        db.session.commit()
        return jsonify({"message": "Board created"}), 201
    """
    @board_blp.arguments(BoardSchema)
    @board_blp.response(201,schema=None)
    def post(self,data):
        # user_id가 존재하지 않으면 자동으로 404 에러 반환
        User.query.get_or_404(data['user_id'])
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        db.session.add(new_board)
        db.session.commit()
        return {"message": "Board created"}

@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    """
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)
        return jsonify({"title": board.title, "content": board.content, "author": board.author.name})
    """
    @board_blp.response(200,schema=BoardSchema())
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)
        return board
    """
    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.json
        board.title = data['title']
        board.content = data['content']
        db.session.commit()
        return jsonify({"message": "Board updated"})
    """
    @board_blp.arguments(BoardSchema(exclude=('user_id',)))
    @board_blp.response(200,schema=None)
    def put(self, board_id,data):
        board = Board.query.get_or_404(board_id)
        board.title = data['title']
        board.content = data['content']
        db.session.commit()
        return {"message": "Board updated"}
    """
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"message": "Board deleted"})
    """
    @board_blp.response(200,schema=None)
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return {"message": "Board deleted"}