"""
main.py
--------
Demonstrates various user scenarios including admin and normal user actions.
"""

from utils import validate_email, validate_age, validate_mobile, validate_gender, validate_blood_group, get_user_info, \
    list_all_users
from log import log_message


def main():
    """
    Main function demonstrating various user scenarios.
    """
    # Scenarios

    # Admin viewing a specific user information
    try:
        admin_username = "kiran"
        user_to_view = "ndines"
        user_info = get_user_info(user_to_view, admin_username, is_admin=True)
        log_message('info', f"Admin {admin_username} viewed user {user_to_view}: {user_info}")
    except (ValueError, PermissionError) as e:
        log_message('critical', str(e))

    # Admin listing all users
    try:
        admin_username = "nkiran"
        all_users = list_all_users(admin_username, is_admin=True)
        log_message('info', f"Admin {admin_username} listed all users: {all_users}")
    except (ValueError, PermissionError) as e:
        log_message('critical', str(e))

    # Normal user viewing their own information
    try:
        normal_username = "fake2"
        user_info = get_user_info(normal_username, normal_username, is_admin=False)
        log_message('info', f"Normal user {normal_username} viewed their information: {user_info}")
    except (ValueError, PermissionError) as e:
        log_message('critical', str(e))


# Run the main function
if __name__ == "__main__":
    main()
