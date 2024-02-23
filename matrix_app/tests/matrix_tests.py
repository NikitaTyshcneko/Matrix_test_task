import pytest
from django.test import Client
from django.test import TestCase
from matrix_app.api.traversal import traverse_matrix
from matrix_app.models import Matrix

@pytest.mark.django_db
class MatrixTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_traverse_matrix_api(self):
        matrix = Matrix.objects.create(matrix_data=[[1, 2], [3, 4]])

        response = self.client.get(f"/api/v1/matrix/traverse/{matrix.id}")

        assert response.status_code == 200
        assert response.json() == traverse_matrix(matrix.matrix_data)

    def test_traverse_matrix_api_with_wrong_id(self):
        matrix = Matrix.objects.create(matrix_data=[[1, 2], [3, 4]])

        response = self.client.get(f"/api/v1/matrix/traverse/{matrix.id+10}")

        assert response.status_code == 404
        assert response.content == b'Matrix does not exist'

    def test_add_matrix(self):
        response = self.client.post("/api/v1/matrix/add")

        assert response.status_code == 201
        assert Matrix.objects.exists()
