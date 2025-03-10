# pip install flask flask-restful sqlalchemy

from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine, text
from flask import jsonify

db_connect = create_engine("sqlite:///chinook.db")


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(text("select EmployeeId from employees"))
        result = {"employees": [i[0] for i in query.cursor.fetchall()]}
        conn.close()
        return jsonify(result)


class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        sql = text("select trackid, name, composer, unitprice from tracks;")
        query = conn.execute(sql)
        result = {"data": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        conn.close()
        return jsonify(result)


class EmployeesName(Resource):
    def get(self, employee_id: int):
        conn = db_connect.connect()
        query = conn.execute(
            text("select * from employees where EmployeeId =%d " % int(employee_id))
        )
        result = {"data": [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        conn.close()
        return jsonify(result)


def main():

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(Employees, "/employees")  # Route_1
    api.add_resource(Tracks, "/tracks")  # Route_2
    api.add_resource(EmployeesName, "/employees/<employee_id>")  # Route_3

    app.run(port=5000)

    db_connect.dispose()


if __name__ == "__main__":
    main()
