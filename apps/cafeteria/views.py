from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.cafeteria.models import Produto
from apps.cafeteria.forms import ProdutoForms
# Create your views here.

def index(request): 
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
    
    produto = Produto.objects.order_by("-data_criacao").filter(publicada=True)
    return render(request, 'cafeteria/index.html', {"produtos": produto})

def produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'cafeteria/produto.html', {"produto": produto})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")        
        return redirect('login')

    produto = Produto.objects.order_by("-data_criacao").filter(publicada=True)

    if "buscar" in request.GET:
        denominacao_a_buscar = request.GET["buscar"]
        if denominacao_a_buscar:
            produto = produto.filter(denominacao__icontains=denominacao_a_buscar)

    return render(request, "cafeteria/index.html", {"produtos": produto})

def cadastrar_produto(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")        
        return redirect('login')
    
    form = ProdutoForms
    if request.method == 'POST':
        form = ProdutoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo produto cadastrado com sucesso!')
            return redirect('index')
    
    return render(request, "cafeteria/cadastrar_produto.html", {'form': form})

def editar_produto(request, produto_id):
    produto = Produto.objects.get(id = produto_id)
    form = ProdutoForms(instance=produto)
    if request.method == 'POST':
        form = ProdutoForms(request.POST, request.FILES, instance= produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editado com sucesso!')
            return redirect('index')        
        
    return render(request, "cafeteria/editar_produto.html", {'form': form, 'produto_id': produto_id})

def deletar_produto(request, produto_id):
    produto = Produto.objects.get(id = produto_id)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso!')
    return redirect('index')      

def filtro(request, categoria):
    produto = Produto.objects.order_by("-data_criacao").filter(publicada=True, categoria = categoria)
      
    return render(request, 'cafeteria/index.html', {'produtos': produto})