# Generated by Django 3.2.9 on 2021-11-30 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0006_auto_20211123_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='billmodel',
            name='bill_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('in_review', 'In Review'), ('approved', 'Approved'), ('canceled', 'Canceled')], default='draft', max_length=10, verbose_name='Bill Status'),
        ),
        migrations.AddField(
            model_name='billmodel',
            name='markdown_notes',
            field=models.TextField(blank=True, null=True, verbose_name='Markdown Notes'),
        ),
        migrations.AddField(
            model_name='invoicemodel',
            name='markdown_notes',
            field=models.TextField(blank=True, null=True, verbose_name='Markdown Notes'),
        ),
        migrations.AlterField(
            model_name='invoicemodel',
            name='invoice_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('in_review', 'In Review'), ('approved', 'Approved'), ('canceled', 'Canceled')], default='draft', max_length=10, verbose_name='Invoice Status'),
        ),
    ]
