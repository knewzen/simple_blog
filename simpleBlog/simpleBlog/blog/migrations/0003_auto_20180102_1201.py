# Generated by Django 2.0 on 2018-01-02 12:01

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180102_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=froala_editor.fields.FroalaField(),
        ),
    ]