from django.shortcuts import render, redirect
from .models import NotaSaida
from .forms import FormNotaSaida

def notaSaidaList(request):
    nota_saida = NotaSaida.objects.all()
    template_name = 'notaSaidaList.html'
    context = {
        'nota_saida': nota_saida,
    }
    return render(request, template_name, context)

def notaSaidaNew(request):
    if request.method == 'POST':
        form = FormNotaSaida(request.POST)
        if form.is_valid:
            saida = form.save(commit=False)
            form.cleaned_data['saida_produto'].quantidade = form.cleaned_data['saida_produto'].quantidade - form.cleaned_data['saida_quant']
            # form.cleaned_data['saida_valor'] = form.cleaned_data['saida_produto'].valor
            form.cleaned_data['saida_produto'].save_base()
            form.save()
            return redirect('notaSaida:notaSaidaList')
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
    
    return redirect('notaSaida:notaSaidaList')