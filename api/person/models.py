from beanie import Document


class Person(Document):
    firstname: str
    lastname: str