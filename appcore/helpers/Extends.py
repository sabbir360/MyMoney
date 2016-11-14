__author__ = 'Sabbir'
from flask import request, url_for, Response


class FrameExtends():

    def __init__(self):
        pass

    @staticmethod
    def url_for_other_page(page, rpp):
        args = request.view_args.copy()
        args['page'] = page
        args['__rpp'] = rpp
        return url_for(request.endpoint, **args)


class CResponse(Response):
    default_mimetype = 'text/html'

    def put_mime(self, mime):
        self.default_mimetype = mime


class ModelHelper():
    def __init__(self):
        pass

    '''
    @staticmethod
    def get_batch_combo():
        from appcore.models.InstanceBatch import InstanceBatch
        return InstanceBatch().combo()
    '''
