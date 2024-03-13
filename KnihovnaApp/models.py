from django.db import models
from django.utils import timezone
from datetime import timedelta


class Knihovna(models.Model):
    aboniment = models.CharField(max_length=256)
    nazev_knihy = models.CharField(max_length=256)
    zapujceno = models.DateField(auto_now_add=True)
    vraceno = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.zapujceno:
            due_date = self.zapujceno + timedelta(weeks=4)
            if timezone.now().date() >= due_date:
                self.send_notification()
        super().save(*args, **kwargs)


    def send_notification(self):
        print(f"Upozorneni: Je cas vratit knihu '{self.nazev_knihy}")