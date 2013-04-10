from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_yani.views.home', name='home'),
    # url(r'^blog_yani/', include('blog_yani.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'blog.views.index'),
    # con esto le decimos a django que toda peticion hecha a la raiz del blog
    # sera manejada por la funcion index ubicada en el archivo views
)

