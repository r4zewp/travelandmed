class User:
    def __init__(self, id: int, username: str, tid: int, name: str, created_at: str):
       self.id = id
       self.username = username
       self.tid = tid
       self.created_at = created_at
       self.name = name

    @staticmethod
    def from_json(json: dict):
        return User(
            id=json['id'],
            created_at=json['created_at'],
            username=json['username'],
            tid=json['tid'],
            name=json['name']
        )

    def to_json(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'username': self.username,
            'tid': self.tid,
            'name': self.name
        }



