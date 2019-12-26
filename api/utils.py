from .pagination import APIPagination

def override_view_attributes(ref):
    ref.pagination_class = APIPagination
