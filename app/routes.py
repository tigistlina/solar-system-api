from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

planets = [
    Planet(1, "Earth", "habitable", "12742km in diameter"),
    Planet(2, "Mercury", "inhabitable", "4880km in diameter"),
    Planet(3, "Venus", "inhabitable", "12104km in diameter"),
    Planet(4, "Mars", "inhabitable", "6779km in diameter"),
    Planet(5, "Jupiter", "inhabitable", "139822km in diameter"),
    Planet(6, "Saturn", "inhabitable", "116460km in diameter")
]

