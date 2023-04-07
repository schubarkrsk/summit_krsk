from django.shortcuts import render
from .forms import Order as OrderForm
from .models import Order as OrderModel


# Create your views here.
def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order_data = OrderModel(
                familiya=form.cleaned_data["familiya"],
                imya=form.cleaned_data["imya"],
                phone_number=form.cleaned_data["phone_number"],
                age=form.cleaned_data["age"],
                sex=form.cleaned_data["sex"],
                table=form.cleaned_data["table"],
                instagram=form.cleaned_data["instagrm"]
            )
            order_data.save()
            return render(request, "main.html", {"success": True})
    else:
        form = OrderForm()
    return render(request, "main/main.html", {"form": form})
