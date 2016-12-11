# Git clone then create some data
$ python3

``>>> from models import engine, db_session, Base, Department, Employee``  
``>>> Base.metadata.create_all(bind=engine)``  

``>>> # Fill the tables with some data``  
``>>> engineering = Department(name='Engineering')``  
``>>> db_session.add(engineering)``  
``>>> hr = Department(name='Human Resources')``  
``>>> db_session.add(hr)``  

``>>> peter = Employee(name='Peter', department=engineering)``  
``>>> db_session.add(peter)``  
``>>> roy = Employee(name='Roy', department=engineering)``  
``>>> db_session.add(roy)``  
``>>> tracy = Employee(name='Tracy', department=hr)``  
``>>> db_session.add(tracy)``  
``>>> db_session.commit()``  

Testing our GraphQL schema
--------------------------

We're now ready to test the API we've built. Let's fire up the server
from the command line.

.. code:: bash

    $ python ./app.py

     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Go to `localhost:5000/graphql <http://localhost:5000/graphql>`__ and
type your first query!

.. code::

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