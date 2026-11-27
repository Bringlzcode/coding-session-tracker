
from db import init_db , add_seshn , del_seshn , list_seshn
from pathlib import Path
import sqlite3

def test_init_db(tmp_path):
    db_file = str(tmp_path / "sessions.db")
    init_db(db_file)
    assert Path(db_file).exists()

    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='sessions'"
    )
    row = cur.fetchone()
    con.close()

    assert row is not None
    assert row[0] == "sessions"
    
    
    
def test_add_seshn(tmp_path):
    
    db_file = str(tmp_path / "sessions.db")
    init_db(db_file)
    ok , session_id = add_seshn("SQLite" , 1.5 , db_file)
    assert ok is True
    assert isinstance(session_id,  int)


def test_del_seshn(tmp_path):
    db_file = str(tmp_path / "sessions.db")
    init_db(db_file)

    ok, session_id = add_seshn("SQLite", 1.5, db_file)
    assert ok is True
    assert del_seshn(session_id, db_file) is True
    # Call your delete function here with session_id and db_file
    # and assert that it succeeded
    
    
def test_list_seshn(tmp_path):
    db_file = str(tmp_path / "sessions.db")
    init_db(db_file)

    ok, session_id = add_seshn("SQLite", 1.5, db_file)
    assert ok is True

    rows, total_hrs, weekly_sessions, seshn_hrs , weekly_topics = list_seshn(db_file)

    assert isinstance(rows, list)
    assert len(rows) == 1
    assert total_hrs == 1.5
    assert sum(seshn_hrs) == 1.5
    assert len(weekly_sessions) == 1
    assert len(weekly_topics) == 1
    
    