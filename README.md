"# marketplace_main R" # Archivos Django
## Views.py

### Login()
```markdown
Login permite a los usuarios iniciar sesión en la aplicación, al igual que utiliza una plantilla personalizada que es: ‘store/login.html’, utiliza un formulario personalizado que sería el loginform y, por último, al enviar los datos correctos que serían usuario y contraseña, el usuario queda autenticado y se puede acceder a funciones que requieren de una sesión activa como el agregar ítems.
```
<img width="975" height="637" alt="image"
src="https://github.com/user-attachments/assets/6a40b352-0ca3-489b-b6d7-b1ec71b28fec"
/>

<img width="975" height="637" alt="image"
src="https://github.com/user-attachments/assets/d6ba18e8-5fd3-4538-b9a9-3e6502b36cfc"
/>

<img width="975" height="637" alt="image"
src="https://github.com/user-attachments/assets/0199ed44-abf3-474c-a555-23289f9af923"
/>


### Logout_user()
```markdown
Logout_user sirve para cerrar la sesión del usuario actual y después de cerrar sesión, redirige al usuario a la página de inicio home. Por otra parte, sirve para evitar que otra persona no pueda acceder al sistema con la misma sesión y elimina toda la información de sesión asociada al usuario.
```

```python
def logout_user(request): logout(request)

return redirect('home')
```

<img width="975" height="543" alt="image"
src="https://github.com/user-attachments/assets/501842c7-be21-4b3a-a16a-7b1f4987c23a"
/>

### Detail()
```markdown
 
Detail muestra información completa de un registro especifico en la base de datos que normalmente esta identificada por un ID o Primary Key, por ejemplo, los ítems que agregamos en el marketplace como lo que seria un producto de un videojuego con sus respectivos detalles ya sea de venta o de categoría.
```

```python
def detail (request, pk):
item = get_object_or_404(Item, pk-pk)
related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

context={ 'item': item,
'related_items': related_items
}

return render(request, 'store/item.html', context)
```

<img width="975" height="450" alt="image"
src="https://github.com/user-attachments/assets/6017bc35-438a-4bed-8eb2-2527c1fa09ed"
/>


### Add_item()
```markdown
Add_item es una función para crear un nuevo item al marketplace sin tener que abrir el django admin ya que se agrega el item por medio de un formulario.
El objetivo de add_item es permitir a los usuarios añadir contenido a la página, ya sea artículos para el marketplace y esto se hace mediante un formulario (GET), cuando se envía el formulario (POST), se valida la información y si es correwcta se guarda en la base de datos de la pagina y se redirige a otra página, que sería para mostrar el detalle del ítem nuevo.
Por último, se puede proteger con @login_required para que solamente usuarios autenticados puedan añadir objetos, por ello la importancia de crearse una cuenta o iniciar sesión en una ya creada.
```
<img width="975" height="526" alt="image"
src="https://github.com/user-attachments/assets/c1c3277a-b5cf-4551-badb-98f0c7159ea8"
/>

<img width="975" height="529" alt="image"
src="https://github.com/user-attachments/assets/cc368e2e-94ef-411f-889d-53c3348307e3"
/>
 
<img width="975" height="409" alt="image"
src="https://github.com/user-attachments/assets/c6b597e1-3596-469f-b15c-5e38a028eae5"
/>

```python @login_required
def add_item(request):
if request.method == 'POST':
form = NewItemForm(request.POST, request.FILES)

if form.is_valid():
item = form.save(commit=False) item.created_by = request.user item.save()

return redirect('detail', pk=item.id)
else:
form = NewItemForm() context = {
'form': form, 'title': 'New Item'
}

return render(request, 'store/form.html', context)
```
```python
from django.shortcuts import render, get_object_or_404, redirect from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required from .models import Item, Category

from .forms import SignupForm, NewItemForm


# Create your views here. def home(request):
items = Item.objects.filter(is_sold=False) categories = Category.objects.all()

context = { 'items': items,
'categories': categories
}
return render(request, 'store/home.html', context)

def contact(request): context = {
'msg': 'Quieres otros productos contactame!'
 
}
return render(request, 'store/contact.html', context) def detail(request, pk):
item = get_object_or_404(Item, pk=pk)
related_items = Item.objects.filter(category=item.category,
is_sold=False).exclude(pk=pk)[0:3]

context={ 'item': item,
'related_items': related_items
}
return render(request, 'store/item.html', context) def register(request):
if request.method == 'POST':
form = SignupForm(request.POST)

if form.is_valid(): form.save()
return redirect('login')
 


```
 
else:
form = SignupForm()
 

```python context = {
'form': form
}
return render(request, 'store/signup.html', context) def logout_user(request):
logout(request)

return redirect('home')


@login_required
def add_item(request):
if request.method == 'POST':
form = NewItemForm(request.POST, request.FILES)

if form.is_valid():
item = form.save(commit=False) item.created_by = request.user
 
item.save()

return redirect('detail', pk=item.id)
else:
form = NewItemForm() context = {
'form': form, 'title': 'New Item'
}

return render(request, 'store/form.html', context)
```

## Urls.py (Las rutas a cada acción nueva en views)

```markdown
Urls.py corresponde al archivo que es el encargado de la configuración de las rutas desarrolladas en el marketplace_main.
La función principal por la que se elaboro este archivo es para definir las direcciones web que los usuarios pueden visitar y enlazarlo con las funciones que se agregaron como las que son para agregar ítems, registrar una cuenta en la página web, iniciar sesión en una cuenta ya creada y el área de contacto que sirve para enviar una reseña o algún comentario al creador de la pagina web.
En este archivo se utiliza el módulo path para declarar las rutas, y el sistema de autenticación para el inicio de sesión de los usuarios.

Estas líneas de código importan herramientas necesarias para crear las rutas y el sistema de inicio de sesión.
```

```python
from django.urls import path
from django.contrib.auth import views as auth_views
```

```markdown
Estas líneas de código controlan la lógica de las páginas, así como un formulario personalizado para cuando el usuario inicie sesión en la página.
```

```python
from .views import contact, detail, register, logout_user, add_item from .forms import LoginForm
```

```markdown
 
Este bloque es el encargado de definir todas las direcciones que estarán disponibles en la página.
```

```python urlpatterns = [
```

```markdown
-	Redirige a la página de contacto, utilizando la función contact para manejar la vista.
```

```python
path('contact/', contact, name='contact'),
```

<img width="975" height="849" alt="image"
src="https://github.com/user-attachments/assets/1284aa90-128c-4ef9-8eb4-1f8479e386da"
/>

```markdown
-	Permite que nuevos usuarios se registren en la aplicación mediante la función register.
```

```python
path('register/', register, name='register'),
```

<img width="975" height="967" alt="image"
src="https://github.com/user-attachments/assets/64058fcf-0dbd-4a18-b30d-3b902f1ceb35"
/>

```markdown
-	Gestiona el inicio de sesión usando la vista de Django (LoginView) con una plantilla personalizada (login.html) y un formulario propio (LoginForm).
```

```python
path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
```

<img width="975" height="798" alt="image"
src="https://github.com/user-attachments/assets/8395a1b5-f264-4737-bd13-09599cccaec3"
/>

```markdown
 
-	Cierra la sesión del usuario mediante la función logout_user.
```

```python
path('logout/', logout_user, name='logout'),
```

<img width="975" height="722" alt="image"
src="https://github.com/user-attachments/assets/7aeb199a-59ea-4db4-9f5f-b4972bdeb317"
/>

```markdown
-	Permite agregar un nuevo ítem o producto en la aplicación a través de la función add_item.
```

```python
path('add_item/', add_item, name='add_item'),
```
<img width="975" height="488" alt="image"
src="https://github.com/user-attachments/assets/be5b5fb3-8da7-4556-b6b6-b00caafd5409"
/>

```markdown
-	Muestra la información de un ítem específico identificado por su ID (pk) usando la función detail.
```

```python
path('detail/<int:pk>/', detail, name='detail')
]
```
<img width="975" height="669" alt="image"
src="https://github.com/user-attachments/assets/16d5c50b-04e3-4480-9f70-01dbfd7466c7"
/>

```python
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import contact, detail, register, logout_user, add_item from .forms import LoginForm
urlpatterns = [
path('contact/', contact, name='contact'), path('register/', register, name='register'),
 
path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
path('logout/', logout_user, name='logout'), path('add_item/', add_item, name='add_item'), path('detail/<int:pk>/', detail, name='detail')
]
```

##Willy
##Actualizaciones de forms.py (LoginForm, SignupForm, NewItemForm)
```markdown
En el archivo forms.py de nuestro proyecto Marketplace_main, se realizaron una serie de mejoras importantes en el registro de usuarios como en la creación de nuevos productos. LoginForm (Formulario de inicio de sesión)
Este formulario se apoya del formulario que la plataforma Django trae por defecto (AuthenticationForm). Lo que se realizó fue personalizar los campos username y password, a los cuales se les agregaron estilos que nos ofrece Bootstrap. En el apartado de username y password se agregó un comando placeholder para que el usuario sepa dónde debe escribirlo correctamente, e asimismo se le añadió la clase form-control para que obtenga una apariencia agradable. Por último, en la sección de password se agregó PasswordInput para que, al momento de añadir la contraseña, no se visualice al teclearse.
SignupForm (Formulario de registro de usuario)
Este formulario se basa en el formulario que Django ya trae por defecto para crear usuarios (UserCreationForm). Lo que se hizo fue personalizar cada uno de sus campos para que el formulario se vea más limpio y sea más fácil de usar. En los apartados de username, email, password1 y password2 se agregaron placeholders para que el usuario identifique dónde debe escribir sus datos. También se añadió la clase form-control en todos estos campos para que obtengan una apariencia más agradable y profesional. Además, los campos de password1 y password2 se configuraron con PasswordInput, para que las contraseñas no se visualicen al momento de teclearse, dando así mayor privacidad y seguridad al usuario.






NewItemForm (Formulario para crear un nuevo producto)
Este formulario toma como base un ModelForm, el cual se conecta directamente con el modelo Item. Lo que se realizó fue personalizar cada campo para que el usuario pueda agregar un producto de forma clara y ordenada. En el apartado de category se utilizó un campo de selección (Select) y se le agregó la clase form-select para que mantenga el estilo visual del resto del proyecto. En el campo name se añadió un TextInput con un diseño similar, permitiendo escribir el nombre del producto. En description se empleó un Textarea y se ajustó su tamaño para que el usuario pueda escribir una descripción más amplia sin complicaciones. El campo price también se dejó con un estilo limpio usando TextInput. Por último, en el apartado de image se utilizó FileInput, que permite subir una imagen del producto, y también se le añadió la clase form-select para mantener una apariencia uniforme en todos los campos.
 
```
##Codigo Forms.py:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm from django.contrib.auth.models import User

from .models import Item

class LoginForm(AuthenticationForm):
username = forms.CharField(widget=forms.TextInput( attrs={
'placeholder': 'Tu username', 'class': 'form-control'
}
))

password = forms.CharField(widget=forms.PasswordInput( attrs={
'placeholder': 'Tu password', 'class': 'form-control'
}
))

class SignupForm(UserCreationForm): class Meta:
model = User
fields = ['username', 'email', 'password1', 'password2' ]

username = forms.CharField(widget=forms.TextInput( attrs={
'placeholder': 'Tu Username', 'class': 'form-control'
}
))

email = forms.CharField(widget=forms.EmailInput( attrs={
'placeholder': 'Tu Email', 'class': 'form-control'
}
))

password1 = forms.CharField(widget=forms.PasswordInput( attrs={
'placeholder': 'Password', 'class': 'form-control'
 
}
))

password2 = forms.CharField(widget=forms.PasswordInput( attrs={
'placeholder': 'Repite Tu Password', 'class': 'form-control'
}
))

class NewItemForm(forms.ModelForm): class Meta:
model = Item
fields = ['category','name','description','price','image']

widgets = {
'category': forms.Select( attrs={
'class': 'form-select'
}
),
'name': forms.TextInput( attrs={
'class': 'form-select',
}
),
'description': forms.Textarea( attrs={
'class': 'form-select', 'style': 'height: 100px'
}
),
'price': forms.TextInput( attrs={
'class': 'form-select',
}
),
'image': forms.FileInput( attrs={
'class': 'form-select',
}
)
}

```

Decorador @login_required
```markdown
 
El decorador @login_required se utiliza para controlar que solo los usuarios que ya iniciaron sesión puedan acceder a cierta vista. En este caso se colocó antes de la función add_item, lo cual significa que únicamente un usuario logueado puede entrar a este apartado y crear un nuevo producto. Si un usuario intenta entrar sin haber iniciado sesión, este decorador lo redirige automáticamente a la página de login para que primero se identifique.
Dentro de la función add_item, lo que se hace es revisar si la petición es de tipo POST, lo cual significa que el usuario ya llenó el formulario para agregar un producto. Si es así, se crea un formulario con los datos enviados y también con los archivos que el usuario haya subido. Después se valida el formulario con form.is_valid(), y si todo está correcto, primero se guarda el producto con commit=False para poder añadirle quién fue el usuario que lo creó.


Esto se hace asignando item.created_by = request.user. Ya que se agregó esa información, ahora sí se guarda el producto de manera definitiva. Cuando el producto se guarda correctamente, se redirige al usuario a la página de detalle del mismo producto usando redirect ('detail', pk=item.id). Si la petición no es POST, entonces simplemente se crea un formulario vacío para que el usuario pueda llenarlo desde cero. Ese formulario se envía a la plantilla junto con un título usando el diccionario context, y al final se muestra con render para que el usuario vea la página correspondiente.

Código @login_required (Ubicado en Views.py):

```
```python @login_required
def add_item(request):
if request.method == 'POST':
form = NewItemForm(request.POST, request.FILES)

if form.is_valid():
item = form.save(commit=False) item.created_by = request.user item.save()

return redirect('detail', pk=item.id)
else:
form = NewItemForm() context = {
'form': form, 'title': 'New Item'
}

return render(request, 'store/form.html', context)
```
##Gabi
##Template (item.html)
```markdown
 
El archivo item.html es una plantilla HTML de Django que forma parte de la aplicación store dentro del proyecto marketplace_main. Su función principal es mostrar la página de detalle de un producto, es decir, toda la información individual de un artículo que se encuentra publicado en el marketplace.
Cuando un usuario selecciona un producto desde la lista de artículos, Django ejecuta una vista que obtiene ese objeto de la base de datos (por ejemplo: Item.objects.get(id=id)) y lo envía a este template. Luego, item.html se encarga de mostrar imagen del producto, nombre, precio, usuario que publicó el artículo, descripción y botón de contacto
item.html es la página encargada de mostrar toda la información de un artículo específico dentro del marketplace.

Código
```
```html
{% extends 'store/base.html' %}

{% block title %}{{item.name}} | {% endblock %}

{% block content %}
<div class="container mt-4 mb-4">
<div class="row">
<div class="col-4">
<img src="{{item.image.url}}" alt="{{item.name}}" width="100%" class="rounded">
</div>
<div class="col-8 p-4 ronded bg-light">
<h1 class="mb-4 text-center">{{ item.name }}</h1>
<hr>
<h4><strong>Precio: ${{ item.price }}</strong></h4>
<h4><strong>Vendedor: ${{ item.created_by.username }}</strong></h4>

{% if item.description %}
<p>{{item.description}}</p>
{% endif %}

<a href="" class="btn btn-dark">Contacta a el vendedor</a>
</div>
</div>
</div>
{% endblock %}

<!-- Cambio Item -->
```
##Template (login.html)
```markdown
El archivo login.html es una plantilla de Django cuyo propósito es mostrar la página de inicio de sesión del marketplace. Esta página permite que un usuario registrado ingrese su nombre de usuario y contraseña para acceder a las funciones privadas del sistema, como publicar artículos, administrar su perfil, comprar, etc.
 
Es una plantilla visual que se conecta con una vista (view) que procesa el formulario de autenticación. El template no realiza lógica por sí mismo, pero presenta el formulario, muestra los errores y envía los datos al servidor.
login.html es la página donde el usuario escribe su username y contraseña para iniciar sesión en el marketplace.
Código
```
```html
{% extends 'store/base.html' %}

{% block title %}Login | {% endblock %}

{% block content %}
<div class="row p-4 d-flex justify-content-center align-items-center">
<div class="col-6 bg-light p-4">
<h4 class="mb-6 text-center">Login</h4>
<hr>
<form action="." method="POST">
{% csrf_token %}
<div class="form-floating mb-3">
<h6>Username:</h6>
{{ form.username }}
</div>

<div class="form-floating mb-3">
<h6>Password:</h6>
{{ form.password }}
</div>

{% if form.errors or form.non_field_errors %}
<div class="mb-4 p-6 bg-danger text-white rounded">
{% for field in form %}
<h5 class="text">
{{field.errors}}
</h5>
{% endfor %}

{{ form.non_field_errors }}
</div>
{% endif %}
<div class="d-flex justify-content-center align-items-center">
<button class="btn btn-primary mb-6">Login</button>
</div>
<div class="d-flex justify-content-center align-items-center mt-2">
<a href="{% url 'register' %}">¿No tienes cuenta? registrate aqui!</a>
</div>

</form>
 
</div>
</div>
{% endblock %}
```
## Template (signup.html)
```markdown
El archivo signup.html es una plantilla HTML de Django encargada de mostrar la página de registro de usuarios dentro del marketplace. Su función principal es permitir que un visitante pueda crear una cuenta proporcionando un nombre de usuario, un correo electrónico, una contraseña, una confirmación de contraseña
Este template trabaja junto con un formulario de Django (por ejemplo, SignupForm) y con la vista que procesa la información. Es una página esencial para permitir que nuevos usuarios puedan acceder a las funciones privadas del sistema.
signup.html es la página donde los usuarios nuevos pueden registrarse para obtener una cuenta en el marketplace.
```
```html
{% extends 'store/base.html' %}

{% block title %}Registro | {% endblock %}

{% block content %}
<div class="row p-4 d-flex justify-content-center align-items-center">
<div class="col-6 bg-light p-4">
<h4 class="mb-6 text-center">Registro</h4>
<hr>
<form action="." method="POST">
{% csrf_token %}
<div class="form-floating mb-3">
<h6>Username:</h6>
{{ form.username }}
</div>
<div class="form-floating mb-3">
<h6>Email:</h6>
{{ form.email }}
</div>
<div class="form-floating mb-3">
<h6>Password:</h6>
{{ form.password1 }}
</div>
<div class="form-floating mb-3">
<h6>Repite Password:</h6>
{{ form.password2 }}
</div>

{% if form.errors or form.non_field_errors %}
<div class="mb-4 p-6 bg-danger text-white rounded">
{% for field in form %}
 
<h5 class="text">
{{field.errors}}
</h5>
{% endfor %}

{{ form.non_field_errors }}
</div>
{% endif %}
<div class="d-flex justify-content-center align-items-center">
<button class="btn btn-primary mb-6">Register</button>
</div>
<div class="d-flex justify-content-center align-items-center mt-2">
<a href="{% url 'login' %}">¿Ya tienes cuenta? Accesa aqui!</a>
</div>
</form>
</div>
</div>
{% endblock %}
```
## Template (navigation.html)
```markdown
El archivo navigation.html es una plantilla parcial (un fragmento de HTML) encargado de mostrar la barra de navegación principal del marketplace. Esta barra aparece en la parte superior de todas las páginas del sitio, ya que se incluye normalmente dentro de base.html mediante la linea de codigo {% include 'store/navigation.html' %}
Su función es permitir que los usuarios se muevan a través del sitio de forma sencilla. Además, la barra cambia dependiendo de si el usuario está autenticado o no, mostrando opciones específicas para cada caso.
navigation.html es la barra de menú principal que controla la navegación del marketplace, adaptándose al estado del usuario (logueado o no).
```
```html Nav Bar

<nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
<div class="container-fluid">
<a href="{% url 'home' %}" class="navbar-brand">Marketplace</a>
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-control="navBarNav" aria-expanded="false" aria-label="Toggle Navigation">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarNav">
<ul class="navbar-nav ms-auto">
<li class="nav-item">
<a href="" class="nav-link active"> Home
</a>
 
</li>
<li class="nav-item">
<a href="{% url 'contact' %}" class="nav-link active"> Contact
</a>
</li>
{% if request.user.is_authenticated %}
<li class="nav-item">
<a href="{% url 'add_item' %}" class="nav-link">Add Item</a>
</li>
<li class="nav-item">
<a href="{% url 'logout' %}" class="nav-link">Logout</a>
</li>
{% else %}
<li class="nav-item">
<a href="{% url 'login' %}" class="nav-link active"> Login
</a>
</li>
<li class="nav-item">
<a href="{% url 'register' %}" class="nav-link active"> Register
</a>
</li>
{% endif %}
</ul>
</div>
</div>
</nav>
```
## Template (form.html)
```markdown
El archivo form.html es un template genérico utilizado para mostrar formularios dentro del proyecto marketplace_main. Su propósito principal es renderizar un formulario dinámico, mostrar mensajes de error y enviar los datos hacia la vista correspondiente. A continuación, se explica en detalle cada parte del código:

```
```html
{% extends 'store/base.html' %}

{% block title %}{{ title }} | {% endblock %}

{% block content %}
<h4 class="mb-4-mt-4">{{ title }}</h4>
<hr>
<form action="." method="POST" enctype="multipart/form-data">
{% csrf_token %}
 
<div>
{{ form.as_p }}
</div>

{% if form.errors or form.non_field_errors %}
<div class="mb-4 p-6 bg-danger">
{% for field in form %}
<h5 class="text-white">
{{field.errors}}
</h5>

{% endfor %}

{{ form.non_field_errors }}
</div>
{% endif %}

<button class = "btn btn-primary mb-6"> Add Item
</button>
</form>

{% endblock %}
```
```markdown Paginas corriendo
```
<img width="709" height="352" alt="image"
src="https://github.com/user-attachments/assets/445e771e-20a1-4e1b-8c6a-8bf5a97e17b8"
/>
<img width="921" height="516" alt="image"
src="https://github.com/user-attachments/assets/f3088300-ab50-4a58-856a-fc20f6944322"
/>
<img width="940" height="435" alt="image"
src="https://github.com/user-attachments/assets/5bb32809-24a9-4bd4-a6c5-e736e2c76ca8"
/>
<img width="975" height="453" alt="image"
src="https://github.com/user-attachments/assets/49ee051a-7e21-403a-9278-e410d912b590 " />
<img width="975" height="548" alt="image"
src="https://github.com/user-attachments/assets/daed8c66-fa71-4818-a9b1-35b8a476a6f1"
/>
