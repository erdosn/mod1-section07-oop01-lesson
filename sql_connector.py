import sqlite3
import pandas as pd 


class SQLConnector(object):

    def __init__(self, filename=None):
        self.connection = sqlite3.Connection(filename)
        self.cursor = self.connection.cursor()
        self.tables = self.make_table_list()

    
    @staticmethod
    def build_select_all_query(table_name=None):
        return "select * from {};".format(table_name)

    
    @staticmethod
    def build_select_columns_query(columns=[], table_name=None):
        column_string = ",".join(columns)
        return "select {} from {};".format(column_string, table_name)


    def select_all_table(self, table_name):
        query = self.build_select_all_query(table_name)
        res = self.cursor.execute(query).fetchall()
        return res

    
    def select_columns_query(self, columns, table_name):
        query = self.build_select_columns_query(columns, table_name)
        res = self.cursor.execute(query).fetchall()
        return res

    
    def make_table_list(self):
        query = "select name from sqlite_master where type='table';"
        res = self.cursor.execute(query).fetchall()
        tables = [r[0] for r in res]
        return tables


class ProductsConn(SQLConnector):

    def __init__(self, filename):
        super().__init__(filename)
        self.table_name = "products"
        self.columns = self.get_column_list()

    
    def get_column_list(self):
        query = self.build_select_all_query(table_name=self.table_name)
        self.cursor.execute(query).fetchall()
        columns = [x[0] for x in self.cursor.description]
        return columns

