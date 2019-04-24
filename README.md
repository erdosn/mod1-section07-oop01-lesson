
### Questions


### Objectives
YWBAT 
* explain when to use inheritance in OOP structured programming
* create child classes that inherit the attributes of a parent class
* build a child class that is specific to a use case

### Scenario
Now that we are able to build a class to better query our database let's extend it using child classes.  The reason for this is that each table has different inputs and structures that must be taken into consideration. We want to build classes that are specific to each table.


```python
from importlib import reload

import sql_connector as sc
import pandas as pd
import numpy as np

reload(sc)
```




    <module 'sql_connector' from '/Users/rafael/flatiron_dsc/curriculum/section07/mod1-section07-oop01-lesson/sql_connector.py'>




```python
conn = sc.SQLConnector(filename="data.sqlite")
```


```python
conn.tables
```




    ['orderdetails',
     'payments',
     'offices',
     'customers',
     'orders',
     'productlines',
     'products',
     'employees']




```python
products = sc.ProductsConn("data.sqlite")
```


```python
products.table_name
```




    'products'




```python
products.columns
```




    ['productCode',
     'productName',
     'productLine',
     'productScale',
     'productVendor',
     'productDescription',
     'quantityInStock',
     'buyPrice',
     'MSRP']


