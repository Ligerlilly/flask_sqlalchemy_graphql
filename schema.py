#import code
#code.interact(local=dict(globals(), **locals()))

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
    employee = graphene.Field(Employee, name=graphene.String())

    def resolve_employee(self, args, info, x):
        employees = EmployeeModel.query.all()

        for e in employees:
            if e.name == args.get("name"):
                return e

schema = graphene.Schema(query=Query)