from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

def home(request):
    if request.method == 'POST':
        widget_form = WidgetForm(request.POST)
        if widget_form.is_valid():
            widget_form.save()
            return redirect('home')
        
        if 'delete' in request.POST:
            widget_id = request.POST.get('delete')
            if widget_id:
                widget = Widget.objects.get(id=widget_id)
                widget.delete()
                return redirect('home')
    else:
        widget_form = WidgetForm()
    widgets = Widget.objects.all()
    total_quantity= sum(widget.quantity for widget in widgets)
    return render(request, 'home.html', {
        'widgets' : widgets,
        'widget_form' : widget_form,
        'total_quantity' : total_quantity
        })
