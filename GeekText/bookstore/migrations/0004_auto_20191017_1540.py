# Generated by Django 2.2.5 on 2019-10-17 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20191017_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wrote',
            old_name='Book_id',
            new_name='book_id',
        ),
    ]