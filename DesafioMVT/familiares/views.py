from django.shortcuts import render
from familiares.models import Familia

# Create your views here.

def mostrar_familiares(request):

    f1 = Familia(nombre='Claudio', parentesco='Padre', edad=59, cumpleanios='1963-18-01')
    f2 = Familia(nombre='Viviana', parentesco='Madre', edad=57, cumpleanios='1965-05-05')
    f3 = Familia(nombre='Jeronimo', parentesco='Hermano', edad=31, cumpleanios='1991-21-01')
    f4 = Familia(nombre='Aldana', parentesco='Hermana', edad=28, cumpleanios='1994-17-09')
    f5 = Familia(nombre='Mainque', parentesco='Hermana', edad=26, cumpleanios='1996-14-02')
    f6 = Familia(nombre='Shaiel', parentesco='Hermana', edad=21, cumpleanios='2001-06-01') 
    
    return render(request, 'familiares/familia.html',{'familiar': [f1, f2, f3, f4, f5, f6]})
    