# Generated by Django 4.1.5 on 2023-01-27 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"verbose_name": "Курс", "verbose_name_plural": "Курсы"},
        ),
        migrations.AlterModelOptions(
            name="student",
            options={"verbose_name": "Вучань", "verbose_name_plural": "Вучнi"},
        ),
        migrations.AlterModelOptions(
            name="teacher",
            options={"verbose_name": "Настаўнік", "verbose_name_plural": "Настаўнікі"},
        ),
        migrations.AddField(
            model_name="teacher",
            name="specialization",
            field=models.CharField(
                blank=True, max_length=30, verbose_name="спецыялізацыя"
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="grade",
            field=models.IntegerField(default=0, verbose_name="клас"),
        ),
        migrations.AlterField(
            model_name="course",
            name="subject",
            field=models.CharField(max_length=20, verbose_name="прадмет"),
        ),
        migrations.AlterField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="school.teacher",
                verbose_name="настаўнік",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="time_lesson",
            field=models.TimeField(verbose_name="час правядзення"),
        ),
        migrations.AlterField(
            model_name="student",
            name="amount_courses",
            field=models.IntegerField(
                default=0, verbose_name="колькасць наведвальных курсаў"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(to="school.course", verbose_name="урок"),
        ),
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(max_length=30, verbose_name="прозвішча, імя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="amount_courses",
            field=models.IntegerField(default=0, verbose_name="колькасць курсаў"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="education",
            field=models.CharField(blank=True, max_length=20, verbose_name="адукацыя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="name",
            field=models.CharField(max_length=30, verbose_name="прозвішча, імя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="work_experience",
            field=models.IntegerField(blank=True, verbose_name="стаж"),
        ),
    ]