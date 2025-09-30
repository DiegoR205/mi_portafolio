from django.contrib import admin
from .models import Profile, Project, FAQ, OpenItem, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nombre','email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titulo','fecha')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pregunta','orden')

@admin.register(OpenItem)
class OpenItemAdmin(admin.ModelAdmin):
    list_display = ('titulo','creado')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','enviado_en')
    readonly_fields = ('enviado_en',)
