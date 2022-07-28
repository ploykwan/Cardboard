#
#   Standard imports
#
from django.contrib.auth.models import User
from django.db import models


#
#   Classes
#

class Card(models.Model):
    DO_FIRST = 'Do first'
    SCHEDULE = 'Schedule'
    DELEGATE = 'Delegate'
    DONT_DO = "Don't do"

    CATEGORY_CHOICES = [
        (DO_FIRST, 'Do first'),
        (SCHEDULE, 'Schedule'),
        (DELEGATE, 'Delegate'),
        (DONT_DO, "Don't do")
    ]

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_author')
    created_at = models.DateTimeField(auto_now_add=True)

    list_display = ('title', 'author', 'created_at',)
    get_queryset = ('title', 'author', 'description',)

    class Meta:
        db_table = 'board_card'
        verbose_name_plural = 'Card'

    def __str__(self):
        return f'[{self.author}] {self.title}'