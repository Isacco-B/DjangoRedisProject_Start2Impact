from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Article_detail", kwargs={"pk": self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

