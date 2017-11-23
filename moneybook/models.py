from django.db import models
from django.conf import settings

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = "".join(arr)
    extension = filename.split('.')[-1]
    return '{}/{}.{}'.format(instance.contents, pid, extension)


class Moneybook(models.Model):
    receipt_image = models.ImageField(upload_to=user_path)
    payment_date = models.DateTimeField()
    pub_date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=100)
    contents = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    etc = models.TextField(default=None)
    is_expense = models.BooleanField(default=True)
    
    def __str__(self):
        return "{} / {}".format(self.payment_date, self.contents)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('moneybook:detail', kwargs={'pk': self.pk})