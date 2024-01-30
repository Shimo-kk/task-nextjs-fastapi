from fastapi import status

URL = "api/v1/work-space"


def test_create_ok(client):
    """
    作成 正常
    """
    data: dict[str, str] = {
        "work_space_name": "test.workspace",
        "admin_name": "test admin",
        "admin_email": "test.admin@example.com",
        "admin_password": "testtest",
    }

    response = client.post(f"{URL}", json=data)

    assert response.status_code == status.HTTP_200_OK


def test_create_ng_already_exists(client):
    """
    作成 異常 重複
    """
    data: dict[str, str] = {
        "work_space_name": "test1.workspace",
        "admin_name": "test admin",
        "admin_email": "test.admin@example.com",
        "admin_password": "testtest",
    }

    response = client.post(f"{URL}", json=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_create_ng_valid_error(client):
    """
    作成 異常 重複
    """
    data: dict[str, str] = {
        "work_space_name": "test.workspace",
        "admin_name": "test admin",
        "admin_email": "test.admin",
        "admin_password": "testtest",
    }

    response = client.post(f"{URL}", json=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_ok(client):
    """
    取得 正常
    """
    response = client.get(f"{URL}/1")

    assert response.status_code == status.HTTP_200_OK


def test_get_ng_not_found(client):
    """
    取得 異常 存在しない
    """
    response = client.get(f"{URL}/4")

    assert response.status_code == status.HTTP_404_NOT_FOUND
