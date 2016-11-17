# django-russian-fields

## Описание
Данная библиотека включает в себя описание и работу следующих полей:

* GENDERField - пол человека (наследуется от CharField, с предопределенным набором choice

Пример:
```python
class SampleModel(models.Model):
    ...
    gender = GENDERField(
        blank=True, null=True
    )
    ...
```