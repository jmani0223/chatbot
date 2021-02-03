import pymysql

db = None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='lee6250',
        db='chatbot',
        charset='utf8'
        )
    print("DB 연결 성공")

    #테이블 삽입 sql 정의
    sql = '''
    INSERT tb_student(name, age, address) values('mani', 33, 'Korea')
        '''

    #테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB 연결 닫기 성공")