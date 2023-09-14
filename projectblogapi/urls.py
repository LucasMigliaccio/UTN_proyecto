from rest_framework import routers
from .viewsets import ProjectBlogViewSet

router= routers.SimpleRouter()
router.register('projectblogapi', ProjectBlogViewSet)
urlpatterns = router.urls