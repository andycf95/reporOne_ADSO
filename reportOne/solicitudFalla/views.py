from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import solicitudFalla
from .forms import solicitudFallaForm

def inicio(request):
    """Página principal del sistema de solicitudes."""

    total_solicitudes = solicitudFalla.objects.count()
    ultimas = solicitudFalla.objects.order_by('-codigo')[:5]

    context = {
        'sistema': 'Sistema de Gestión de Solicitudes',
        'descripcion': 'Registro y seguimiento de solicitudes',
        'total_solicitudes': total_solicitudes,
        'ultimas_solicitudes': ultimas,
    }

    return render(request, 'inicio.html', context)

def lista_solicitudes(request):
    solicitudes_list = solicitudFalla.objects.all().order_by('-codigo')
    paginator = Paginator(solicitudes_list, 10)
    page = request.GET.get('page', 1)
    try:
        solicitudes = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        solicitudes = paginator.page(1)
    return render(request, 'solicitudFalla/solicitud_list.html', {'solicitudes': solicitudes})

def create_solicitud(request):
    if request.method == 'POST':
        form = solicitudFallaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitudes:lista')
        else:
            print(form.errors)   # ← para ver el error real en consola

    else:
        form = solicitudFallaForm()

    return render(request, 'solicitudFalla/solicitud_form.html', {'form': form})

def edit_solicitud(request, pk):
    solcitud = get_object_or_404(solicitudFalla, pk=pk)
    form = solicitudFallaForm(request.POST or None, instance=solcitud)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('solicitudes:lista')
    return render(request, 'solicitudFalla/solicitud_form.html', {'form': form})

def delete_solicitud(request, pk):
    solicitud = get_object_or_404(solicitudFalla, pk=pk)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('solicitudes:lista')
    return render(request, 'solicitudFalla/solicitud_confirm_delete.html', {'Solicitud': solicitud})

