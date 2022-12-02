# Generated by Django 4.1.3 on 2022-12-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_companycertificate_certificate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('order',), 'verbose_name': 'Contact ', 'verbose_name_plural': '9 Contacts'},
        ),
        migrations.AddField(
            model_name='partner',
            name='url',
            field=models.URLField(default=12, max_length=255, verbose_name='Link'),
            preserve_default=False,
        ),
    ]
