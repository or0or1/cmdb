# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4e3b\u673aIP')),
                ('other_ip', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u5176\u4ed6IP')),
                ('hostname', models.CharField(max_length=128, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('port', models.IntegerField(blank=True, null=True, verbose_name='\u7aef\u53e3\u53f7')),
                ('username', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u7ba1\u7406\u7528\u6237\u540d')),
                ('password', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5bc6\u7801')),
                ('use_default_auth', models.BooleanField(default=True, verbose_name='\u4f7f\u7528\u9ed8\u8ba4\u7ba1\u7406\u8d26\u53f7')),
                ('mac', models.CharField(blank=True, max_length=20, null=True, verbose_name='MAC\u5730\u5740')),
                ('remote_ip', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u8fdc\u63a7\u5361IP')),
                ('brand', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u786c\u4ef6\u5382\u5546\u578b\u53f7')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5185\u5b58')),
                ('disk', models.CharField(blank=True, max_length=1024, null=True, verbose_name='\u786c\u76d8')),
                ('system_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7cfb\u7edf\u7c7b\u578b')),
                ('system_version', models.CharField(blank=True, max_length=8, null=True, verbose_name='\u7cfb\u7edf\u7248\u672c\u53f7')),
                ('system_arch', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u7cfb\u7edf\u5e73\u53f0')),
                ('cabinet', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u673a\u67dc\u53f7')),
                ('position', models.IntegerField(blank=True, null=True, verbose_name='\u673a\u5668\u4f4d\u7f6e')),
                ('number', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u8d44\u4ea7\u7f16\u53f7')),
                ('status', models.IntegerField(blank=True, choices=[(1, '\u5df2\u4f7f\u7528'), (2, '\u672a\u4f7f\u7528'), (3, '\u62a5\u5e9f')], default=1, null=True, verbose_name='\u673a\u5668\u72b6\u6001')),
                ('asset_type', models.IntegerField(blank=True, choices=[(1, '\u7269\u7406\u673a'), (2, '\u865a\u62df\u673a'), (3, '\u4ea4\u6362\u673a'), (4, '\u8def\u7531\u5668'), (5, '\u9632\u706b\u5899'), (6, 'Docker'), (7, '\u5176\u4ed6')], null=True, verbose_name='\u4e3b\u673a\u7c7b\u578b')),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN\u7f16\u53f7')),
                ('date_added', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6fc0\u6d3b')),
                ('comment', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('comment', models.CharField(blank=True, max_length=160, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssetRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('alert_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='goconf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('repo', models.CharField(max_length=128)),
                ('localpath', models.CharField(max_length=64)),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
            ],
        ),
        migrations.CreateModel(
            name='gogroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='go group name')),
            ],
        ),
        migrations.CreateModel(
            name='goservices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=32, verbose_name='goservices services name')),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.gogroup')),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('bandwidth', models.CharField(blank=True, default=b'', max_length=32, null=True, verbose_name='\u673a\u623f\u5e26\u5bbd')),
                ('linkman', models.CharField(blank=True, default=b'', max_length=16, null=True, verbose_name='\u8054\u7cfb\u4eba')),
                ('phone', models.CharField(blank=True, default=b'', max_length=32, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('address', models.CharField(blank=True, default=b'', max_length=128, null=True, verbose_name='\u673a\u623f\u5730\u5740')),
                ('network', models.TextField(blank=True, default=b'', null=True, verbose_name='IP\u5730\u5740\u6bb5')),
                ('date_added', models.DateField(auto_now=True, null=True)),
                ('operator', models.CharField(blank=True, default=b'', max_length=32, null=True, verbose_name='\u8fd0\u8425\u5546')),
                ('comment', models.CharField(blank=True, default=b'', max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': 'IDC\u673a\u623f',
                'verbose_name_plural': 'IDC\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='minion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saltname', models.CharField(max_length=32, verbose_name='salt minion name')),
		('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='svn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('repo', models.CharField(max_length=128)),
                ('localpath', models.CharField(max_length=64)),
                ('movepath', models.CharField(max_length=64)),
                ('revertpath', models.CharField(max_length=64)),
                ('executefile', models.CharField(max_length=64)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.gogroup')),
            ],
        ),
        migrations.AddField(
            model_name='goservices',
            name='saltminion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.minion'),
        ),
        migrations.AddField(
            model_name='goconf',
            name='hostname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.minion'),
        ),
        migrations.AddField(
            model_name='goconf',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.gogroup'),
        ),
        migrations.AddField(
            model_name='asset',
            name='group',
            field=models.ManyToManyField(blank=True, to='asset.AssetGroup', verbose_name='\u6240\u5c5e\u4e3b\u673a\u7ec4'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.IDC', verbose_name='\u673a\u623f'),
        ),
    ]
