from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director')
    search_fields = ['title', 'director']
    list_filter = ['release_date']

admin.site.register(Movie, MovieAdmin)