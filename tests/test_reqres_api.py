from apis.reqres_api import *

def test_create_read_update_delete_user():
    # Create user
    create_res = create_user("morpheus", "leader")
    assert create_res.status_code == 201
    user_data = create_res.json()
    user_id = user_data.get("id")
    assert user_id is not None

    # Note: GET might fail since ReqRes doesn’t persist data
    get_res = get_user(user_id)
    assert get_res.status_code in [200, 404]  # 404 is acceptable

    # Update user
    update_res = update_user(user_id, "neo", "zion captain")
    assert update_res.status_code == 200
    assert update_res.json().get("job") == "zion captain"

    # Delete user
    delete_res = delete_user(user_id)
    assert delete_res.status_code == 204
