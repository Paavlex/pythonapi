# Generated by Django 3.2.3 on 2021-05-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=40)),
                ('cvss_score', models.CharField(default='-', max_length=3)),
                ('cvss_vector', models.CharField(default='-', max_length=110)),
                ('owasp_score', models.CharField(default='-', max_length=7)),
                ('date', models.CharField(default='-', max_length=10)),
            ],
        ),
    ]
