from django.contrib import admin
from . models import LocalGovt, RegType, Gender,GroupType, Gallery, Registeration

admin.site.register([LocalGovt, RegType, Gender,GroupType, Gallery, Registeration])
