from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Trims(Model):
    id = fields.IntField(pk=True)
    car = fields.ForeignKeyField("models.Cars")
    trim = fields.TextField()
    kwh = fields.IntField()
    range = fields.IntField()
    fwd = fields.BooleanField()
    rwd = fields.BooleanField()
    awd = fields.BooleanField()
    acceleration = fields.FloatField()
    horsepower = fields.IntField()
    torque = fields.IntField()
    weight = fields.IntField()
    mpge = fields.FloatField(null=True)
    kwh100mi = fields.IntField(null=True)
    charge120v = fields.TextField(null=True)
    charge240v = fields.TextField(null=True)
    chargeport = fields.TextField(null=True)
    price = fields.IntField()
    rating = fields.FloatField(null=True)

    def dollars_per_horsepower(self) -> float:
        return round((self.price / self.horsepower), 2)

    def dollars_per_torque(self) -> float:
        return round((self.price / self.torque), 2)

    def dollars_per_mile(self) -> float:
        return round((self.price / self.range), 2)

    class PydanticMeta:
        computed = ["dollars_per_horsepower", "dollars_per_torque", "dollars_per_mile"]

    class Meta:
        table = "trims"


Trims_Response = pydantic_model_creator(Trims)
