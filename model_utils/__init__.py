from pkg_resources import get_distribution, DistributionNotFound

from .choices import Choices  # noqa:F401
from .tracker import FieldTracker, ModelTracker  # noqa:F401

try:
    __version__ = get_distribution("django-model-utils").version
except DistributionNotFound:
    # package is not installed
    pass
