from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class Room(BaseModel):
    room = models.CharField(max_length=100, default="Double Room", choices=(("Single Room", "Single Room"),
                        ("Double Room", "Double Room"), ("Suite Room", "Suite Room")))
    slug = models.SlugField(unique=True, null=True, blank=True)
    room_area = models.CharField(max_length=100)
    number_of_guests = models.IntegerField()
    price = models.IntegerField()
    connecting_rooms = models.IntegerField()
    no_of_bed = models.CharField(max_length=100)
    description = models.TextField()
    tag = models.CharField(max_length=100, null=True, blank=True, choices=(("Best Seller", "Best Seller"),
                        ("Popular", "Popular")))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.room)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.room


class RoomImage(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_images")
    image = models.ImageField(upload_to="room")