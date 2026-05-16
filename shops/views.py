from django.shortcuts import render
from .models import Shop, Profile
from  .forms import shopsForm, UserRegistrationForm, ProfileForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')

def shops_list(request):

    search_query = request.GET.get('search', '')

    category_query = request.GET.get('category', '')

    shops = Shop.objects.all().order_by('-created_at')

    if search_query:

        shops = shops.filter(

    Q(text__icontains=search_query) |

    Q(user__username__icontains=search_query)

)
        
    if category_query:

        shops = shops.filter(
            category=category_query
        )

    return render(
        request,
        'shops_list.html',
        {
            'shop': shops,
            'search_query': search_query,
            'category_query': category_query
        }
    )

@login_required
def shop_create(request):
    if request.method == "POST":
        form = shopsForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.save()
            return redirect('shops_list')
      
    else:
       form = shopsForm()
    return render(request,'shop_form.html',{'form' : form}) 

@login_required
def shop_edit(request, shop_id):
    shops = get_object_or_404(Shop ,pk=shop_id,user = request.user)

    if request.method == 'POST':
        form = shopsForm(request.POST, request.FILES, instance=shops)
        if form.is_valid():
            shops = form.save(commit=False)
            shops.user = request.user
            shops.save()
            return redirect('shops_list')
    else:
        form = shopsForm(instance=shops)
    return render(request, 'shop_form.html',{'form' : form})   

@login_required
def shop_delete(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id, user = request.user)
    if request.method =='POST':
        shop.delete()
        return redirect('shops_list')
    return render(request, 'shop_confirm_delete.html',{'shop' : shop})


def register(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password1']
            )

            user.save()

            login(request, user)

            return redirect('shops_list')

    else:

        form = UserRegistrationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )
    
def profile(request, username):

    user = User.objects.get(username=username)

    profile, created = Profile.objects.get_or_create(
        user=user
    )

    shops = Shop.objects.filter(
        user=profile.user
    ).order_by('-created_at')

    return render(
        request,
        'profile.html',
        {
            'profile': profile,
            'shops': shops
        }
    )

@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(
    user=request.user
)

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            return redirect(
                'profile',
                username=request.user.username
            )

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        'edit_profile.html',
        {'form': form}
    )

@login_required
def like_shop(request, shop_id):

    shop = get_object_or_404(Shop, id=shop_id)

    if request.user in shop.likes.all():

        shop.likes.remove(request.user)

    else:

        shop.likes.add(request.user)

    return redirect('shops_list')

def home(request):
    return render(request, 'home.html')

def categories(request):
    return render(request, 'categories.html')

@login_required
def favorite_shop(request, shop_id):

    shop = get_object_or_404(
        Shop,
        id=shop_id
    )

    if request.user in shop.favorites.all():

        shop.favorites.remove(request.user)

    else:

        shop.favorites.add(request.user)

    return redirect('shops_list')

@login_required
def favorites_list(request):

    favorite_shops = request.user.favorite_shops.all()

    return render(
        request,
        'favorites.html',
        {
            'favorite_shops': favorite_shops
        }
    )