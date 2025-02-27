from flask import Flask,render_template
from flask_smorest import Api
from db import db
from routes.users import user_blp
from routes.board import board_blp
from schemas import *
from flask_migrate import Migrate
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1234@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db.init_app(app)
migrate=Migrate(app,db)

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api=Api(app)
with app.app_context():
    api.spec.components.schema("BoardSchema", schema=BoardSchema)
    api.spec.components.schema("UserSchema", schema=UserSchema)
    api.register_blueprint(board_blp)
    api.register_blueprint(user_blp)

@app.route('/manage_board')
def manage_board():
    return render_template('board.html')

@app.route('/manage_users')
def manage_users():
    return render_template('users.html')

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)