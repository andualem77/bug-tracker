# Generated by Django 4.2.3 on 2023-07-06 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_alter_ticket_priority_alter_ticket_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='attachments',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=40),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type',
            field=models.CharField(choices=[('Bugs/Errors', 'Bugs/Errors'), ('Feature request', 'Feature Request'), ('Other Comments', 'Other Comments'), ('Traning/documents request', 'Traning/documents Request')], max_length=40),
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='attachments/')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
    ]
