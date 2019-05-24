
from django.urls import path
from . import views

urlpatterns = [
    path('test1/',views.text),
    path('xsjzb/',views.xsj_index,name="index"),
    path('add/',views.xsj_add,name="add"),
    path('add_handle/',views.xsj_add_handle,name="add_handle"),
    path('cgal/',views.xsj_cgal,name="chenggonganli"),

    path('gyhq/',views.xsj_gyhq,name="guanyuhuaqi"),
    path('about_1/',views.xsj_about_1,name="about_1"),
    path('about_2/',views.xsj_about_2,name="about_2"),

    path('lxwm/',views.xsj_lxwm,name="lianxiwomen"),
    path('person/',views.xsj_per,name="personal"),

    path('xwzx/',views.xsj_xwzx,name="xinwenzhongxin"),
    path('xwzx/gsxw/',views.xsj_gsxw,name="gsxw"),
    path('xwzx/hyxw/',views.xsj_hyxw,name="hyxw"),

    path('lyb/',views.xsj_lyb,name="liuyanban"),
    path('xwzx/xqy/<blog_id>',views.xsj_xqy,name="xqy"),

    path('ywjs/',views.xsj_ywjs,name="yewujieshao"),
    path('ywjs/xqy/<blog_id>',views.xsj_col,name="ywjsxqy"),

    path('edit/',views.xsj_edit,name="edit"),
    path('delete/<blog_id>',views.delete,name="delete"),
    path('alter/<blog_id>',views.alter,name="alter"),
    # path('college/',views.college,name="aclooege"),

]