import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class APIBaseTest:
    def setup_method(self) -> None:
        self.client: APIClient = APIClient()
