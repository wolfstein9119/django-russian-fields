# django-russian-fields

## Описание
Данная библиотека включает в себя описание и работу следующих полей:

* GENDERField - пол человека (наследуется от CharField, с предопределенным набором choice)

Пример использования:
```python
...
from russian_fields import GENDERField
...


class SampleModel(models.Model):
    ...
    gender = GENDERField(
        blank=True, null=True
    )
    ...
```

* AgencyTypeESIA - тип ОГВ (органа государственной власти) согласно методической рекомендации работы с ЕСИА.
Наследуется от CharField с предопределенным набором choice

Пример использования:
```python
...
from russian_fields import AgencyTypeESIA
...


class SampleModel(models.Model):
    ...
    gender = AgencyTypeESIA(
        blank=True, null=True
    )
    ...
```