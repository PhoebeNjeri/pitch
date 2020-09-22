from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy ()

class user(db.model):
    """ user model """

    __tablename__ =  "users"
    id = db.column(db.integer, primary_key=True)
    username = db.column(db.string(25), unique=True, nullable=False)
    password = db.column(db.string(), nullable=false)

    
