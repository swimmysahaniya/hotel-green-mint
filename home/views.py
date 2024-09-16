from django.shortcuts import render
from .models import Room

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm, RoomBookingForm
from django.template.loader import render_to_string


def home(request):
    room = Room.objects.all()

    context = {
        'page': 'Hotel Green Mint',
        'room': room,
    }

    return render(request, "index.html", context)


def about(request):

    context = {
        'page': 'about',
    }

    return render(request, "about.html", context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile_number = form.cleaned_data['mobile_number']
            message = form.cleaned_data['message']

            # Render the HTML email template
            html_message = render_to_string('email-templates/contact-form-template.html', {
                'name': name,
                'email': email,
                'mobile_number': mobile_number,
                'message': message,
            })

            # Send email
            send_mail(
                'Contact Enquiry',
                '',  # Plain text message (optional)
                'sahaniyaswimmy@gmail.com',
                ['sahaniyaswimmy@gmail.com', email],
                fail_silently=False,
                html_message=html_message,
            )

            # Redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    context = {
        'page': 'contact',
        'form': form,
    }

    return render(request, "contact.html", context)


def thanks(request):

    context = {
        'page': 'thanks',
    }

    return render(request, "thanks.html", context)


def gallery(request):

    context = {
        'page': 'gallery',
    }

    return render(request, "gallery.html", context)


def facilities(request):

    context = {
        'page': 'facilities',
    }

    return render(request, "facilities.html", context)


def reservation(request):
    room = Room.objects.all()

    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            no_of_adults = form.cleaned_data['no_of_adults']
            no_of_children = form.cleaned_data['no_of_children']
            no_of_rooms = form.cleaned_data['no_of_rooms']
            no_of_extra_beds = form.cleaned_data['no_of_extra_beds']
            message = form.cleaned_data['message']

            # Render the HTML email template
            html_message = render_to_string('email-templates/room-booking.html', {
                'room': room,
                'name': name,
                'email': email,
                'phone': phone,
                'date': date,
                'no_of_adults': no_of_adults,
                'no_of_children': no_of_children,
                'no_of_rooms': no_of_rooms,
                'no_of_extra_beds': no_of_extra_beds,
                'message': message,
            })

            # Send email
            send_mail(
                'Room Booking Enquiry',
                '',  # Plain text message (optional)
                'sahaniyaswimmy@gmail.com',
                ['sahaniyaswimmy@gmail.com', email],
                fail_silently=False,
                html_message=html_message,
            )

            # Redirect to a new URL
            return HttpResponseRedirect('/thanks/')
    else:
        form = RoomBookingForm()

    context = {
        'page': 'reservation',
        'room': room,
        'form': form,
    }

    return render(request, "reservation.html", context)


def faqs(request):

    context = {
        'page': 'FAQs',
    }

    return render(request, "faqs.html", context)


def destination(request):

    context = {
        'page': 'Destination',
    }

    return render(request, "destination.html", context)


def prop_policy(request):

    context = {
        'page': 'property policies',
    }

    return render(request, "property-policies.html", context)


def rnc_policy(request):

    context = {
        'page': 'rules and cancellation policies',
    }

    return render(request, "rules-policies.html", context)


def rooms(request):
    room = Room.objects.all()

    context = {
        'page': 'rooms',
        'room': room,
    }

    return render(request, "rooms.html", context)


def room_detail(request, slug):
    one_room_detail = Room.objects.get(slug=slug)
    images = one_room_detail.room_images.all()

    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            no_of_adults = form.cleaned_data['no_of_adults']
            no_of_children = form.cleaned_data['no_of_children']
            no_of_rooms = form.cleaned_data['no_of_rooms']
            no_of_extra_beds = form.cleaned_data['no_of_extra_beds']
            message = form.cleaned_data['message']

            # Render the HTML email template
            html_message = render_to_string('email-templates/room-booking.html', {
                'room': room,
                'name': name,
                'email': email,
                'phone': phone,
                'date': date,
                'no_of_adults': no_of_adults,
                'no_of_children': no_of_children,
                'no_of_rooms': no_of_rooms,
                'no_of_extra_beds': no_of_extra_beds,
                'message': message,
            })

            # Send email
            send_mail(
                'Room Booking Enquiry',
                '',  # Plain text message (optional)
                'sahaniyaswimmy@gmail.com',
                ['sahaniyaswimmy@gmail.com', email],
                fail_silently=False,
                html_message=html_message,
            )

            # Redirect to a new URL
            return HttpResponseRedirect('/thanks/')
    else:
        form = RoomBookingForm()

    context = {
        'page': 'room detail',
        'room_detail': one_room_detail,
        'images': images,
        'form': form,
    }

    return render(request, "room-detail.html", context)

