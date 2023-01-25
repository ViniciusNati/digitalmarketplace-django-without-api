from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *
##




################################################ Class Based View #####################################################

class index(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 50
    

################################################ Functions Based View #####################################################

##função anunciar e verificar se usuario está logado
@login_required
def AnunciarView(request):
    if request.user.is_authenticated: # se estiver logado
        if request.method == 'POST': #verifica se formulario ja recebeu os dados no botão enviar
            form = AnunciarForm(request.POST) #pede os dados caso n tenha recebido
            form.instance.user = request.user #resolve a porra toda q eu tava c problema
            if form.is_valid(): #validação de formulario
                form.save() #salva o modelform no bd
                return redirect(reverse('index')) #redirecionar para um sucess url
        else:
            form = AnunciarForm() #retry
        return render(request, 'announce/anunciar.html', {'form': form}) #se der erro redireciona pro anunciar
    else: 
        return HttpResponse('vc n ta logado') #se não estiver logado

#def AnnounceView(request):



@login_required
def VerifiedView(request):
        if request.user.is_authenticated: # se estiver logado
            if request.method == 'POST': #verifica se formulario ja recebeu os dados no botão enviar
                form = VerifiedForm(request.POST) #pede os dados caso n tenha recebido
                form.instance.user = request.user #resolve a porra toda q eu tava c problema
                if form.is_valid(): #validação de formulario
                    form.save() #salva o modelform no bd
                    return redirect(reverse('index')) #redirecionar para um sucess url
            else:
                form = VerifiedForm() #retry
            return render(request, 'profile/verified.html', {'form': form}) #se der erro redireciona pro anunciar
        else: 
            return HttpResponse('vc n ta logado') #se não estiver logado


@login_required
def AccountView(request):
    if request.user.is_authenticated: 
        account = Bank.objects.filter(user=request.user)
        context = {'account': account}
        return render(request, 'profile/account.html', context)

@login_required
def BankView(request):
    if request.user.is_authenticated: 
        account = Bank.objects.filter(user=request.user)
        context = {'account': account}
        return render(request, 'profile/bank.html', context)


"""def PostView(request,slug): #passar o slug pra url
    slug = Post.objects.get(slug=slug) #slug.tudo funciona
    form = CommentForm #form de comentario
    
    #CommentView(request)
    context = {
        'slug': slug,
        'form': form,
        }
    return render(request, 'announce/post.html', context)"""

def PostView(request,slug): #passar o slug pra url
    slug = Post.objects.get(slug=slug) #slug.tudo funciona

    form = CommentForm #form de comentario
    if request.user.is_authenticated: # se estiver logado
        if request.method == 'POST': #verifica se formulario ja recebeu os dados no botão enviar
            form = CommentForm(request.POST) #pede os dados caso n tenha recebido
            
            form.instance.user = request.user #resolve a porra toda q eu tava c problema
            #post = Post.objects.get(id=post_id)

            #postid = get_object_or_404(Post, id=id)


            form.instance.post = slug
            form.instance.postid = Post.id

            if form.is_valid(): #validação de formulario
                #########
                form.save() #salva o modelform no bd
                return redirect(reverse('index')) #redirecionar para um sucess url
        else:
            form = CommentForm() #retry
        return render(request,'announce/post.html', {'slug': slug,'form': form}) #se der erro redireciona pro anunciar  #'announce/post.html
    else: 
        return HttpResponse('vc n ta logado') #se não estiver logado"""
    #CommentView(request)


"""@login_required
def CommentView(request,slug):
    if request.user.is_authenticated: # se estiver logado
        if request.method == 'POST': #verifica se formulario ja recebeu os dados no botão enviar
            form = CommentForm(request.POST) #pede os dados caso n tenha recebido

            form.instance.user = request.user #resolve a porra toda q eu tava c problema

            if form.is_valid(): #validação de formulario
                #########
                form.save() #salva o modelform no bd
                return redirect(reverse('index')) #redirecionar para um sucess url
        else:
            form = CommentForm() #retry
        return render(request,'announce/comment.html', {'form': form}) #se der erro redireciona pro anunciar  #'announce/post.html
    else: 
        return HttpResponse('vc n ta logado') #se não estiver logado"""



def ProfileSlug(request, username,id): #receber url com nome de usuario

    usern = User.objects.get(username=username,id=id)
    #userr3 = Bank.objects.filter(user=id)

    context = {
        'usern': usern,  #slug.title funciona
       # 'userr3': userr3,
        }
    return render(request, 'profile/profile.html', context)



###
def template1(request):
    return render (request,'partials/pages/index.html')

def template2(request):
    return render (request,'partials/pages/anunciar.html')

def template3(request):
    return render (request,'partials/pages/anuncio.html')

def template4(request):
    return render (request,'partials/pages/search.html')