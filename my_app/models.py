from django.db import models


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    mouths_to_learn = models.IntegerField()


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Student(AbstractPerson):
    WINDOWS = 'windows'
    MACOS = 'macos'
    LINUX = 'linux'
    pc_choices = [
        ('WINDOWS', 'windows'),
        ('MACOS', 'macos'),
        ('LINUX', 'linux'),
    ]
    work_study_place = models.CharField(max_length=100, null=True)
    has_own_notebook = models.BooleanField(max_length=100)
    preferred_os = models.CharField(max_length=10, choices=pc_choices, default=WINDOWS)


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=100, null=True)
    experience = models.DateField()
    courses = models.ManyToManyField(Student, through='Course')




class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    data_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


