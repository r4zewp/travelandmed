class ClientOffer:
    def __init__(self, id: int, phone: str, created_from: str, uid: int, offers: [int], created_at: str):
        self.id = id,
        self.phone = phone,
        self.created_from = created_from,
        self.uid = uid,
        self.offers = offers,
        self.created_at = created_at

    @staticmethod
    def from_json(json: dict):
        try:
            return ClientOffer(
                id=json['id'],
                phone=json['phone'],
                created_from=json['created_from'],
                uid=json['uid'],
                offers=json.get('offers', []),  # Default to empty list if 'offers' is missing
                created_at=json['created_at']
            )
        except KeyError as e:
            raise ValueError(f"Missing key in JSON data: {e}")

    def to_json(self):
        return {
            'id': self.id,
            'phone': self.phone,
            'created_from': self.created_from,
            'uid': self.uid,
            'offers': self.offers,
            'created_at': self.created_at
        }
