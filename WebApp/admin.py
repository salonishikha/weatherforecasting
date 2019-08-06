from django.contrib import admin
from .models import Weather


class WeatherAdmin(admin.ModelAdmin):
    """
    below is from
    http://stackoverflow.com/questions/11657682/
    django-admin-interface-using-horizontal-filter-with-
    inline-manytomany-field
    """
    class Meta:
        model = Weather
        fields = '__all__'


admin.site.register(Weather, WeatherAdmin)