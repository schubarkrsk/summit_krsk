from django import forms

SEX_CHOICE = [
    ("male", "Мужской"),
    ("female", "Женский")
]

TABLE_CHOISE = [
    ("none", "Не бронировать стол"),
    ("small", "Стол на 4 персоны (+2000 руб.)"),
    ("big", "Стол на 8 персон (+5000 руб.)")
]

class Order(forms.Form):
    familiya = forms.CharField(label="Фамилия", max_length=50)
    imya = forms.CharField(label="Имя", max_length=50)
    phone_number = forms.CharField(label="Контактный телефон", max_length=12)
    age = forms.IntegerField(label="Ваш возраст", initial=18)
    sex = forms.ChoiceField(label="Пол", choices=SEX_CHOICE)
    table = forms.ChoiceField(label="Бронь стола", choices=TABLE_CHOISE)
    instagram = forms.CharField(label="Ссылка на ваш Instagram", max_length=150)
