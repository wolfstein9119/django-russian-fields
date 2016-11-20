# django-russian-fields

## Описание
Данная библиотека включает в себя описание и работу следующих полей:

* **GENDERField** - пол человека (наследуется от CharField, с предопределенным набором choice **M/F** )

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

* **AgencyTypeESIA** - тип ОГВ (органа государственной власти) согласно методической рекомендации работы с ЕСИА.
Наследуется от CharField с предопределенным набором choice **10.FED / 30.FND / 11.REG / 12.LCL / 20.GOV / 21.MCL**

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

* **TerritoryCodeField** - код субъекта РФ.
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

* **INNField** - ИНН.
Поле имеет 3 режима работы (параметр mode): person (ИНН физ.лица), legal (ИНН юр.лица), general (общий ИНН, по умолчанию)
Наследуется от CharField. Поле включает в себя проверку на минимальную и максимальную длину.
Дополнительно встроена проверка на контроль содержимого - допускаются только цифры и введенный ИНН должен удовлетворять своему контрольному числу.
Значение поля представляет собой объект класса INN(str).
Объект класса INN(str) содержит следующие свойства:
    * region_code - кода региона
    * inspection_code - код инспекции
    * record_number - номер записи
    * control_number - контрольное число

Пример использования
```python
...
from russian_fields import INNField, INNPersonField, INNBusinessField
...


class Sample2Model(models.Model):
    ...
    inn = INNField(
        mode='general',
        blank=True, null=True
    )
    inn_person = INNPersonField(
        blank=True, null=True
    )
    inn_business = INNBusinessField(
        blank=True, null=True
    )
    ...

s2m = Sample2Model.objects.get(id=some_id)
print(
    s2m.inn.region_code,
    s2m.inn.inspection_code,
    s2m.inn.record_number,
    s2m.inn.control_number
)
```

* **INNPersonField** - ИНН физ.лица (эквивалентен INNField(mode='person')).

* **INNBusinessField** - ИНН юр.лица (эквивалентен INNField(mode='legal')).

* **KPPField** - КПП.
Наследуется от CharField. Поле включает в себя проверку на минимальную и максимальную длину.
Значение поля представляет собой объект класса KPP(str).
Объект класса KPP(str) содержит следующие свойства:
    * inspection_code - код инспекции
    * cause - причина постановка на учет
    * record_number - номер записи

Пример использования:
```python
...
from russian_fields import KPPField
...


class Sample2Model(models.Model):
    ...
    kpp = KPPField(
        blank=True, null=True
    )
    ...

s2m = Sample2Model.objects.get(id=some_id)
print(
    s2m.kpp.inspection_code,
    s2m.kpp.cause,
    s2m.kpp.record_number
)
```
