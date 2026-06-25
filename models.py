from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200))
    address = db.Column(db.String(300))
    favorite = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Contact {self.name}"