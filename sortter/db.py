from loguru import logger
import psycopg2
from psycopg2.errors import UniqueViolation

from support_request import SupportRequest

class SortterDatabaseError(Exception):
    pass

_conn = None
_cur = None

def connect():
    global _conn
    global _cur
    _conn = psycopg2.connect("postgresql://postgres:postgres@db:5432/postgres")
    # _conn = psycopg2.connect("postgresql://postgres:postgres@0.0.0.0:5432/postgres")
    _cur = _conn.cursor()

def close():
    if _cur:
        _cur.close()
    if _conn:
        _conn.close()

def save_support_request(support_request: SupportRequest) -> None:
    sql = """
        insert into support_requests (first_name, last_name, email, phone, description)
        values (%(first_name)s,%(last_name)s,%(email)s,%(phone)s,%(description)s)
    """
    assert _conn, "Database connection failure"
    assert _cur, "Database connection failure"

    try:
        _cur.execute(sql, support_request.dict())
    except UniqueViolation:
        # just changing error type to not expose psycopg2 imports
        raise SortterDatabaseError("already added")
    finally:
        _conn.commit()

def get_support_requests() -> list[SupportRequest]:
    sql = """
        select first_name, last_name, email, phone, description from support_requests
    """
    assert _conn, "Database connection failure"
    assert _cur, "Database connection failure"

    requests: list[SupportRequest] = []
    _cur.execute(sql)
    for res in _cur.fetchall():
        requests.append(SupportRequest(
            first_name=res[0],
            last_name=res[1],
            email=res[2],
            phone=res[3],
            description=res[4],
        ))
    _conn.commit()
    return requests