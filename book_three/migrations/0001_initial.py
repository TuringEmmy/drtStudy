# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-21 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20, verbose_name='标题')),
                ('bpub_date', models.DateField(verbose_name='出版日期')),
                ('bread', models.IntegerField(default=0, verbose_name='阅读量')),
                ('bcomment', models.IntegerField(default=0, verbose_name='评论量')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image', models.ImageField(null=True, upload_to='booktest', verbose_name='封面图片')),
            ],
            options={
                'verbose_name': '图书',
                'db_table': 'tb_books',
                'verbose_name_plural': '图书',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20, verbose_name='名称')),
                ('hgender', models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('hcomment', models.CharField(max_length=200, null=True, verbose_name='备注信息')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_three.BookInfo', verbose_name='所属图书')),
            ],
            options={
                'verbose_name': '英雄',
                'db_table': 'tb_heros',
                'verbose_name_plural': '英雄',
            },
        ),
    ]
