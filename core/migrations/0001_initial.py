# Generated by Django 3.1.1 on 2020-09-20 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typevent', models.CharField(max_length=113)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ponente', models.CharField(max_length=133)),
                ('duracion', models.IntegerField()),
                ('anio', models.IntegerField(verbose_name='año')),
                ('img', models.ImageField(upload_to='upload/')),
                ('tipoevento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoevento')),
            ],
        ),
    ]
