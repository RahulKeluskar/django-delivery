from django.db import models

class Restaurant(models.Model):
    """
    Information about restaurants.
    """

    PRICE_CHOICES = (
        (1, '$'),
        (2, '$$'),
        (3, '$$$'),
        (4, '$$$$')
    )

    CUISINE_CHOICES = (
        ('IND', 'Indian'),
        ('CHI', 'Chinese'),
        ('USA', 'American'),
        ('JPN', 'Japanese'),
        ('THL', 'Thai'),
        ('KHM', 'Khmer'),
        ('VNM', 'Vietnamese'),
        ('ITL', 'Italian'),
        ('MEX', 'Mexican')
    )

    name = models.CharField(max_length=300)
    address = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    cuisine = models.CharField(max_length=100, 
        choices=CUISINE_CHOICES, blank=True, default='')
    price = models.SmallIntegerField(choices=PRICE_CHOICES, null=True)
    delivers = models.BooleanField(default=True)
    site_url = models.URLField(default=500)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class MenuItem(models.Model):
    """A list of different items available on the menu of 
    each restaurant"""

    TIMES = (
        (1, 'All day'),
        (2, 'Breakfast'),
        (3, 'Lunch'),
        (4, 'Dinner'),
        (5, 'Kids menu')
    )

    restaurant = models.ForeignKey(Restaurant, related_name='menu_item')
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.SmallIntegerField(choices=TIMES, default=1)

    def __unicode__(self):
        return self.title

class OpenHours(models.Model):
    """
    The hours when each restaurant is open each day.
    """

    DAYS = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday')
    )

    HOURS = [(i, i) for i in range(1, 25)]

    restaurant = models.ForeignKey(Restaurant, related_name='open_hours')
    from_hour = models.SmallIntegerField(choices=HOURS, null=True)
    to_hour = models.SmallIntegerField(choices=HOURS, null=True)
    day = models.SmallIntegerField(choices=DAYS, null=True)


