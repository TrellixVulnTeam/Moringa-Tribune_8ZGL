# Generated by Django 3.1.4 on 2021-01-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={},
        ),
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
