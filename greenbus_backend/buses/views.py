from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from buses.serializers import BusSerializer, RouteSerializer
from buses.models import Bus, Route
from authn.models import UserProfile

@api_view(['GET'])
@authentication_classes([])
def get_buses(request):
    buses = Bus.objects.all()
    # Serialize the queryset
    serializer = BusSerializer(buses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([])
def search_buses(request):
    # Extract source and destination from the request data
    source = request.data.get('source')
    destination = request.data.get('destination')

    # Validate that both source and destination are provided
    if not source or not destination:
        return Response({'error': 'Both source and destination must be provided'}, status=400)

    # Assuming source and destination are city names
    buses = Bus.objects.filter(route__source_city=source, route__destination_city=destination)

    # Serialize the queryset
    serializer = BusSerializer(buses, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
def get_routes(request):
    routes = Route.objects.all()
    # Serialize the queryset
    serializer = RouteSerializer(routes, many=True)
    return Response(serializer.data)

################# Admin access only #################

@api_view(['POST'])
@authentication_classes([])
def create_routes(request):
    # get id from body of request
    id = request.data.get('id')
    
    # find the userprofile with the id
    try:
        user = UserProfile.objects.get(id=id)
    except:
        return Response({'error': 'User not found'}, status=404)
    
    # if the user is not admin, return an error
    if user.user_type != 'admin':
        return Response({'error': 'You are not allowed to access this resource'}, status=403)

    # Extract source and destination from the request data
    source = request.data.get('source')
    destination = request.data.get('destination')
    distance = request.data.get('distance')
    
    # Validate that both source and destination are provided
    if not source or not destination or not distance:
        return Response({'error': 'source, destination and distance must be provided'}, status=400)
    
    # create a new route
    route = Route.objects.create(source_city=source, destination_city=destination, distance=distance)
    
    # Serialize the queryset
    serializer = RouteSerializer(route)
    
    return Response(serializer.data)
    
@api_view(['POST'])
@authentication_classes([])
def create_buses(request):
    # get id from body of request
    id = request.data.get('id')
    
    # find the userprofile with the id
    try:
        user = UserProfile.objects.get(id=id)
    except:
        return Response({'error': 'User not found'}, status=404)
    # if the user is not admin, return an error
    if user.user_type != 'admin':
        return Response({'error': 'You are not allowed to access this resource'}, status=403)
    
    # Extract data from the request data
    bus_name = request.data.get('bus_name')
    total_seats = request.data.get('total_seats')
    current_occupancy = request.data.get('current_occupancy')
    available_days = request.data.get('available_days')
    route_id = request.data.get('route')
    fare = request.data.get('fare')
    eta = request.data.get('eta')
    
    # Validate that all required fields are provided
    if not bus_name or not total_seats or not current_occupancy or not available_days or not route_id or not fare or not eta:
        return Response({'error': 'bus_name, total_seats, current_occupancy, available_days, route_id, fare and eta must be provided'}, status=400)
    
    # get route with the route id
    try:
        route = Route.objects.get(id=route_id)
    except:
        return Response({'error': 'Route not found'}, status=404)
    
    # create a new bus
    bus = Bus.objects.create(bus_name=bus_name, total_seats=total_seats, current_occupancy=current_occupancy,\
        available_days=available_days, route=route, fare=fare, eta=eta)
    
    # Serialize the queryset
    serializer = BusSerializer(bus)
    
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([])
def update_bus(request):
    # get id from body of request
    id = request.data.get('id')
    
    # find the userprofile with the id
    try:
        user = UserProfile.objects.get(id=id)
    except:
        return Response({'error': 'User not found'}, status=404)
    # if the user is not admin, return an error
    if user.user_type != 'admin':
        return Response({'error': 'You are not allowed to access this resource'}, status=403)
    
    # Extract data from the request data
    bus_id = request.data.get('bus_id')
    bus_name = request.data.get('bus_name')
    total_seats = request.data.get('total_seats')
    current_occupancy = request.data.get('current_occupancy')
    available_days = request.data.get('available_days')
    route_id = request.data.get('route')
    fare = request.data.get('fare')
    eta = request.data.get('eta')
    
    # Validate that all required fields are provided
    if not bus_id or not bus_name or not total_seats or not current_occupancy or \
        not available_days or not route_id or not fare or not eta:
        return Response({'error': 'bus_id, bus_name, total_seats, current_occupancy, \
            available_days, route_id, fare and eta must be provided'}, status=400)
    
    # get route with the route id
    try:
        route = Route.objects.get(id=route_id)
    except:
        return Response({'error': 'Route not found'}, status=404)
    
    # get bus with the bus id
    try:
        bus = Bus.objects.get(id=bus_id)
    except:
        return Response({'error': 'Bus not found'}, status=404)
    
    # update the bus
    bus.bus_name = bus_name
    bus.total_seats = total_seats
    bus.current_occupancy = current_occupancy
    bus.available_days = available_days
    bus.route = route
    bus.fare = fare
    bus.eta = eta
    bus.save()
    
    # Serialize the queryset
    serializer = BusSerializer(bus)
    
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([])
def delete_bus(request):
    # get id from body of request
    id = request.data.get('id')
    # find the userprofile with the id
    try:
        user = UserProfile.objects.get(id=id)
    except:
        return Response({'error': 'User not found'}, status=404)
    # if the user is not admin, return an error
    if user.user_type != 'admin':
        return Response({'error': 'You are not allowed to access this resource'}, status=403)
    
    # Extract data from the request data
    bus_id = request.data.get('bus_id')
    
    # Validate that all required fields are provided
    if not bus_id:
        return Response({'error': 'bus_id must be provided'}, status=400)
    
    # get bus with the bus id
    try:
        bus = Bus.objects.get(id=bus_id)
    except:
        return Response({'error': 'Bus not found'}, status=404)
    
    # delete the bus
    bus.delete()
    
    return Response({'success': 'Bus deleted successfully'}, status=200)

@api_view(['POST'])
@authentication_classes([])
def update_route(request):
    # get id from body of request
    id = request.data.get('id')
    
    # find the userprofile with the id
    try:
        user = UserProfile.objects.get(id=id)
    except:
        return Response({'error': 'User not found'}, status=404)
    # if the user is not admin, return an error
    if user.user_type != 'admin':
        return Response({'error': 'You are not allowed to access this resource'}, status=403)
    
    # Extract data from the request data
    route_id = request.data.get('route_id')
    source_city = request.data.get('source')
    destination_city = request.data.get('destination')
    distance = request.data.get('distance')
    
    # Validate that all required fields are provided
    if not route_id or not source_city or not destination_city or not distance:
        return Response({'error': 'route_id, source, destination and distance must be provided'}, status=400)
    
    # get route with the route id
    try:
        route = Route.objects.get(id=route_id)
    except:
        return Response({'error': 'Route not found'}, status=404)
    
    # update the route
    route.source_city = source_city
    route.destination_city = destination_city
    route.distance = distance
    route.save()
    
    # Serialize the queryset
    serializer = RouteSerializer(route)
    
    return Response(serializer.data)

