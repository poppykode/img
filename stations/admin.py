from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ExaminerMarkSheet)
admin.site.register(models.ExaminerMarkSheetAnswer)
admin.site.register(models.FirstLevelStation)
admin.site.register(models.SecondLevelStation)
admin.site.register(models.ThirdLevelStation)

