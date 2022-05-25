from django.contrib import admin
from .models import Part, IsVoited, Kondorse, Vote 

# Register your models here.

admin.site.register(Part)
admin.site.register(IsVoited)
admin.site.register(Kondorse)
admin.site.register(Vote)
