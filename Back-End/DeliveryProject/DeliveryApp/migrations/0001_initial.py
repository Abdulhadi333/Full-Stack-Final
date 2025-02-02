# Generated by Django 4.0.6 on 2022-07-23 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewDelegate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('PhoneNumber', models.IntegerField(max_length=10)),
                ('IdNumber', models.IntegerField(max_length=10)),
                ('PersonalImage', models.URLField()),
                ('CarInfo', models.TextField(max_length=200)),
                ('CarImage', models.URLField()),
                ('DrivingLicense', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('4', 'excellent'), ('3 ', 'very good'), ('2', 'good'), ('1', 'bad')], max_length=250)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DeliveryApp.newdelegate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PackageType', models.CharField(choices=[('طرد صغير', 'طرد صغير'), ('طرد متوسط', 'طرد متوسط'), ('طرد كبير', 'طرد كبير')], max_length=50)),
                ('FromWhichCity', models.CharField(choices=[('الرياض', 'الرياض'), ('مكة', 'مكة'), ('الدمام', 'الدمام'), ('جدة', 'جدة'), ('المدينة', 'المدينة'), ('أبها', 'أبها'), ('القصيم', 'القصيم'), ('الاحساء', 'الاحساء'), ('أبها', 'أبها'), ('جازان', 'جازان'), ('تبوك', 'تبوك'), ('نجران', 'نجران'), ('حائل', 'حائل'), ('الحدود الشماليه', 'الحدود الشماليه')], max_length=50)),
                ('ToWhichCity', models.CharField(choices=[('الرياض', 'الرياض'), ('مكة', 'مكة'), ('الدمام', 'الدمام'), ('جدة', 'جدة'), ('المدينة', 'المدينة'), ('أبها', 'أبها'), ('القصيم', 'القصيم'), ('الاحساء', 'الاحساء'), ('أبها', 'أبها'), ('جازان', 'جازان'), ('تبوك', 'تبوك'), ('نجران', 'نجران'), ('حائل', 'حائل'), ('الحدود الشماليه', 'الحدود الشماليه')], max_length=50)),
                ('DeliveryTime', models.CharField(choices=[('0-5h', ' 0-5h'), ('6-12h', '6-12h'), ('+12h', '+12h')], max_length=50)),
                ('Description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('4', 'excellent'), ('3 ', 'very good'), ('2', 'good'), ('1', 'bad')], max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
