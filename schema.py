import code

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Department as DepartmentModel, Employee as EmployeeModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee)
    employee = graphene.Field(Employee, id=graphene.Int())

    def resolve_employee(self, args, info, x):
        employees = EmployeeModel.query.all()

        for e in employees:
            #code.interact(local=dict(globals(), **locals()))
            if e.id == args.get("id"):
                return e

schema = graphene.Schema(query=Query)