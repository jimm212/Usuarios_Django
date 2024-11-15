from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from .models import Oferta
from django.http import Http404
from .forms import OfertaForm
from django.contrib import messages

# Create your views here.
@login_required()
@permission_required('ofertas.change_oferta', raise_exception=True)
@permission_required('ofertas.add_oferta', raise_exception=True)
def crear_o_editar_oferta(request, oferta_id = None):
    oferta = get_object_or_404(Oferta, id=oferta_id) if oferta_id else None
    
    if request.method == 'POST':
        form = OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            if oferta:
                messages.success(request, 'La oferta ha sido actualizada con éxito!')
            else:
                messages.success(request, 'La oferta ha sido creada con éxito!')
            
            return redirect('ofertas:index')
    else:
        form = OfertaForm(instance=oferta)
        context = {
            'form': form,
            'es_editar': oferta is not None
        }
    return render(request, 'ofertas/crear_oferta.html', context)

@login_required()
@permission_required('ofertas.delete_oferta', raise_exception=True)
def eliminar_oferta(request, ofertas_id):
    oferta = get_object_or_404(Oferta, id=ofertas_id)
    
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            oferta.delete()
            return redirect('ofertas:index')
    return render(request, 'ofertas/eliminar_oferta.html', {'oferta': oferta})

@login_required()
@permission_required('ofertas.add_oferta', raise_exception=True)
def crear_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ofertas:index')
    else:
        form = OfertaForm()
    return render(request, 'ofertas/crear_oferta.html', {'form': form})

def index (request):
    current_date = datetime.now()
    ofertas = []
    
    try:
        ofertas = Oferta.objects.filter(fecha_inicio__lte=current_date, fecha_fin__gte=current_date)
        # raise Exception('Error Inesperado')
    
        if not ofertas:
            raise ValueError("No hay ofertas disponibles en este momento.")
    except ValueError as e:
        # Manejar el error especifico ValueError
        return render(request, 'ofertas/index.html', {'error': str(e), 'current_date': current_date})
    except Exception as e:
        # Manejar cualquier otro error
        return render(request, 'ofertas/index.html', {'error': 'Se produjo un error inesperado!','current_date': current_date})
            
    context = {
        'current_date': current_date,
        #'is_special_offert': False, # True o False según sea el caso
        'ofertas': ofertas
    }
    return render(request,'ofertas/index.html', context) # Renderizará la plantilla index.html
    
