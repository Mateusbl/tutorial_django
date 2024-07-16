from datetime import date

from django.db import models


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(verbose_name="data de entrega", null=False, blank=False)
    finished_at = models.DateField(null=True)

    def mark_as_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()


class Meta:
    ordering = ["deadline"]


# Create your models here.
