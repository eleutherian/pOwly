# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('sequence', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=16384)),
                ('parent_chapter', models.ForeignKey(to='tutorial.Chapter')),
            ],
            options={
                'ordering': ('parent_chapter', 'sequence', 'tutorial'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=2048)),
                ('date_created', models.DateTimeField(verbose_name='date_created')),
                ('date_modified', models.DateTimeField(verbose_name='date_modified')),
                ('upvotes', models.IntegerField(default=1)),
                ('downvotes', models.IntegerField(default=0)),
                ('is_public', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('isPositive', models.BooleanField(default=True)),
                ('tutorial', models.ForeignKey(to='tutorial.Tutorial')),
                ('user', models.ForeignKey(to='tutorial.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='author',
            field=models.ForeignKey(to='tutorial.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chapter',
            name='tutorial',
            field=models.ForeignKey(to='tutorial.Tutorial'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('sequence', 'tutorial', 'parent_chapter')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='chapter',
            order_with_respect_to='parent_chapter',
        ),
    ]
