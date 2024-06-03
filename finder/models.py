from django.db import models

class Discipline(models.Model):
    discipline_code = models.CharField(max_length=50)
    discipline_name = models.CharField(max_length=100)
    quantity_of_exams = models.IntegerField()
    quantity_of_tests = models.IntegerField()

    class Meta:
        db_table = 'discipline'