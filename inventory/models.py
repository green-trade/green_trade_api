from django.db import models

import uuid


class Base(models.Model):

    # make the primary key an uuid, helps with sec and no clash
    id = models.UUIDField(
            default=uuid.uuid4(), editable=False, primary_key=True)

    # an auto crate and update time feadls
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    # so django doesn't make this class in to a database row
    class Meta:
        abstract = True


class Inventory(Base):
    name = models.CharField(max_length=256)
    provider = models.CharField(max_length=256)
    thc_percent = models.IntegerField()
    cbd_percent = models.IntegerField()
