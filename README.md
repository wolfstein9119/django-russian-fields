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
    agency_type_esia = AgencyTypeESIA(
        blank=True, null=True
    )
    ...
```

* TerritoryCodeField - код субъекта РФ.
Наследуется от CharField. Поле включает в себя проверку на минимальную и максимальную длину (2 символа).
Дополнительно встроена проверка на контроль содержимого - допускаются только цифры.

Пример использования
```python
...
from russian_fields import TerritoryCodeField
...


class SampleModel(models.Model):
    ...
    territory_code = TerritoryCodeField(
        blank=True, null=True
    )
    ...
```