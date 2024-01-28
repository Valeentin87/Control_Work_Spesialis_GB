import MySQLdb
db = MySQLdb.connect('localhost', 'val87', '12345', 'nursery')
cursor = db.cursor()
query = '''SELECT * FROM nursery'''
cursor.execute(query)
ls = cursor.fetchall()
print(ls)
cursor.close()



def count_animals():
    '''возвращает количество животных, которые есть в питомнике'''
    cursor = db.cursor()
    query = '''SELECT COUNT(*) FROM nursery'''
    cursor.execute(query)
    count_rows = cursor.fetchone()
    print(count_rows)
    cursor.close()
    return count_rows[0]

if __name__ == '__main__':
    pass