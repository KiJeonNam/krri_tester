import cx_Oracle
import config
import pandas as pd

class krri_dataservice():
    def __init__(self):
        localhost = 'localhost'
        port = 1521
        sid = 'orcl'

        user = 'c##db'
        pw = '1234'

        self.dsn = cx_Oracle.makedsn(localhost, port, sid)
        self.con = cx_Oracle.connect(user, pw, self.dsn)

        self.cur = self.con.cursor()
        print('DB is connected')

    def data_select(self, value):
        parameter = [value]
        select_query = """
        select *
        from msr_data
        where key =: value
        --where TIME <: value
        """
        df = pd.read_sql_query(select_query, con=self.con, params=parameter)
        return df

    def data_insert(self, data):
        parameter = data
        insert_query = """
        insert into msr_data
        (key, time, location, pm, ppm)
        values
        (:1, :2, :3, :4, :5)"""
        return
