# Generated by Django 4.1.1 on 2022-10-01 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=265)),
                ('status', models.CharField(choices=[('Initial', 'Initial'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Completed', 'Completed')], default='Initial', max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
                ('due_by', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
