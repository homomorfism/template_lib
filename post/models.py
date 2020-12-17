from django.db import models

# Create your models here.
from category.models import Category


class Post(models.Model):
    temp_summary = "Lorem ipsum Sed eiusmod esse aliqua sed incididunt aliqua incididunt mollit id et sit proident " \
                   "dolor nulla sed commodo est ad minim elit reprehenderit nisi officia aute incididunt velit sint " \
                   "in aliqua cillum in consequat consequat in culpa in anim. "
    who_added = models.CharField(max_length=20, help_text="Username who added material", null=False, )

    date_publication = models.DateTimeField(help_text='Date and time for uploading', null=False)

    image_preview_small = models.ImageField(help_text="Preview image (small)",
                                            default='home/static/home/images/thumbs/masonry/rucksack-600.jpg')
    image_preview_big = models.ImageField(help_text="Preview image (big)",
                                          default='home/static/home/images/thumbs/masonry/rucksack-1200.jpg')

    title = models.CharField(max_length=100, help_text="Enter title of material", null=False)
    author = models.CharField(max_length=100, help_text="Enter author of material", null=False)

    description = models.CharField(max_length=200, help_text="Enter description of book", default=temp_summary)

    categories = models.ManyToManyField(to=Category, help_text="Choose tags for book")

    attachments = models.ManyToManyField(to='MyFileField', help_text='Choose attachments to post')

    # In the future add state 'deleted'
    states = [
        ('0', 'Invisible'),
        ('1', 'Approved'),
        ('2', 'Declined'),
    ]

    visibility = models.CharField(max_length=1, choices=states, default='0', help_text="Current state of material")

    def __str__(self):
        return self.title

    # Sorting in admin panel
    class Meta:
        ordering = ['title', '-date_publication', ]


class MyFileField(models.Model):
    file = models.FileField(upload_to='media/', help_text="Upload file with material", null=False)
