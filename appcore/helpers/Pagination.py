__author__ = 'Sabbir'
from math import ceil


class Pagination(object):

    def __init__(self, page, total_count, per_page=None):
        self.page = page
        if per_page:
            self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        """

        :type self: object
        """
        last = 0
        for num in xrange(1, self.pages + 1):
            if not (not (num <= left_edge) and not (
                            self.page - left_current - 1 < num < self.page + right_current) and not (
                        num > self.pages - right_edge)):
                if last + 1 != num:
                    yield None
                yield num
                last = num