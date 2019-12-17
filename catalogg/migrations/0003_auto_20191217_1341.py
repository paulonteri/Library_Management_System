# Generated by Django 3.0 on 2019-12-17 10:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogg', '0002_auto_20191217_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('18ea1b07-28f6-43c8-be10-dce04d102f42'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
