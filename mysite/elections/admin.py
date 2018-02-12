from django.contrib import admin

# Register your models here.
from .models import Candidate # candidate 를 admin에 내용 추가

admin.site.register(Candidate)