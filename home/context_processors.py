from .models import Room


def room_navigation(request):
    rooms = Room.objects.all()
    return {'room': rooms}
