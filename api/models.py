from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Kol(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    kind = models.IntegerField()

    class Meta:
        verbose_name_plural = "حسابهای کل"

    def __str__(self):
        return self.name


class Moin(models.Model):
    kol = models.ForeignKey(Kol, related_name='moins',
                            on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    kind = models.IntegerField()

    class Meta:
        verbose_name_plural = "حسابهای معین"

    def __str__(self):
        return self.name


class Tafsili(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "حسابهای تفصیلی"

    def __str__(self):
        return self.name


class Sanad(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    note = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "اسناد حسابداری"

    def __str__(self):
        return self.note


class Artykl(models.Model):
    sanad = models.ForeignKey(
        Sanad, related_name='artykls', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    kol = models.ForeignKey(Kol, related_name='kols', on_delete=models.CASCADE)
    moin = models.ForeignKey(Moin, related_name='moins',
                             on_delete=models.CASCADE)
    taf1 = models.ForeignKey(
        Tafsili, related_name='taf1s', on_delete=models.CASCADE)
    taf2 = models.ForeignKey(
        Tafsili, related_name='taf2s', on_delete=models.CASCADE)
    taf3 = models.ForeignKey(
        Tafsili, related_name='taf3s', on_delete=models.CASCADE)
    bed = models.FloatField()
    bes = models.FloatField()
    note = models.CharField(max_length=1000)
    user = models.ForeignKey(User, related_name='users',
                             on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "آرتیکل های حسابداری"

    def __str__(self):
        return self.note
