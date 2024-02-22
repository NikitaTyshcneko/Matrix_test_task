from django.contrib.postgres.fields import ArrayField
from django.db import models


class Matrix(models.Model):
    matrix_data = ArrayField(
        ArrayField(models.IntegerField(), null=False),
        null=False,
    )
