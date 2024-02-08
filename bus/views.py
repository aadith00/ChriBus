from django.shortcuts import render, redirect, get_object_or_404
from .models import Bus, Booking, User
from datetime import datetime
import io
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


def booking(request):
    return render(request, 'booking.html')

def search_buses(request):
    if request.method == 'POST':
        departure_city = request.POST.get('departureCity')
        destination_city = request.POST.get('destinationCity')
        departure_date_str = request.POST.get('departureDate')

        if departure_date_str:
            departure_date = datetime.strptime(departure_date_str, '%Y-%m-%d').date()

        available_buses = Bus.objects.filter(departure_city=departure_city, destination_city=destination_city, departure_date=departure_date)

        return render(request, 'buses_list.html', {'available_buses': available_buses})
    
    else:
        return render(request, 'no_buses.html')


def bus_details(request, num_plate):
    bus = get_object_or_404(Bus, pk=num_plate)
    bus.available_seats = bus.calculate_available_seats()

    bus.tick_num = bus.generate_random_ticket()

    return render(request, 'bus_details.html', {'bus':bus})


def generate_ticket_pdf(ticket_number, bus_number, journey_date, register_number):
    # Create a buffer to hold PDF content
    buffer = io.BytesIO()

    # Create a PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Define styles
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']

    # Ticket information
    data = [
        ['Ticket Number:', ticket_number],
        ['Bus Number:', bus_number],
        ['Journey Date:', str(journey_date)],
        ['Register Number:', register_number],
    ]

    # Create a table to hold ticket information
    table = Table(data, colWidths=[150, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))

    # Add table to the document
    doc.build([Paragraph("Ticket Information", normal_style), table])

    # # Add custom sentence at the end
    # additional_info = "Your ticket is confirmed, and we're thrilled to be a part of your travel experience. Wishing you a comfortable and pleasant journey. Safe travels, and we look forward to serving you again soon!"
    # doc.add_paragraph(Paragraph(additional_info, normal_style))

    pdf_content = buffer.getvalue()
    buffer.close()

    return pdf_content

def book_ticket(request, num_plate, tick_num, depar_date):
    if request.method == 'POST':

        existing_booking = Booking.objects.filter(user=request.user, journey_date=depar_date).exists()
        if existing_booking:
            return render(request, 'already_booked.html')
        
        else:
            # Retrieve the bus instance
            bus = Bus.objects.get(pk=num_plate)
            bus.booked_seats += 1
            bus.save()
            
            booking = Booking.objects.create(
                user=request.user,
                num_plate=bus,
                ticket_number=tick_num,
                journey_date=bus.departure_date
            )

            if not booking.journey_date:
                booking.journey_date = datetime.now().date()

            booking.save()

            # Generate ticket PDF
            pdf_content = generate_ticket_pdf(tick_num, num_plate, booking.journey_date, booking.user)

            # Prepare HTTP response with PDF content for download
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'

            return response

    else:
        return render(request, 'book_failure.html')  # Handle case when no available seats


# def book_ticket(request, num_plate, tick_num):
#     if request.method == 'POST':
#         # Retrieve the bus instance
#         bus = Bus.objects.get(pk=num_plate)
#         bus.booked_seats += 1
#         bus.save()
        
#         booking = Booking.objects.create(
#             user=request.user,
#             num_plate=bus,
#             ticket_number=tick_num,
#             journey_date=bus.departure_date
#         )

#         if not booking.journey_date:
#             booking.journey_date = datetime.now().date()

#         booking.save()

#         # Generate ticket PDF
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'

#         buffer = io.BytesIO()
#         pdf = canvas.Canvas(buffer)

#         # Customize ticket content as per your requirement
#         pdf.drawString(100, 750, "Ticket Information:")
#         pdf.drawString(100, 730, f"Ticket Number: {tick_num}")
#         pdf.drawString(100, 730, f"Register Number: {request.user.username}")
#         pdf.drawString(100, 710, f"Bus Number: {num_plate}")
#         pdf.drawString(100, 690, f"Journey Date: {booking.journey_date}")

#         pdf.showPage()
#         pdf.save()

#         pdf_content = buffer.getvalue()
#         buffer.close()
#         response.write(pdf_content)

#         return response
#     else:
#         return render(request, 'book_failure.html')  # Handle case when no available seats


