"""PDT API urls."""
from django.conf.urls import url, include
from rest_framework import routers

from .views import (
    ReleaseViewSet,
    InstanceViewSet,
    CIProjectViewSet,
    MigrationViewSet,
    MigrationReportViewSet,
    MigrationStepReportViewSet,
    CaseViewSet,
    DeploymentReportViewSet,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'releases', ReleaseViewSet)
router.register(r'instances', InstanceViewSet)
router.register(r'ci-projects', CIProjectViewSet)
router.register(r'migrations', MigrationViewSet)
router.register(r'migration-reports', MigrationReportViewSet)
router.register(r'migration-step-reports', MigrationStepReportViewSet)
router.register(r'cases', CaseViewSet)
router.register(r'deployment-reports', DeploymentReportViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', include(router.urls)),
]
