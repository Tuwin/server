# Generated by Django 3.0.3 on 2020-06-24 07:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_etebase', '0017_auto_20200623_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionitem',
            name='uid',
            field=models.CharField(db_index=True, max_length=43, validators=[django.core.validators.RegexValidator(message='Not a valid UID', regex='^[a-zA-Z0-9\\-_]*$')]),
        ),
    ]
