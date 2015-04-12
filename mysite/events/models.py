from django.db import models


class NameRepresentation:

    def __str__(self):
        return self.name


class Place(NameRepresentation, models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)


class EventType(NameRepresentation, models.Model):
    name = models.CharField(max_length=120)


class Event(NameRepresentation, models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120, blank=True)
    date = models.DateField()
    type = models.ForeignKey(EventType)
    place = models.ManyToManyField(Place)
