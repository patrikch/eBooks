# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('ebookfilename', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100, blank=True)),
                ('publisher', models.CharField(max_length=50, blank=True)),
                ('format', models.CharField(max_length=5)),
                ('pubYear', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('key', models.CharField(max_length=20)),
                ('parent', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='keys',
            field=models.ManyToManyField(to='books.Key'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dvd', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='location',
            field=models.ForeignKey(to='books.Location'),
            preserve_default=True,
        ),
    ]
