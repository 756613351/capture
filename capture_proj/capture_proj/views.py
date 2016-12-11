#coding:utf-8
import os
from django.shortcuts import render_to_response, RequestContext


def index(request, template_name):

    _dir = '/srv/capture/picture/'
    vm = {'zips': [_ for _ in  os.listdir(_dir) if not os.path.isdir(_dir+_)]}
    return render_to_response(template_name, vm, RequestContext(request))
