# Generated by Django 3.1.2 on 2020-12-07 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perpusapp', '0002_auto_20201207_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=10)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='buku',
            name='kelas_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perpusapp.kelas'),
        ),
    ]