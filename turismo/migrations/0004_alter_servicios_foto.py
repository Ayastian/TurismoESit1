# Generated by Django 5.0.6 on 2024-06-13 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0003_alter_servicios_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='servicios'),
        ),
    ]