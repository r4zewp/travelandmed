class City:
    def __init__(self, id: int, name: str, cid: int):
        self.id = id,
        self.name = name,
        self.cid = cid

    @staticmethod
    def from_json(json: dict):
        cities = []
        for js in json:
            try:
                city = City(
                    id=js['id'],
                    name=js['name'],
                    cid=js['cid']
                )
                cities.append(city)
            except KeyError as e:
                raise ValueError(f"Missing key in JSON data: {e}")
        return cities

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'cid': self.cid
        }
