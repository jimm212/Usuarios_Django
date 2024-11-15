from django.shortcuts import render , redirect
from django.contrib.auth.models import User, Group
from .forms import RegistroForm 

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Asignación el grupo comun al nuevo usuario
            grupo_usuario_comun = Group.objects.get(name= 'Usuario_comun')
            user.groups.add(grupo_usuario_comun)
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})