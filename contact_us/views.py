from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import Http404
from django.db.models import Q

from .models import Contact_Us

from .forms import SendInquiryForm

# Create your views here.
def contact_us(request):
    form = SendInquiryForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Your inquiry has been sent. Please give us 2 business days to respond.')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request, "forms/contact_us_form.html", context)

@login_required
def all_inquiries(request):
    try:
        query_list = Contact_Us.objects.all().order_by('-timestamp')

        #========Search feature============
        query = request.GET.get("q")  # q is for the search text value
        if query:
            query_list = query_list.filter(
                Q(cust_name__icontains=query) |
                Q(cust_email_address__icontains=query) |
                Q(cust_inquiry__icontains=query)
            ).distinct()  #to avoid duplicate result
        #=====END OF Search feature=======

        #=========Pagination============

        paginator = Paginator(query_list, 50)

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

        request.session['all'] = True
        request.session['unread'] = False
        request.session['read'] = False

    except Contact_Us.DoesNotExist:
        raise Http404("No messages received.")
    return render(request, 'inquiries/display_all.html', {'inquiries': page_content, 'page_range': page_range})

@login_required
def unread_inquiries(request):
    try:
        query_list = Contact_Us.objects.filter(marked_read=False).order_by('-timestamp')

        #========Search feature============
        query = request.GET.get("q")  # q is for the search text value
        if query:
            query_list = query_list.filter(
                Q(cust_name__icontains=query) |
                Q(cust_email_address__icontains=query) |
                Q(cust_inquiry__icontains=query)
            ).distinct()
        #=====END OF Search feature=======

        #=========Pagination============

        paginator = Paginator(query_list, 50)

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

        request.session['all'] = False
        request.session['unread'] = True
        request.session['read'] = False

    except Contact_Us.DoesNotExist:
        raise Http404("No messages received.")
    return render(request, 'inquiries/display_all.html', {'inquiries': page_content, 'page_range': page_range})

@login_required
def read_inquiries(request):
    try:
        query_list = Contact_Us.objects.filter(marked_read=True).order_by('-timestamp')

        #========Search feature============
        query = request.GET.get("q")  # q is for the search text value
        if query:
            query_list = query_list.filter(
                Q(cust_name__icontains=query) |
                Q(cust_email_address__icontains=query) |
                Q(cust_inquiry__icontains=query)
            ).distinct()
        #=====END OF Search feature=======

        #=========Pagination============

        paginator = Paginator(query_list, 50)

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

        request.session['all'] = False
        request.session['unread'] = False
        request.session['read'] = True

    except Contact_Us.DoesNotExist:
        raise Http404("No messages received.")
    return render(request, 'inquiries/display_all.html', {'inquiries': page_content, 'page_range': page_range})

@login_required
def inquiry_details(request, pk):
    message_body = get_object_or_404(Contact_Us, pk=pk)
    request.session['id'] = pk  #save in session the mess id to use it in mark_as_read()
    return render(request, 'inquiries/inquiry_details.html', {'message_body': message_body})

@login_required
def mark_as_read(request):
    '''
    :param request: to change the marked_read = True
    :return: if proper session ID was selected it will update the marked_read status of the record
    '''
    try:
        session_message_id = request.session['id']
        session_instance = get_object_or_404(Contact_Us, pk=session_message_id)
        t = Contact_Us.objects.get(id=session_message_id)
        t.marked_read = True
        t.save()

    except KeyError:
        raise Http404("Page does not exist")

    return render(request, 'inquiries/inquiry_details.html', {'message_body': session_instance})



#TODO: generic relations/sessions-to transfer value to diff. function
#TODO: DONE! Pagination with custom number: https://stackoverflow.com/questions/30864011/display-only-some-of-the-page-numbers-by-django-pagination
#TODO: Create logout page
#TODO: breadcrumb