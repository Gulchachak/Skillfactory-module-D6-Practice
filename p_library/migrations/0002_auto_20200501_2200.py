# Generated by Django 2.2.6 on 2020-05-02 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=128),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_name', models.CharField(max_length=60)),
                ('friend_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='redaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Redaction'),
        ),
    ]
