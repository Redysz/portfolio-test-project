# Generated by Django 3.0.2 on 2020-03-24 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200324_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='second_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translation_second_title', to='projects.Translation'),
        ),
    ]
