from fastapi import status

URL = "api/v1/user"


def test_create_ok(client):
    """
    作成 正常
    """
    data: dict[str, str] = {
        "work_space_id": 1,
        "name": "test user",
        "email": "test@example.com",
        "password": "testtest",
        "is_admin": True,
    }

    response = client.post(f"{URL}", json=data)

    assert response.status_code == status.HTTP_200_OK


def test_create_ng_already_exists(client):
    """
    作成 異常 重複
    """
    data: dict[str, str] = {
        "work_space_id": 1,
        "name": "test user",
        "email": "test1@example.com",
        "password": "testtest",
        "is_admin": True,
    }

    response = client.post(f"{URL}", json=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_all_user_ok(client):
    """
    全件取得 正常
    """
    response = client.get(f"{URL}/1")

    assert response.status_code == status.HTTP_200_OK


def test_update_ok(client):
    """
    更新 正常
    """
    data: dict[str, str] = {
        "id": 1,
        "name": "test user updated",
        "is_admin": True,
    }

    response = client.put(f"{URL}", json=data)

    assert response.status_code == status.HTTP_200_OK


def test_delete_ok(client):
    """
    削除 正常
    """
    response = client.delete(f"{URL}/1")

    assert response.status_code == status.HTTP_200_OK
