from tortoise import fields
from tortoise.models import Model


class Manufacturers(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    website = fields.TextField()

    class Meta:
        table = "manufacturer"
