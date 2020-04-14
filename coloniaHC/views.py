from django.shortcuts import render


def nuevo_usuario(request):
    ctx={}
    return render(request, 'nuevoUsuario.html', context=ctx)
