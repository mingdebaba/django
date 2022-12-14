# Generated by Django 4.1.2 on 2022-10-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schoolworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classify', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='')),
                ('difficulty', models.CharField(choices=[('简单', '简单'), ('一般', '一般'), ('难', '难')], max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('study_quality', models.CharField(choices=[('好', '好'), ('一般', '一般'), ('不好', '不好')], max_length=100)),
            ],
        ),
    ]
