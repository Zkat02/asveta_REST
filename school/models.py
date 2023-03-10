from django.db import models

DAY_WEEK_CHOICES = (
    ('monday', 'Понедельник'),
    ('tuesday ', 'Вторник'),
    ('wednesday ', 'Среда'),
    ('thursday ', 'Четверг'),
    ('friday ', 'Пятница'),
    ('saturday  ', 'Суббота'),
    ('sunday  ', 'воскресенье'),
)


class Student(models.Model):
    tg_id = models.IntegerField(default=0, verbose_name='id в телеге')
    name = models.CharField(max_length=30, verbose_name='прозвішча, імя')
    amount_courses = models.IntegerField(default=0, verbose_name='колькасць наведвальных курсаў')
    courses = models.ManyToManyField("Course", verbose_name="урок")
    email = models.EmailField(verbose_name="пошта", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вучань'
        verbose_name_plural = 'Вучнi'


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='прозвішча, імя')
    specialization = models.CharField(max_length=30, verbose_name='спецыялізацыя', blank=True)
    education = models.CharField(max_length=20, blank=True, verbose_name='адукацыя')
    work_experience = models.IntegerField(blank=True, verbose_name='стаж')
    amount_courses = models.IntegerField(default=0, verbose_name='колькасць курсаў')
    email = models.EmailField(verbose_name="пошта", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Настаўнік'
        verbose_name_plural = 'Настаўнікі'


class Course(models.Model):
    subject = models.CharField(max_length=20, verbose_name='прадмет')
    grade = models.IntegerField(default=0, verbose_name='клас')
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name='настаўнік')
    time_lesson = models.TimeField(verbose_name='час правядзення')
    amount_studens = models.IntegerField(default=0, verbose_name='колькасць вучаняў зараз')
    amount_places = models.IntegerField(default=5, verbose_name='ўсяго месц')
    is_full = models.BooleanField(default=False, verbose_name='запоўнены')
    day_week = models.CharField(max_length=10, choices=DAY_WEEK_CHOICES, default='monday')

    def __str__(self):
        return f"{self.subject} {self.grade} клас"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='назва')
    content = models.TextField(blank=True, verbose_name='тэкст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='створана')
    update_at = models.DateTimeField(auto_now=True, verbose_name='зменены')
    photo = models.ImageField(upload_to='site_pictures/%Y/%m/%d', verbose_name='фота', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='апублікавана')

    # tag = models.ForeignKey('Tag', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

# class Record(models.Model):
#     subject = models.CharField(max_length=20, verbose_name='прадмет')
#     grade = models.IntegerField(default=0, verbose_name='клас')
#     time_lesson = models.TimeField(verbose_name='час правядзення')
#     email = models.EmailField(verbose_name="пошта")
#     is_confirmed = models.BooleanField(default=False, verbose_name='пацверджана')
#
#     def __str__(self):
#         return self.pk
#
#     class Meta:
#         verbose_name = 'Запic на курс'
#         verbose_name_plural = 'Запicы на курсы'
