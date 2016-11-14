__author__ = 'Sabbir'
from flask import request
from appcore.helpers.Pagination import Pagination


class Service():

    per_page = 10

    def __init__(self):
        pass

    def page_generator(self, opt_filter, page_no):
        page_no = int(page_no)

        self.per_page = request.values.get("__rpp") or self.per_page
        self.per_page = int(self.per_page)

        data = opt_filter.limit(self.per_page)

        if page_no > 1:
            data = data.offset(self.per_page*(page_no - 1))

        # print data.all()
        # import pdb;pdb.set_trace()
        return dict(data=data.all(),
                    page=Pagination(page=page_no, per_page=self.per_page, total_count=opt_filter.count()))