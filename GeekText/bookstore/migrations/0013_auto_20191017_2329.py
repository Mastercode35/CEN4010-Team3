# Generated by Django 2.2.6 on 2019-10-18 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0012_auto_20191017_2258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addresses',
            new_name='Address',
        ),
        migrations.RenameModel(
            old_name='CommentsRatings',
            new_name='CommentRating',
        ),
        migrations.RenameModel(
            old_name='CreditCards',
            new_name='CreditCard',
        ),
        migrations.RenameModel(
            old_name='Sales',
            new_name='Sale',
        ),
        migrations.RenameModel(
            old_name='SaleItems',
            new_name='SaleItem',
        ),
        migrations.RenameModel(
            old_name='WishListItems',
            new_name='WishListItem',
        ),
    ]
