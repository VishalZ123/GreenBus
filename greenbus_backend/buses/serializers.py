from rest_framework import serializers
from buses.models import Bus, Route

class BusSerializer(serializers.ModelSerializer):
    route = serializers.SerializerMethodField()
    
    class Meta:
        model = Bus
        fields = ['id', 'bus_name', 'total_seats', 'current_occupancy', 'available_days', 'fare', 'eta', 'route']
    
    def get_route(self, obj):
        return {
            'source': obj.route.source_city,
            'destination': obj.route.destination_city,
        }
    
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'source_city', 'destination_city', 'distance']