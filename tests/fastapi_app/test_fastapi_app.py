from fastapi.testclient import TestClient
from pytest_mock import MockFixture

from remo import app


ROOT_FOLDER_PATCHED = "/root_folder"


client = TestClient(app)


def test_search(
    mocker: MockFixture,
):
    mocker.patch(
        "remo.root_folder",
        ROOT_FOLDER_PATCHED,
    )
    
    mock_search_tree = (
        mocker.patch(
            "remo.utils.search_tree",
            return_value=["result1", "result2"],
        )
    )

    # Input data for the test
    test_data = {
        "query": "test_query"
    }

    response = client.post("/search", json=test_data)

    assert response.status_code == 200

    assert response.json() == {
        "results": ["result1", "result2"]
    }

    mock_search_tree.assert_called_once_with(
        ROOT_FOLDER_PATCHED,
        "test_query",
    )
