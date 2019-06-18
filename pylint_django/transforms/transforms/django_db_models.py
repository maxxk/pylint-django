from django.core.exceptions import MultipleObjectsReturned \
    as MultipleObjectsReturnedException


def __noop(self, *args, **kwargs):
    """Just a dumb no-op function to make code a bit more DRY"""
    return None

def __noop_list(self, *args, **kwargs):
    return []

def __noop_manager(self, *args, **kwargs):
    """Just a dumb no-op function to make code a bit more DRY"""
    return SubscriptableManager()


class Model(object):
    _meta = None
    objects = None

    id = None
    pk = None

    MultipleObjectsReturned = MultipleObjectsReturnedException

    save = __noop
    delete = __noop


class Manager(object):
    """
    Eliminate E1002 for Manager object
    """

    def get_or_create(self, *args, **kwargs):
        return None, False
    
    def aggregate(self, *args, **kwargs):
        return {}
    
    def in_bulk(self, id_list=None):
        return {}

    get_queryset = __noop_manager
    none = __noop
    all = __noop_manager
    count = __noop
    dates = __noop
    distinct = __noop_manager
    extra = __noop_manager
    get = __noop
    create = __noop
    bulk_create = __noop
    filter = __noop_manager
    annotate = __noop_manager
    complex_filter = __noop
    exclude = __noop_manager
    iterator = __noop
    latest = __noop
    order_by = __noop_manager
    select_for_update = __noop
    select_related = __noop_manager
    prefetch_related = __noop_manager
    values = __noop_manager
    values_list = __noop_manager
    update = __noop
    reverse = __noop_manager
    defer = __noop_manager
    only = __noop_manager
    using = __noop_manager
    exists = __noop

    __contains__ = __noop
    __iter__ = __noop_list

class SubscriptableManager(list, Manager):
    pass

