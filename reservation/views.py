from django.shortcuts import render
from reservation.forms import ReservationForm
# Create your views here.
def reserve(request):
    form = ReservationForm()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'reservation/reservation.html', {'form':form})