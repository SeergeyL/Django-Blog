from django.core.paginator import Paginator


def setup_paginator(items, request, items_per_page=10):
    """ Setup paginator and returns page and paginator """

    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return page, paginator
