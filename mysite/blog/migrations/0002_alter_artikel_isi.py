# Generated by Django 4.0.3 on 2022-03-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
