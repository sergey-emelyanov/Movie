# Generated by Django 4.0.2 on 2022-08-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_remove_bookshop_budget_remove_bookshop_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshop',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
