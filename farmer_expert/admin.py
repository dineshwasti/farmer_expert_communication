from django.contrib import admin
from . models import FarmerQuery,ExpertReply,User

# Register your models here.
admin.site.register(FarmerQuery)
admin.site.register(ExpertReply)
admin.site.register(User)
