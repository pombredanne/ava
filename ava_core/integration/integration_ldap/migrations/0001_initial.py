# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('integration_abstract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LDAPIntegrationAdapter',
            fields=[
                ('integrationadapter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='integration_abstract.IntegrationAdapter')),
                ('dump_dn', models.CharField(max_length=100, verbose_name='Domain')),
                ('server', models.CharField(max_length=100, verbose_name='Server')),
                ('salt', models.CharField(max_length=100)),
                ('ldap_password', models.CharField(max_length=100)),
                ('ldap_user', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('integration_abstract.integrationadapter',),
        ),
    ]
