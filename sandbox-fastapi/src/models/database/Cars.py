from tortoise import fields
from tortoise.models import Model


class Cars(Model):
    id = fields.IntField(pk=True)
    manufacturer = fields.ForeignKeyField("models.Manufacturers")
    website = fields.TextField()
    image = fields.TextField(null=True)
    make = fields.TextField()
    model = fields.TextField()
    year = fields.IntField()
    cargo = fields.FloatField()

    user = fields.ForeignKeyField("models.Users", related_name="cars", null=True)
    created_at = fields.DatetimeField(null=True, auto_now=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        table = "car"
