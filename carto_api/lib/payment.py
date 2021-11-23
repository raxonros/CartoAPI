from lib.db import Database


class Payment:

    def __init__(self):
        self.db = Database()

    def get_total_payment(self, date_init, date_final, postal_code_id):
        try:
            if postal_code_id != None:
                sql_total_payment_query = f'''SELECT SUM(amount)\
                FROM paystats\
                WHERE p_month BETWEEN '{date_init}' AND '{date_final}'\
                AND postal_code_id = {postal_code_id};'''

            else:
                sql_total_payment_query = f'''SELECT SUM(amount)\
                FROM paystats\
                WHERE p_month BETWEEN '{date_init}' AND '{date_final}';'''

            conn = self.db.connect()
            cursor = self.db.query(sql_total_payment_query, conn)

            for i in cursor.fetchall():
                result = {"total_payment":  i[len(i)-1]}

            self.db.close_connect(conn)

            return result

        except Exception as e:
            print(e)

    def get_age_gender_payment(self, date_init, date_final, gender, age, postal_code_id ):
        try:
            if postal_code_id != None:
                sql_age_gender_query = f'''SELECT SUM(amount) \
                FROM paystats \
                WHERE (p_month BETWEEN '{date_init}' AND '{date_final}') \
                AND p_gender = '{gender}' \
                AND p_age = '{age}' \
                AND postal_code_id = {postal_code_id};'''
            else:
                sql_age_gender_query = f'''SELECT SUM(amount) \
                FROM paystats \
                WHERE (p_month BETWEEN '{date_init}' AND '{date_final}') \
                AND p_gender = '{gender}' \
                AND p_age = '{age}';'''

            conn = self.db.connect()
            cursor = self.db.query(sql_age_gender_query, conn)

            for i in cursor.fetchall():
               result={"age":age, "gender": gender, "postal_code":postal_code_id, "paid_amount": i[len(i)-1] }

            self.db.close_connect(conn)

            return result

        except Exception as e:
            print(e)

    def get_payment_by_postal_code(self, date_init, date_final):
        total_payment = []

        sql_total_payment_by_postal_code_query = f'''SELECT postal_code_id, SUM(amount) \
            FROM paystats \
            WHERE (p_month BETWEEN '{date_init}' AND '{date_final}')\
            GROUP BY postal_code_id;'''

        try:
            conn = self.db.connect()
            cursor = self.db.query(sql_total_payment_by_postal_code_query, conn)

            for i in cursor.fetchall():
                total_payment.append({"postal_code":i[0], "amount":i[1]})

            return total_payment
        except Exception as e:
            print(e)

