# Generated by Django 3.0.5 on 2020-04-09 08:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0004_auto_20200409_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_version',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='booktype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.booktype'),
        ),
        migrations.AlterField(
            model_name='books',
            name='publish_year',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 8, 21, 11, 188830, tzinfo=utc)),
        ),
    ]
