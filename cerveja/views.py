from django.shortcuts import render, redirect
from cerveja.models import Cervejas
from .forms import FormProdutos

def index(request):
    template_name = 'index.html'
    return render(request,template_name)

def produto_lista(request):
    produtos = Cervejas.objects.all()
    template_name = 'produto_lista.html'
    context = {'produtos':produtos,}
    return render(request,template_name,context)

def produto_novo(request):
    if request.method == "POST":
        form = FormProdutos(request.POST)
        if form.is_valid:
            form.save()
            return redirect('produto_lista')
    else:
        form = FormProdutos()
    template_name = 'produto_novo.html'
    context = {'form':form}
    return render(request,template_name,context)

def produto_delete(request,pk):
    produtos = Cervejas.objects.get(pk=pk)
    produtos.delete()
    return redirect('produto_lista')

def produto_edit(request,pk):
    produtos = Cervejas.objects.get(pk=pk)
    if request.method == "POST":
        form = FormProdutos(request.POST,instance=produtos)
        if form.is_valid:
            form.save()
            return redirect ('produto_lista')
    else:
        form = FormProdutos(instance=produtos)
    template_name = 'produto_edit.html'
    context = {
        'form' : form,
        'pk' : pk,
    }
    return render(request,template_name,context)
