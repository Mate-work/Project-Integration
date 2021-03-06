# Generated by Django 3.0.8 on 2020-07-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='opportunities',
            field=models.ManyToManyField(blank=True, to='person.Opportunity'),
        ),
        migrations.AlterField(
            model_name='person',
            name='skills',
            field=models.ManyToManyField(blank=True, to='person.Skill'),
        ),
        migrations.AlterField(
            model_name='person',
            name='type',
            field=models.TextField(choices=[('S', 'Student'), ('p', 'Professional'), ('Z', 'Organization'), ('O', 'Others')]),
        ),
    ]
