from app.services.auth_service import login_user, register_user


def test_login_user():
    result = login_user("new@example.com", "secret")

    assert result["email"] == "new@example.com"
    assert result["message"] == "login service called"


def test_register_user():
    result = register_user("new@example.com", "secret")

    assert result["email"] == "new@example.com"
    assert result["message"] == "register service called"
