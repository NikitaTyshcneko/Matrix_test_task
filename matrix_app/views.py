import os
from django.http import HttpResponse
from ninja import Router
from typing import List
from matrix_app.models import Matrix
from matrix_app.api.matrix import add_matrix_from_url
from matrix_app.api.traversal import traverse_matrix

matrix_router = Router()

matrix_url = 'https://raw.githubusercontent.com/Real-Estate-THE-Capital/python-assignment/main/matrix.txt'


@matrix_router.get("/traverse/{matrix_id}", tags=['Matrix'])
def print_traverse_matrix_by_id(request, matrix_id: int) -> List[List[int]] or HttpResponse:
    try:
        matrix = Matrix.objects.get(id=matrix_id)
        traversal_result = traverse_matrix(matrix.matrix_data)
        return traversal_result
    except Matrix.DoesNotExist:
        return HttpResponse(content="Matrix does not exist", content_type="text/plain", status=404)


@matrix_router.post("/add", tags=['Matrix'])
async def add_matrix(request):
    try:
        result = await add_matrix_from_url(matrix_url)
        return HttpResponse(content=result, content_type="text/plain", status=201)
    except Exception as e:
        return HttpResponse(content=str(e), content_type="text/plain", status=500)
