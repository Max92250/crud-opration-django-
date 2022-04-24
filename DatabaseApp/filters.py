
import django_filters

from DatabaseApp.models import Employee

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = '__all__'