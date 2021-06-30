from django.contrib import admin
from .models import *

admin.site.register(Pattern)
admin.site.register(Topic)
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(TestData)
admin.site.register(SubjectPermission)
