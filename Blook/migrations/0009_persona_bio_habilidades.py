# Generated by Django 3.0.1 on 2021-09-06 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blook', '0008_persona_bio_educacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='bio_Habilidades',
            field=models.TextField(null=True),
        ),
    ]
