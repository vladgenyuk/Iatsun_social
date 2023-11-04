from django.db import models
from django.utils import timezone

from apps.accounts.models import UserAccount


def get_default_image() -> str:
    return 'default/no_image.png'


class Publication(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Publication title')
    content = models.TextField(null=True, blank=True, verbose_name='Publication content')
    published_at = models.DateTimeField(null=False, blank=False, default=timezone.now, verbose_name='Time created')
    updated_at = models.DateTimeField(null=False, blank=False, default=timezone.now, verbose_name='Time updated')
    image = models.ImageField(upload_to='blog/', default=get_default_image, verbose_name='Publication image')

    publisher = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name='Publication creator')

    def __str__(self):
        return f'{self.title}'

    # @property
    # def slug(self):
    #     return slugify(f"{self.pk}-{self.title}")
