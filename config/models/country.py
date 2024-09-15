from config.models.city import City

class Country:
    def __init__(self, id: int, name: str, name_ru: str, cities: [City]):
        self.id = id,
        self.name = name,
        self.name_ru = name_ru
        self.cities = cities

    @staticmethod
    def from_json(json: dict):
        return Country(
            id=json['id'],
            name=json['name'],
            name_ru=json['name_ru'],
            cities=City.from_json(json['cities'])
        )

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_ru': self.name_ru
        }

