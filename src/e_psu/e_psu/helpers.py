from django.utils.deconstruct import deconstructible
from uuid import uuid4
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)

def paginate_object(query_set_object, offset, page):
    paginator = Paginator(query_set_object, offset)
    try:
        query_set_object_page = paginator.page(page)
    except PageNotAnInteger:
        query_set_object_page = paginator.page(1)
    except EmptyPage:
        query_set_object_page = paginator.page(paginator.num_pages)
    return query_set_object_page