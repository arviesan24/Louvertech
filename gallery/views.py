from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from .models import Gallery
from django.db.models import Q

from .forms import UploadFileForm

# Create your views here.


def index(request):
    """
    :param request: Get the objects to display the gallery
    :return: Paginated list of all products
    """
    try:
        query_list = Gallery.objects.all().order_by('-timestamp')

        #========Search feature============
        query = request.GET.get("q")  # q is for the search text value
        if query:
            query_list = query_list.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        #=====END OF Search feature=======

        #=========Pagination============

        paginator = Paginator(query_list, 10)

        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            page_content = paginator.page(page)
        except(EmptyPage, InvalidPage):
            page_content = paginator.page(1)


        #Get the index of the current page
        index = page_content.number - 1
        #This value is maximum index of your pages, so the last page - 1
        max_index = len(paginator.page_range)
        #Make range of 7, calculate where to slice the list
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]
        #=====End of Pagination=========

    except Gallery.DoesNotExist:
        raise Http404("Images does not exist")
    return render(request, 'index.html', {'gallery_app': page_content, 'page_range': page_range})

@login_required
def upload_product(request):
    '''
    request.session['add_product'] - change the title of the form to add product
    '''
    request.session['add_product'] = True
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Product successfully saved.')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,

    }
    return render(request, "forms/add_gallery_form.html", context)

@login_required
def edit_product(request, slug=None):
    '''
        request.session['add_product'] - change the title of the form to edit product
        get the value of slug to set it as the default value to edit in the form
        instance.save() - will automatically consider by django as update request since existing value is present
    '''
    request.session['add_product'] = False
    instance = get_object_or_404(Gallery, slug=slug)
    form = UploadFileForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Product successfully edited.')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,

    }
    return render(request, "forms/add_gallery_form.html", context)

def product_details(request, slug=None):
    instance = get_object_or_404(Gallery, slug=slug)
    context = {
        "instance": instance,  #include this so you can call the image link in the templates
        "product_name": instance.name,
        "product_details": instance.description,
        "product_image": instance.image_location,
    }

    return render(request, "product_details.html", context)