from .base import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front_side = db.Column(db.String(120), unique=True, nullable=False)
    back_side = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Card {self.front_side}>'