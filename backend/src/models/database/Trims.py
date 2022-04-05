from tortoise import fields
from tortoise.models import Model


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
    weight= fields.IntField()

    mpge = fields.FloatField(null=True)
    kwh100mi = fields.IntField(null=True)
    charge120v = fields.TextField(null=True)
    charge240v = fields.TextField(null=True)
    chargeport = fields.TextField(null=True)
    price = fields.IntField()
    rating = fields.FloatField(null=True)

    class Meta:
        table = "trims"
