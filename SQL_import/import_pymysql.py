import pymysql

# connect MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="****", charset='utf8', db="sql_invoicing")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# send
sqlStr = "SELECT * FROM clients WHERE client_id > %s"
cursor.execute(sqlStr, [3, ])
data_list = cursor.fetchall()
print(data_list)

# print by rows
for row in data_list:
    print(row)

"""
attention:
When insert data, do not use normal format method in python
if you are quite familiar with C, this is quite like what you do scanf

sqlStr = "insert into tableName(colName1, colName2, colName3) value(%s, %s, %s)"
cursor.execute(sqlStr, ["value1", "value2", "value3"])
conn.commit()

also, you can named %s, ex:
sqlStr = "insert into tableName(colName1, colName2, colName3) value(%(name1)s, %(name2)s, %(name3)s)"
cursor.execute(sqlStr, {"name1": "value1", "name2": "value2", "name3":" "value3"})
conn.commit()
"""

# close
cursor.close()
conn.close()
