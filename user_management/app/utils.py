"""
utils.py
---------
Contains utility functions for validating user data and retrieving user information.
"""

import re
from log import log_message
from constants import VALID_COUNTRY_LIST, EXCLUDED_NUMBERS, VALID_GENDERS, VALID_BLOOD_GROUPS


def validate_email(email):
    """
    Validates the given email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ValueError: If the email format is invalid.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        log_message('error', f"Invalid email format: {email}")
        raise ValueError("Invalid email format")
    log_message('info', f"Valid email: {email}")
    return True


def validate_age(age):
    """
    Validates the given age.

    Args:
        age (int): The age to validate.

    Raises:
        ValueError: If the age is not within the valid range (0-120).

    Returns:
        bool: True if the age is valid, False otherwise.
    """
    if not (0 <= age <= 120):
        log_message('error', f"Invalid age: {age}")
        raise ValueError("Invalid age")
    log_message('info', f"Valid age: {age}")
    return True


def validate_mobile(mobile):
    """
    Validates the given mobile number.

    Args:
        mobile (str): The mobile number to validate.

    Raises:
        ValueError: If the mobile number format is invalid.

    Returns:
        bool: True if the mobile number is valid, False otherwise.
    """
    mobile_regex = r'^\d{10}$'
    if not re.match(mobile_regex, mobile):
        log_message('error', f"Invalid mobile number: {mobile}")
        raise ValueError("Invalid mobile number")
    if mobile in EXCLUDED_NUMBERS:
        log_message('info', f"Excluded mobile number: {mobile}")
        return False
    log_message('info', f"Valid mobile number: {mobile}")
    return True


def validate_gender(gender):
    """
    Validates the given gender.

    Args:
        gender (str): The gender to validate.

    Raises:
        ValueError: If the gender is not valid.

    Returns:
        bool: True if the gender is valid, False otherwise.
    """
    if gender.lower() not in VALID_GENDERS:
        log_message('error', f"Invalid gender: {gender}")
        raise ValueError("Invalid gender")
    log_message('info', f"Valid gender: {gender}")
    return True


def validate_blood_group(blood_group):
    """
    Validates the given blood group.

    Args:
        blood_group (str): The blood group to validate.

    Raises:
        ValueError: If the blood group is not valid.

    Returns:
        bool: True if the blood group is valid, False otherwise.
    """
    if blood_group.upper() not in VALID_BLOOD_GROUPS:
        log_message('error', f"Invalid blood group: {blood_group}")
        raise ValueError("Invalid blood group")
    log_message('info', f"Valid blood group: {blood_group}")
    return True


def get_user_info(username, current_user, is_admin):
    """
    Retrieves information for the specified user.

    Args:
        username (str): The username of the user whose information is to be retrieved.
        current_user (str): The username of the current user making the request.
        is_admin (bool): Whether the current user is an admin.

    Raises:
        PermissionError: If the current user is not authorized to view the requested user's information.
        ValueError: If the requested user is not found.

    Returns:
        dict: The user information if the user is found and the current user is authorized.
    """
    from data import data
    user_info = data['records'].get(username)
    if user_info:
        if username == current_user or is_admin:
            log_message('info', f"User info for {username}: {user_info}")
            return user_info
        else:
            log_message('warning', f"Unauthorized access attempt by {current_user} to view {username}'s information")
            raise PermissionError("Unauthorized access")
    else:
        log_message('error', f"User {username} not found")
        raise ValueError("User not found")


def list_all_users(current_user, is_admin):
    """
    Lists all users if the requester is an admin.

    Args:
        current_user (str): The username of the current user making the request.
        is_admin (bool): Whether the current user is an admin.

    Raises:
        PermissionError: If the current user is not authorized to list all users.

    Returns:
        dict: A dictionary containing all users' information.
    """
    from data import data
    if is_admin:
        log_message('info', f"Admin {current_user} listing all users")
        return data['records']
    else:
        log_message('warning', f"Unauthorized access attempt by {current_user} to list all users")
        raise PermissionError("Unauthorized access")
