from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Produto


# Autenticação de usuário
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next', 'listar_produto')
            return redirect(next_url)
        messages.error(request, 'Usuário ou senha inválida')
    return render(request, 'produtos/login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


# Listagem de todos os elementos da classe produtos
@login_required(login_url='login')
def listar_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})


# Cadastrar itens da classe produtos
@login_required(login_url='login')
def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        quantidade = request.POST['quantidade']
        preco = request.POST['preco']
        Produto.objects.create(nome=nome, quantidade=quantidade, preco=preco)
        return redirect('listar_produto')
    return render(request, 'produtos/adicionar.html')
    

# Alterar itens da classe produtos
@login_required(login_url='login')
def editar_produto(request, id):
    produtos = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produtos.nome = request.POST['nome']
        produtos.quantidade = request.POST['quantidade']
        produtos.preco = request.POST['preco']
        produtos.save()
        return redirect('listar_produto')
    return render(request, 'produtos/editar.html', {'produtos': produtos})


# Excluir itens da classe produtos
@login_required(login_url='login')
def excluir_produto(request, id):
    produtos = get_object_or_404(Produto, id=id)
    produtos.delete()
    return redirect('listar_produto')