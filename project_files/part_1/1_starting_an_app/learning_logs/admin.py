from django.contrib import admin

#registring topic in admin site
from .models import Topic
admin.site.register(Topic)


#registring entry in admin site
from django.contrib import admin

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)


