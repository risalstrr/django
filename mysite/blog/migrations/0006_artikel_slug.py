# Generated by Django 4.0.3 on 2022-03-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_artikel_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
