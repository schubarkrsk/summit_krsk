from django.db import models


# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    familiya = models.CharField(help_text="Фамилия", max_length=50)
    imya = models.CharField(help_text="Имя", max_length=50)
    phone_number = models.CharField(help_text="Телефон", max_length=12)
    age = models.IntegerField(help_text="Возраст")
    sex = models.CharField(help_text="Пол", max_length=10)
    table = models.CharField(help_text="Бронь стола", max_length=50)
    instagram = models.CharField(max_length=150)
    is_accepted = models.BooleanField(help_text="Допущен")
    is_pay = models.BooleanField(help_text="Оплачен")
    cost = models.IntegerField(help_text="Сумма")

    class Meta:
        verbose_name = "Заявки на бронь"

    def __str__(self):
        return f"{self.familiya} {self.imya} / {self.sex} {self.age} / {self.phone_number} {self.instagram} / {self.table}\n" \
               f"ДОПУЩЕН: {self.is_accepted} / ОПЛАЧЕН: {self.is_pay} / Сумма: {self.cost}"
