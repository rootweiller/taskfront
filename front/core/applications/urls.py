from django.conf.urls import *

from .applications import *

from .config import JobtypeAdd, WorkdayAdd

urlpatterns = [


    url(r'^add/', ApplicationsAdd.as_view(), name='ApplicationsAdd'),
    url(r'^job/add', JobtypeAdd.as_view(), name='JobTypeAdd' ),
    url(r'^job/workday', WorkdayAdd.as_view(), name='WorkdayAdd'),
    url(r'^apply/(?P<pk>[0-9]+)/$', ApplicationsDetail.as_view(), name='ApplicationsDetail'),
    url(r'^apply/all', ApplicationsAll.as_view(), name='ApplicationsAll'),
    url(r'^apply/add', ApplicationsApprove.as_view(), name='ApplicationsApprove'),

    url(r'^apply/list', ApplyApproveList.as_view(), name='ApplyApproveList'),

]
