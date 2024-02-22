from typing import List
import aiohttp
from asgiref.sync import sync_to_async
from matrix_app.api.traversal import traverse_matrix
from matrix_app.models import Matrix


async def add_matrix_from_url(url: str) -> List[List[int]]:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch matrix: {response.status}")

                matrix_data = await response.text()

                matrix_rows = [list(map(int, filter(None, row.strip().split('|'))))
                               for row in matrix_data.splitlines() if matrix_data.splitlines().index(row) % 2 != 0]

                create_matrix = sync_to_async(Matrix.objects.create)
                await create_matrix(matrix_data=matrix_rows)
                return traverse_matrix(matrix_rows)
    except aiohttp.ClientError as e:
        raise Exception(f"Network error: {str(e)}")
