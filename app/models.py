from app import db
from datetime import datetime

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow )