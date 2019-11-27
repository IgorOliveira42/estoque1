from django.shortcuts import render, redirect
from .forms import FormAnalises
from .models import Analises

def analise_list(request):
    analises = Analises.objects.all()
    template_name = 'analise_list.html'
    context = {
        'analises': analises,
    }
    return render(request, template_name, context)

def analise_new(request):
    if request.method == "POST":
        form = FormAnalises(request.POST)
        if form.is_valid:
            form.save(commit=False)
            form.cleaned_data['analise_produto'].quantidade = form.cleaned_data['analise_produto'].quantidade - form.cleaned_data['analise_quantidade']
            form.cleaned_data['analise_produto'].save_base()
            form.save()
            return redirect('analise:analise_list')
    else:
        form = FormAnalises()
    template_name = 'analise_new.html'
    context = {'form':form}
    return render(request,template_name,context)

def analise_update(request,pk):
    analises = Analises.objects.get(pk=pk)
    if request.method == "POST":
        form = FormAnalises(request.POST,instance=analises)
        if form.is_valid:
            form.save(commit=False)
            form.cleaned_data['analise_produto'].quantidade = form.cleaned_data['analise_produto'].quantidade + form.cleaned_data['analise_quantidade']
            form.cleaned_data['analise_quantidade'] = 0
            form.cleaned_data['analise_produto'].conformidade = form.cleaned_data['conformidade']
            form.cleaned_data['analise_produto'].save_base()
            form.save()
            return redirect ('analise:analise_list')
    else:
        form = FormAnalises(instance=analises)
    template_name = 'analise_update.html'
    context = {
        'form' : form,
        'pk' : pk,
    }
    return render(request,template_name,context)


def analise_delete(request,pk):
    analises = Analises.objects.get(pk=pk)
    analises.delete()
    return redirect('analise:analise_list')


'''
def notaSaidaNew(request):
    if request.method == 'POST':
        form = FormNotaSaida(request.POST)
        if form.is_valid:
            saida = form.save(commit=False)
            form.cleaned_data['saida_produto'].quantidade = form.cleaned_data['saida_produto'].quantidade - form.cleaned_data['saida_quant']
            # form.cleaned_data['saida_valor'] = form.cleaned_data['saida_produto'].valor
            form.cleaned_data['saida_produto'].save_base()
            form.save()
            redirect('notaSaida:notaSaidaList')
    else:
        form = FormNotaSaida()
    template_name = 'notaSaidaNew.html'
    context = {
        'form':form,
    }
    return render(request,template_name,context)



def notaSaidaDelete(request, pk):
    nota_saida = NotaSaida.objects.get(pk=pk)
    nota_saida.delete()
    
    return redirect('notaSaida:notaSaidaList')'''