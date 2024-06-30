from django.urls import include, path
from .models import CourseResource, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')
course_resource = CourseResource()
category_resource = CategoryResource()
api.register(resource=course_resource)
api.register(resource=category_resource)


course_resource = CourseResource()
category_resource = CategoryResource()

urlpatterns = [
    path('', include(api.urls), name='index'),
    path('courses/', include(course_resource.urls)),
    path('categories/', include(category_resource.urls)),
]