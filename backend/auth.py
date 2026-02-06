from database import db
import hashlib
import uuid


def encrypt_password(password):
    salt = uuid.uuid4().hex
    encrypted_pwd = hashlib.sha256(salt.encode() + password.encode('utf-8'))
    encrypted_pwd = encrypted_pwd.hexdigest() + ":" + salt
    return encrypted_pwd


def verify_password(password, hashed_password):
    hash_pass, salt = hashed_password.split(":")
    new_hashpwd = hashlib.sha256(salt.encode() + password.encode('utf-8'))
    new_hashpwd = new_hashpwd.hexdigest()
    if hash_pass == new_hashpwd:
        return True
    else:
        return False


def sign_up(username=None, password=None):
    connection = None
    if not username or username == " " :
        print("Utente non valido")
        return({"success": False, "validate":False})
    if not password or password == " " :
        print("Password non valido")
        return({"success": False, "validate":False})
    pw_secure = encrypt_password(password)
    query = """INSERT INTO users (username, password) VALUES (%s,%s)"""
    try:
        connection = db.get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query, (username, pw_secure))
            connection.commit()
        print("Sign up successful")
        return ({"username":username, "success": True, "validate":True})
    except Exception as e:
        print("Sign up failed: ", e)
        return ({"success": False})
    finally:
        db.release_connection(connection)

def login(username, password):
    connection = None
    if not username or not password or username == " " or password == " ":
        print("Credenziali non valide")
        return {"success":False, "validate":False}
    query = """SELECT password FROM users WHERE username = %s"""
    try:
        connection = db.get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query, (username,))
            record = cursor.fetchone()
        if not record:
            print("Utente non trovato")
            return {"username": username, "success": False, "validate": False}
        if verify_password(password, record[0]):
            return {"username":username, "success":True, "validate":True}
        else:
            return {"username":username, "success":False, "validate":False}
    except Exception as e:
        print("Sign up failed: ", e)
    finally:
        db.release_connection(connection)
