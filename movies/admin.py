from django.contrib import admin


from movies.models import ContentList,StreamingPlatform

# Register your models here.

admin.site.register(StreamingPlatform)
admin.site.register(ContentList)

