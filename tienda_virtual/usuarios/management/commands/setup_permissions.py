from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Configura el usuario Admin, los grupos de permisos y los permisos iniciales'
    
    def handle(self, *args, **kwargs):
        # Crear usuario admin con permisos completos
        admin_user, created = User.objects.get_or_create(
            username='admin2',
            defaults={'email': 'admin@admin.cl', 'is_staff': True, 'is_superuser':True}
        )
        if created:
            admin_user.set_password('adminpass')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Usuario creado con éxito.'))
        else:
            self.stdout.write(self.style.WARNING('Usuario ya existe.'))

        # Crear grupo de usuarios
        grupo_permisos = {'Editor1':['add_oferta', 'view_oferta','change_oferta'],
                        'Usuario_comun':['view_oferta']}
        for grupo_nombre, permisos in grupo_permisos.items():
            grupo, creado = Group.objects.get_or_create(name=grupo_nombre)
            
            for permisos_codename in permisos:
                permiso = Permission.objects.get(codename=permisos_codename)
                grupo.permissions.add(permiso)
            
        if creado:
            self.stdout.write(self.style.SUCCESS(f'Grupo {grupo_nombre} creados con éxito y permisos asignados.'))
        else:
            self.stdout.write(self.style.WARNING(f'Grupo {grupo_nombre} ya esta registrado.'))
        
        # Asignar el grupo Editor1 al usuario admin y darle todos los permisos
        
        admin_user.groups.add(Group.objects.get(name='Editor1'))
        admin_user.is_staff = True
        admin_user.is_active = True
        admin_user.save()
        self.stdout.write(self.style.SUCCESS('Configuración inicial completada con éxito'))
