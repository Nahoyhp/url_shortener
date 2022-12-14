from cmath import e
import sqlite3
from textwrap import shorten

import my_util


class sqDb:
    conn = None
    cur = None

    _SQL_INSERT_URL_ = """ INSERT INTO urls VALUES(?, ?)"""
    _SQL_QUERY_URL_ = """SELECT shorten_url FROM urls WHERE url = ? """
    _SQL_REVERSE_QUERY__ = """SELECT url FROM urls WHERE shorten_url = ?"""

    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file, check_same_thread=False)
            self.curr = self.conn.cursor()
        except e:
            print(e)

    def insertOrReturn(self, url):
        # check if the url is already shorten before
        result = self.contain(url)
        if result != False:
            return result

        # calculate the shorten url
        chosen_url = my_util.generate_shorten_url()
        length = 5

        # check if the shorten url is already taken
        while self.reverse_lookup(chosen_url) != False:
            length += 1
            chosen_url = my_util.generate_shorten_url(length)

        print("Generate new shorten_url", chosen_url)

        tup = (url, chosen_url)
        self.curr.execute(self._SQL_INSERT_URL_, tup)
        self.conn.commit()

        return chosen_url

    def contain(self, url):
        self.curr.execute(self._SQL_QUERY_URL_, (url,))
        rows = self.curr.fetchall()

        if len(rows) == 0:
            print("Database doesn't contain url", url)
            return False

        shorten_url = rows[0][0]
        print("Database contain", url, "and the shorten is", shorten_url)
        return shorten_url

    def reverse_lookup(self, shorten_url):
        self.curr.execute(self._SQL_REVERSE_QUERY__, (shorten_url,))
        rows = self.curr.fetchall()

        if len(rows) == 0:
            return False

        url = rows[0][0]
        print("Database contain", url, "and the shorten is", shorten_url)
        return url
