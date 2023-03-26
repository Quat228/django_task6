from employee_client.models import *

e1 = Employee.objects.create(name="Kubat", birth_date="2004-02-13",
                             position="Back-End Developer", salary=60000, work_experience="2022-11-15")

e2 = Employee.objects.create(name="Daun", birth_date="2002-02-13",
                             position="Front-End Developer", salary=40000, work_experience="2021-11-15")

e3 = Employee.objects.create(name="Aibek", birth_date="2001-01-15",
                             position="Fullstack Developer", salary=80000, work_experience="2020-8-15")

e4 = Employee.objects.create(name="Janger", birth_date="2005-08-2",
                             position="Designer", salary=50000, work_experience="2018-2-19")

p1 = Passport.objects.create(inn="23256765456543", id_card="323232323", employee=e1)
p2 = Passport.objects.create(inn="13256765456542", id_card="787878787", employee=e2)
p3 = Passport.objects.create(inn="23457382918243", id_card="656565656", employee=e3)
p4 = Passport.objects.create(inn="13213439706580", id_card="121212121", employee=e4)

Passport.objects.last().delete()
Employee.objects.last().delete()

wp1 = WorkProject.objects.create(project_name="AI")

wp1.employees.set([e1, e2, e3])

wp1.employees.remove(Employee.objects.get(id=2))

wp1.employees.create(name="Janat", birth_date="2000-01-15",
                     position="Helper", salary=20000, work_experience="2022-2-19")

c1 = Client.objects.create(name="Askar", birth_date="1998-02-15", address="10 mrk", phone_number="0557132204")
c2 = Client.objects.create(name="Akbar", birth_date="1997-08-15", address="7 mrk", phone_number="0709864947")
c3 = Client.objects.create(name="Temirlan", birth_date="1999-03-20", address="8 mrk", phone_number="0705023015")

vipc1 = VIPClient.objects.create(name="Azamat", birth_date="2004-07-16", address="6 mrk",
                                 phone_number="0555131313", donation_amount=5000)

list_id_vip_client = []

for vip_client in VIPClient.objects.all():
    list_id_vip_client.append(vip_client.id)


if c2.id not in list_id_vip_client:
    Client.objects.get(id=c2.id).delete()


Employee.objects.all()
Employee.objects.filter(passport__isnull=False)
WorkProject.objects.all()
e1.work_projects.all()
Employee.objects.get(name="Kubat").work_projects.all()
Client.objects.all()
VIPClient.objects.all()


e1.passport.get_gender()
# В момент создания экземляра e1 и добавления в базу данных, в дб birth_date зашла как datetime.date, а вот
# экземпляру e1 передалось birth_date просто как строка, поэтому без кода ниже get_age() вызвал бы ошибку,
# но в случае если обращаться к объекту таблицы напрямую: Employee.objescts.get(id=1).get_age(),
# то get_age возвращать ошибки не будет, так как из бд он уже будет брать в виде datetime.date
e1.birth_date = datetime.datetime.strptime(e1.birth_date, "%Y-%m-%d").date()

e1.get_age()
