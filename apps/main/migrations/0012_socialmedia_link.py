# Generated by Django 4.1.3 on 2022-12-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_contact_options_partner_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='link',
            field=models.URLField(default=1, max_length=255, verbose_name='link'),
            preserve_default=False,
        ),
    ]
