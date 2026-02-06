from database import db
import hashlib
import uuid


def encrypt_password(password):
    """
    Encrypts a plain text password using SHA-256 with a random salt.

    The generated hash is stored in the format:
    <hashed_password>:<salt>

    :param password: Plain text password
    :return: Hashed password with salt
    """
    # Generate a random salt
    salt = uuid.uuid4().hex

    # Create SHA-256 hash using salt + password
    encrypted_pwd = hashlib.sha256(
        salt.encode() + password.encode('utf-8')
    )

    # Store hash and salt together
    encrypted_pwd = encrypted_pwd.hexdigest() + ":" + salt
    return encrypted_pwd


def verify_password(password, hashed_password):
    """
    Verifies a plain text password against a stored hashed password.

    :param password: Plain text password provided by the user
    :param hashed_password: Stored password in the format hash:salt
    :return: True if the password is valid, False otherwise
    """
    # Split stored hash and salt
    hash_pass, salt = hashed_password.split(":")

    # Recalculate hash using the stored salt
    new_hashpwd = hashlib.sha256(
        salt.encode() + password.encode('utf-8')
    ).hexdigest()

    # Compare hashes
    return hash_pass == new_hashpwd


def sign_up(username=None, password=None):
    """
    Registers a new user in the database.

    :param username: Username provided by the user
    :param password: Plain text password
    :return: Dictionary with operation result
    """
    connection = None

    # Basic input validation
    if not username or username == " ":
        print("Invalid username")
        return {"success": False, "validate": False}

    if not password or password == " ":
        print("Invalid password")
        return {"success": False, "validate": False}

    # Encrypt password before storing it
    pw_secure = encrypt_password(password)

    # SQL query to insert the new user
    query = """INSERT INTO users (username, password) VALUES (%s, %s)"""

    try:
        # Get database connection
        connection = db.get_connection()

        # Execute query
        with connection.cursor() as cursor:
            cursor.execute(query, (username, pw_secure))
            connection.commit()

        print("Sign up successful")
        return {"username": username, "success": True, "validate": True}

    except Exception as e:
        print("Sign up failed:", e)
        return {"success": False}

    finally:
        # Always release the database connection
        db.release_connection(connection)


def login(username, password):
    """
    Authenticates a user by verifying username and password.

    :param username: Username provided by the user
    :param password: Plain text password
    :return: Dictionary with authentication result
    """
    connection = None

    # Basic input validation
    if not username or not password or username == " " or password == " ":
        print("Invalid credentials")
        return {"success": False, "validate": False}

    # SQL query to retrieve the user's hashed password
    query = """SELECT password FROM users WHERE username = %s"""

    try:
        # Get database connection
        connection = db.get_connection()

        with connection.cursor() as cursor:
            cursor.execute(query, (username,))
            record = cursor.fetchone()

        # User not found
        if not record:
            print("User not found")
            return {"username": username, "success": False, "validate": False}

        # Verify password
        if verify_password(password, record[0]):
            return {"username": username, "success": True, "validate": True}
        else:
            return {"username": username, "success": False, "validate": False}

    except Exception as e:
        print("Login failed:", e)

    finally:
        # Always release the database connection
        db.release_connection(connection)
