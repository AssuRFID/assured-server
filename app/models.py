from app import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    uid = db.Column(db.String(32), index=True, unique=True)
    access_room1 = db.Column(db.Boolean)
    inside_room1 = db.Column(db.Boolean)

    @property
    def serialise(self):
        return {
            'id': self.id,
            'name': self.name,
            'uid': self.uid,
            'access_room1': self.access_room1,
            'inside_room1': self.inside_room1
        }

    def __repr__(self):
        return '<Tag {}, name {}>'.format(self.uid, self.name)
