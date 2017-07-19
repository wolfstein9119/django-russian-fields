# django-russian-fields

## Установка
После установки пакета необходимо добавить в INSTALLED_APPS
```python
INSTALLED_APPS = [                                  # Добавить 'russian-fields' в INSTALLED_APPS
    # ...
    'russian-fields',
    # ...
]
```

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

* **OGRNField** - ОГРН.
Поле имеет 3 режима работы (параметр mode): business (ИП), legal (ИНН юр.лица), general (общий ОГРН, по умолчанию)
Наследуется от CharField. Поле включает в себя проверку на минимальную и максимальную длину.
Дополнительно встроена проверка на контроль содержимого - допускаются только цифры и введенный ОГРН должен удовлетворять своему контрольному числу.
Значение поля представляет собой объект класса OGRN(str).
Объект класса OGRN(str) содержит следующие свойства:
    * feature - признак отнесения государственного регистрационного номера записи
    * year - код инспекции
    * region_code - порядковый номер субъекта РФ
    * inspection_code - код налоговой инспекции
    * record_number - номер записи, внесенной в государственный реестр в течение года
    * control_number - контрольное число

Пример использования
```python
...
from russian_fields import OGRNField, OGRNBusinessField, OGRNLegalField
...


class Sample3Model(models.Model):
    ...
    ogrn = OGRNField(
        mode='general',
        blank=True, null=True
    )
    ogrn_legal = OGRNLegalField(
        blank=True, null=True
    )
    ogrn_business = OGRNBusinessField(
        blank=True, null=True
    )
    ...

s3m = Sample3Model.objects.get(id=some_id)
print(
    s3m.ogrn.feature,
    s3m.ogrn.year,
    s3m.ogrn.region_code,
    s3m.ogrn.inspection_code,
    s3m.ogrn.record_number,
    s3m.ogrn.control_number
)
```

* **OGRNBusinessField** - ОГРНИН (эквивалентен OGRNField(mode='business')).

* **OGRNLegalField** - ИНН юр.лица (эквивалентен OGRNField(mode='legal')).

* **OKOGUField** - код общероссийского классификатора органов гос.власти.
Наследуется от CharField. Поле включает в себя проверку на минимальную и максимальную длину (7 символов).
Дополнительно встроена проверка на контроль содержимого - допускаются только цифры.

Пример использования
```python
...
from russian_fields import OKOGUField
...


class Sample4Model(models.Model):
    ...
    okogu = OKOGUField(
        blank=True, null=True
    )
    ...
```

* **OKOPFField** - код общероссийского классификатора организационной-правовых форм.
Наследуется от CharField. Поле включает в себя проверку на минимальную и максимальную длину (5 символов).
Дополнительно встроена проверка на контроль содержимого - допускаются только цифры.

Пример использования
```python
...
from russian_fields import OKOPFField
...


class Sample4Model(models.Model):
    ...
    okopf = OKOPFField(
        blank=True, null=True
    )
    ...
```