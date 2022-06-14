# Generated by Django 4.0.4 on 2022-06-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book1',
            name='book available',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='book1',
            name='reader',
        ),
        migrations.AddField(
            model_name='book1',
            name='reader',
            field=models.ManyToManyField(related_name='reader', to='library_app.reader'),
        ),
    ]