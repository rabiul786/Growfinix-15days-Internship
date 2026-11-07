# Unit tests for Task 5 (run with: pytest)
import pytest
import student_system as ss


@pytest.fixture
def conn():
    # a fresh in-memory database for every test
    connection = ss.connect_db(":memory:")
    yield connection
    connection.close()


@pytest.fixture
def conn_with_data(conn):
    ss.add_student(conn, "101", "Rahim Khan", "20", "B.Tech", "82.5")
    ss.add_student(conn, "102", "Ayesha Begum", "21", "B.Sc", "91")
    return conn


# ----- validation -----
def test_valid_age():
    assert ss.is_valid_age("20") is True
    assert ss.is_valid_age("3") is True


def test_invalid_age():
    assert ss.is_valid_age("abc") is False
    assert ss.is_valid_age("-5") is False
    assert ss.is_valid_age("2") is False
    assert ss.is_valid_age("150") is False
    assert ss.is_valid_age("") is False


def test_valid_and_invalid_marks():
    assert ss.is_valid_marks("0") is True
    assert ss.is_valid_marks("100") is True
    assert ss.is_valid_marks("85.5") is True
    assert ss.is_valid_marks("101") is False
    assert ss.is_valid_marks("-1") is False
    assert ss.is_valid_marks("abc") is False


def test_valid_and_invalid_names():
    assert ss.is_valid_name("Rahim Khan") is True
    assert ss.is_valid_name("R2D2") is False
    assert ss.is_valid_name("") is False


def test_roll_number_rules():
    assert ss.is_valid_roll_no("CS101") is True
    assert ss.is_valid_roll_no("10 1") is False
    assert ss.is_valid_roll_no("1; DROP") is False


# ----- add / view -----
def test_add_and_get_student(conn):
    ss.add_student(conn, "101", "Rahim", "20", "B.Tech", "80")
    row = ss.get_student(conn, "101")
    assert row[1] == "Rahim"
    assert row[4] == 80.0


def test_duplicate_roll_number(conn_with_data):
    with pytest.raises(ValueError):
        ss.add_student(conn_with_data, "101", "Someone", "22", "B.Com", "60")


def test_add_with_wrong_input(conn):
    with pytest.raises(ValueError):
        ss.add_student(conn, "101", "Rahim", "abc", "B.Tech", "80")
    with pytest.raises(ValueError):
        ss.add_student(conn, "101", "Rahim", "20", "B.Tech", "500")
    with pytest.raises(ValueError):
        ss.add_student(conn, "101", "", "20", "B.Tech", "80")
    assert ss.get_all_students(conn) == []


def test_get_all_students(conn_with_data):
    assert len(ss.get_all_students(conn_with_data)) == 2


# ----- search -----
def test_search(conn_with_data):
    assert len(ss.search_students(conn_with_data, "rahim")) == 1
    assert len(ss.search_students(conn_with_data, "B.")) == 2
    assert ss.search_students(conn_with_data, "xyz") == []


def test_search_empty_word(conn_with_data):
    with pytest.raises(ValueError):
        ss.search_students(conn_with_data, "   ")


def test_sql_injection_does_not_work(conn_with_data):
    ss.search_students(conn_with_data, "'; DROP TABLE students; --")
    assert len(ss.get_all_students(conn_with_data)) == 2


# ----- update / delete -----
def test_update_student(conn_with_data):
    ss.update_student(conn_with_data, "101", "Rahim Khan", "21", "M.Tech", "95")
    row = ss.get_student(conn_with_data, "101")
    assert row[2] == 21
    assert row[3] == "M.Tech"
    assert row[4] == 95.0


def test_update_missing_student(conn_with_data):
    with pytest.raises(ValueError):
        ss.update_student(conn_with_data, "999", "Nobody", "20", "B.Tech", "50")


def test_update_with_wrong_marks(conn_with_data):
    with pytest.raises(ValueError):
        ss.update_student(conn_with_data, "101", "Rahim Khan", "20", "B.Tech", "-10")


def test_delete_student(conn_with_data):
    ss.delete_student(conn_with_data, "101")
    assert ss.get_student(conn_with_data, "101") is None


def test_delete_missing_student(conn_with_data):
    with pytest.raises(ValueError):
        ss.delete_student(conn_with_data, "999")


# ----- average -----
def test_average_marks(conn_with_data):
    assert ss.average_marks(conn_with_data) == 86.75


def test_average_with_no_students(conn):
    assert ss.average_marks(conn) == 0
