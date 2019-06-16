from django.shortcuts import render, HttpResponse, redirect
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'category_list': category_list, 'page_list': page_list}
    
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context = {'msg': 'Bold'}
    return render(request, 'rango/about.html', context)


def show_category(request, category_name_slug):
    context_dict = {}
    print("yes")
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        page_list = Page.objects.filter(category=category)

        context_dict['pages'] = page_list
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()

    context_dict = {'form':form}
    return render(request, 'rango/add_category.html', context_dict)


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if request.method == 'POST':
        form = PageForm(request.POST)    
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect('show_category', category.slug)
        
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)