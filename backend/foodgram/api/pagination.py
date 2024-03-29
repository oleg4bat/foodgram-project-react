from rest_framework.pagination import PageNumberPagination


class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = 6
    page_query_param = 'page'
    max_page_size = 10000
