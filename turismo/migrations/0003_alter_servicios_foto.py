# Generated by Django 5.0.6 on 2024-06-13 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0002_alter_servicios_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='turismo/media'),
        ),
    ]