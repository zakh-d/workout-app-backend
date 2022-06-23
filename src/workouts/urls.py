from rest_framework.routers import SimpleRouter

from workouts.views import WorkoutsApiView

router = SimpleRouter()
router.register(r'workouts', WorkoutsApiView)

urlpatterns = router.urls
