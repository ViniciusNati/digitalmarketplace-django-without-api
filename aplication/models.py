from django.db import models
from django.contrib.auth.models import User #allauth?
from django.utils.text import slugify
from django.db import IntegrityError



class Category(models.Model): #só vai servir pra fazer filtragem dos anuncios (listview)
    cat = models.CharField(max_length=50)
    image=models.ImageField(upload_to='category/',null=True)

    def __str__(self):
        return self.cat


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   #user = foreign key allauth
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title   
    cat = models.ForeignKey(Category, on_delete=models.CASCADE) #relação com o cat do categoria /    
    price = models.FloatField()
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)

        ##incremento
        i = 1
        while Post.objects.filter(slug=self.slug).exists():
            self.slug = f"{self.slug}-{i}"
            i += 1

        super().save(*args, **kwargs)

    published = models.BooleanField(default=False,null=True) #ativado ou desativado
    premium = models.BooleanField(default = False, null=True) #premium ou não
    amount = models.IntegerField(default = 1) #quantidade
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='post/',null=True)
    amountselled = models.IntegerField(default = 0,null=True)

""" def save(self, *args, **kwargs):
    value = self.title
    self.slug = slugify(value, allow_unicode=True)

    ##incremento
    i = 1
    while Post.objects.filter(slug=self.slug).exists():
        self.slug = f"{self.slug}-{i}"
        i += 1

    super().save(*args, **kwargs)"""

class slugpostsave(models.Model):
    slug = models.OneToOneField(Post,on_delete=models.CASCADE, null=True)




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{self.post}'
        
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    published = models.BooleanField(default=False,null=True)
    postid = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='seila', null=True)


#my_post = Post.objects.get(id=1)
#comments = my_post.comment_set.all()
#approved_comments = my_post.comment_set.filter(approved=True)



class LastReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    #avaliaçoespositivas = seila
    #ultimasavaliacoes = seilaoq


class Bank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}' #formatado pra string
    #avatar = models.ImageField
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    releasebalance = models.DecimalField(max_digits=10, decimal_places=2,default=0) #
    accpoints = models.IntegerField(default=0)
 #   cart = models.ManyToManyField(Post, related_name="carrinho", default=None) #não sei se é manytomany
    verified = models.BooleanField(default=False)
    acctype = models.CharField(max_length=20, default='Membro') #membro,parceiro,premium,influencer| ideas
    #buys = seilaoq
    #notifications = seilaoq
    #favoritos = seilaoq
class Verified(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}' #formatado pra string

    telephone = models.IntegerField(null=True) #verificaçoes
    rg = models.CharField(max_length=10,null=True)  #verificaçoes
    cpf = models.CharField(max_length=11,null=True) #verificaçoes
    birthdate = models.DateField(null=True) #verificaçoes
    cep = models.CharField(max_length=8,null=True)
    address = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=20,null=True)
    country = models.CharField(max_length=20,null=True) 
    photorg = models.ImageField(upload_to='documents/', null=True)





#template
#comprar anuncio
#anunciosativos /template