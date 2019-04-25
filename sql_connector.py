import sqlite3
import pandas as pd 

import matplotlib.pyplot as plt


class SQLConnector(object):

    def __init__(self, filename=None):
        self.connection = sqlite3.Connection(filename)
        self.cursor = self.connection.cursor()
        self.tables = self.make_table_list()


    @staticmethod
    def build_select_all_query(table_name=None):
        """
        select * from table;
        """
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
        self.tables = None


    def get_column_list(self):
        query = self.build_select_all_query(table_name=self.table_name)
        self.cursor.execute(query).fetchall()
        columns = [x[0] for x in self.cursor.description]
        return columns
    
    
    def select_all_products(self):
        res = self.select_all_table(table_name=self.table_name)
        return res

    
    def products_to_pandas(self):
        # builds the select * from products;
        query = self.build_select_all_query(table_name=self.table_name)

        # using pandas to read the query and passing in the connection
        df = pd.read_sql(query, self.connection)
        return df

    
    def load_products_dataframe(self):
        df = self.products_to_pandas()
        df["quantityInStock"] = df.quantityInStock.astype(int)
        df["MSRP"] = df.MSRP.astype(float)
        df["buyPrice"] = df.buyPrice.astype(float)
        return df
    

    def sort_table(self, df, column, ascending=True):
        df = df.sort_values(by = column, ascending=ascending)
        return df


    
    def plot_histogram(self, column_name, bins=20, show=False):
        df = self.load_products_dataframe()
        fig = plt.figure(figsize=(10, 10))
        plt.hist(df[column_name], bins=bins)
        plt.title(column_name.capitalize() + " Histogram")
        if show:
            plt.show()
        return fig


    def get_quantity_of_product(self, product_code):
        query = "select quantityInStock from {} where productCode = '{}';".format(self.table_name, product_code)
        res = self.cursor.execute(query).fetchall()[0][0]
        return int(res)


if __name__=="__main__":
    print("hello world")
    products = ProductsConn(filename="data.sqlite")
    print(vars(products))
    print(products.plot_histogram("MSRP", show=True))


