from app import db

class User(db.Model):
    
    id =            db.Column(db.Integer,       primary_key=True)
    username =      db.Column(db.String(32),    nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128),   nullable=False)
    created_at =    db.Column(db.DateTime,      nullable=False)
    active =        db.Column(db.Boolean,      nullable=False)

    def __str__(self):
        return f"User {self.id} ({self.username}), registered on {self.created_at} -- status: {self.active}"
    