import datetime

from my_app.models import *
lang = Language.objects.create(name='Python', mouths_to_learn=6)
lang2 = Language.objects.create(name='Java Script', mouths_to_learn=6)
lang3 = Language.objects.create(name='UX-UI', mouths_to_learn=2)

stu = Student.objects.create(name='Amanov Aman', email='aman@mail.ru', phone_number='996700989898', work_study_place='School №13', has_own_notebook=True, preferred_os='windows')
stu2 = Student.objects.create(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888', work_study_place='TV', has_own_notebook=True, preferred_os='mac')
stu3 = Student.objects.create(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312', work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='linux')

men = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454', main_work=None, experience=datetime.date(year=2021, month=10, day=23))
men2 = Mentor.objects.create(name='Halil Nurmuhametov', email='imask@gmail.com', phone_number='0709989876', main_work='University of Fort Collins', experience=datetime.date(year=2010, month=9, day=18))

cour = Course.objects.create(name='UI-UI 43', mentor=men, student=stu3, data_started=datetime.date(year=2022, month=8, day=22), language=lang3)
cour2 = Course.objects.create(name='Python-21', mentor=men2, student=(stu, stu2), data_started=datetime.date(year=2022, month=8, day=1), language=lang)

