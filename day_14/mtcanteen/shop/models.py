from django.db import models

CATEGORY_CHOICES = [
    ('bakery', 'Bakery'),
    ('mess_breakfast', 'Mess - Breakfast'),
    ('mess_lunch', 'Mess - Lunch'),
    ('mess_dinner', 'Mess - Dinner'),
    ('canteen_breakfast', 'Canteen - Breakfast'),
    ('canteen_lunch', 'Canteen - Lunch'),
    ('canteen_dinner', 'Canteen - Dinner'),
]

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"
