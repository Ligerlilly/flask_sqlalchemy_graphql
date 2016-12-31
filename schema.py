import code

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Department as DepartmentModel, Employee as EmployeeModel
from flask import request


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
            if e.id == args.get("id"):
                return e

class UpdateEmployee(graphene.Mutation):
    # Result field
    employee = graphene.Field(Employee)

    # The input fields
    class Input:
        name = graphene.String()
        id = graphene.Int()
        department = graphene.String()

    @classmethod
    def mutate(cls, instance, args, info, extra_ags):
        employees = EmployeeModel.query.all()
        if request.method == 'POST':
            name = args.get('name')
            for e in employees:
                if e.id == args.get('id'):
                    e.name = name
                    # code.interact(local=dict(globals(), **locals()))    
                    e.save()
                    return UpdateEmployee(employee=e)

# class UpdateEmployeeMutation(graphene.ObjectType):
#     updateEmployee = graphene.Field(UpdateEmployee)

class Mutations(graphene.ObjectType):
    updateEmployee = UpdateEmployee.Field()


schema = graphene.Schema(query=Query,  mutation=Mutations)
# schema = graphene.Schema(query=Query)

''' 
mutation M {
    updateEmployee(id: 1, name: "Jason") {
      employee {
        name
      }
    }
  }
'''

'''
{
allEmployees {
    edges {
      node {
        id
        name
        department {
          name
        }
      }
    }
  }
}
'''
