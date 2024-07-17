# Generated by Django 5.0.6 on 2024-07-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('receipt_image', models.ImageField(blank=True, null=True, upload_to='receipts/')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='invoice',
            name='balance_due',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='invoice',
            name='template',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
