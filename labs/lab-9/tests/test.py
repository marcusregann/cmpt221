import pytest

from sqlalchemy import insert, select, text, delete
from models import User

# test db connection
def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# test to insert a user
# you can count this as one of your 5 test cases :)
def test_insert_user(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Marcus").first()

    assert selected_user is not None
    assert selected_user.LastName == "Regan"

# test to select a users password
def test_select_user(db_session):
    # Selectes Users Passwords
        select_stmt=select(User)
        db_session.execute(select_stmt)
        db_session.commit()

        selected_user = db_session.query(User).filter_by(Email="marcus.regan1@marist.edu").first()
        assert selected_user is not None
        assert selected_user.Password == "password"
# test to try and delete user
def test_delete_user_fail(db_session, sample_signup_input):
    # Deletes User
        delete_stmt=delete(User).where(User.Email==sample_signup_input('Email'))
        db_session.execute(delete_stmt)
        db_session.commit()

        deleted_user = db_session.query(User).filter_by(User.Email==sample_signup_input('Email')).first()
        assert deleted_user is not None
        assert deleted_user.PhoneNumber=="1234567"

def test_select_user_fail(db_session, sample_signup_input):
    # Selectes Users Passwords
        select_stmt=select(User)
        db_session.execute(select_stmt)
        db_session.commit()

        selected_user = db_session.query(User).filter_by(password="marcus.regan1@marist.edu").first()
        assert selected_user is not None
        assert selected_user.Password == "password"