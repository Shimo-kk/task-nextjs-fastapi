from fastapi import status

URL = "api/v1/auth"


def test_signin_ok(client):
    """
    サインイン 正常
    """
    data = {"work_space_name": "test1.workspace", "email": "test1@example.com", "password": "testtest"}
    response = client.post(f"{URL}/signin", json=data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "work_space_id": 1,
        "name": "test user1",
        "email": "test1@example.com",
        "is_admin": True,
    }


def test_signin_ng_not_found(client):
    """
    サインイン 異常 存在しない
    """
    data = {"work_space_name": "test1.workspace", "email": "test@example.com", "password": "testtest"}
    response = client.post(f"{URL}/signin", json=data)

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_signin_ng_bad_request(client):
    """
    サインイン 異常 パスワードが誤り
    """
    data = {"work_space_name": "test1.workspace", "email": "test1@example.com", "password": "testtesttest"}
    response = client.post(f"{URL}/signin", json=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_signout_ok(client):
    """
    サインアウト 正常
    """
    response = client.get(f"{URL}/signout")

    assert response.status_code == status.HTTP_200_OK
