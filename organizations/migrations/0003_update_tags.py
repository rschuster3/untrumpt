# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 20:27
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_import_organization_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='organization',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(b'women', b"Women's Rights"), (b'racial_minorities', b'Rights of Racial Minorities'), (b'religious_minorities', b'Rights of Religious Minorities'), (b'immigrants', b"Immigrants' Rights"), (b'youths', b'Helping Kids'), (b'disabled', b'Rights of the Disabled'), (b'environment', b'The Environment'), (b'civil_rights', b'Civil Rights'), (b'sexual_abuse', b'Protecting from Sexual Abuse'), (b'lgbt', b'LGBT Rights'), (b'reproduction', b'Reproductive Rights'), (b'homeless', b'Homelessness'), (b'guns', b'Gun Laws'), (b'drugs', b'Drug Laws')], max_length=147),
        ),
    ]
