# Generated by Django 4.0.4 on 2022-06-09 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Book1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofbook', models.CharField(max_length=120)),
                ('book available', models.BooleanField(default=True)),
                ('author', models.ManyToManyField(related_name='author', to='library_app.author1')),
                ('reader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reader', to='library_app.reader')),
            ],
            options={
                'ordering': ['nameofbook'],
            },
        ),
    ]
