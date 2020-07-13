from .db import db


class Resistor(db.Model):
    __tablename__ = 'resistor'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    factor = db.Column(db.Integer, nullable=False)
    tolerance = db.Column(db.String, nullable=False)
    measured_unit = db.Column(db.String, nullable=False)
    variable = db.Column(db.Integer, nullable=False)
    coefficient = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"['{self.color}','{self.value}','{self.factor}'," \
               f"'{self.tolerance}','{self.variable}''{self.coefficient}']"
