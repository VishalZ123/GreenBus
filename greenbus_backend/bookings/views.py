from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from buses.models import Bus
from authn.models import UserProfile
from bookings.models import Booking
from bookings.serializers import BookingSerializer

@api_view(['POST'])
@authentication_classes([])
def book_bus(request):
    # Extract bus id and user id from the request data
    bus_id = request.data.get('bus_id')
    user_id = request.data.get('user_id')

    # Validate that bus id and user id is provided
    if not bus_id or not user_id:
        return Response({'error': 'Bus id and User id must be provided'}, status=400)

    try:
        bus = Bus.objects.get(id=bus_id)
    except:
        return Response({'error': 'Bus not found'}, status=404)
    
    try:
        user = UserProfile.objects.get(id=user_id)
    except:
        return Response({'error': 'User not found'}, status=404)

    # Validate that bus has seats available
    if bus.current_occupancy >= bus.total_seats:
        return Response({'error': 'Bus is full'}, status=400)

    # Book the bus
    bus.current_occupancy += 1
    bus.save()
    
    # Update user's bookings
    user.booked_buses.add(bus)
    user.save()
    
    # Create a booking
    booking = Booking.objects.create(user=user, bus=bus, seat_number=bus.current_occupancy, status='Booked')
    booking.save()

    # serialize the booking
    serializer = BookingSerializer(booking)
    
    return Response(serializer.data, status=201)

@api_view(['POST'])
@authentication_classes([])
def cancel_booking(request):
    # Extract booking id from the request data
    booking_id = request.data.get('booking_id')
    
    # Validate that booking id is provided
    if not booking_id:
        return Response({'error': 'Booking id must be provided'}, status=400)
    
    try:
        booking = Booking.objects.get(id=booking_id)
    except:
        return Response({'error': 'Booking not found'}, status=404)
    
    # Validate that booking is not already cancelled
    if booking.status == 'Cancelled':
        return Response({'error': 'Booking is already cancelled'}, status=400)
    
    # Cancel the booking
    booking.status = 'Cancelled'
    booking.save()
    
    # Update bus occupancy
    bus = booking.bus
    bus.current_occupancy -= 1
    bus.save()
    
    # Update user's bookings
    user = booking.user
    user.booked_buses.remove(bus)
    user.save()
    
    return Response({'message': 'Booking cancelled successfully'}, status=200)

