# Generated by Django 4.2.6 on 2023-10-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_bookmark', '0006_remove_bookmark_gambar_alter_bookmark_buku'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='gambar',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='judul',
            field=models.CharField(default='default', max_length=100),
        ),
    ]