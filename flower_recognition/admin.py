from django.contrib import admin
from flower_recognition.models import *


# Register your models here.
class FlowerPhotoInline(admin.TabularInline):
    model = FlowerPhoto
    extra = 0
    fields = ('img', 'image_tag',)
    readonly_fields = ('image_tag',)


@admin.register(Flower)
class FlowerAdminModel(admin.ModelAdmin):
    model = Flower
    inlines = [FlowerPhotoInline]


# admin.site.register(Flower)
admin.site.register(FlowerPhoto)
