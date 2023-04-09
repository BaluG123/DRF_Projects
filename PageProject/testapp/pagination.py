from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class Mypagination(PageNumberPagination):
    max_page_size="16"
    page_query_param="mypage"
    page_size=15