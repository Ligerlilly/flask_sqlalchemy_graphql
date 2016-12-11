# Creating some data
$ python3

>>>> from models import engine, db_session, Base, Department, Employee
>>>> Base.metadata.create_all(bind=engine)

>>>> # Fill the tables with some data
>>>> engineering = Department(name='Engineering')
>>>> db_session.add(engineering)
>>>> hr = Department(name='Human Resources')
>>>> db_session.add(hr)

>>>> peter = Employee(name='Peter', department=engineering)
>>>> db_session.add(peter)
>>>> roy = Employee(name='Roy', department=engineering)
>>>> db_session.add(roy)
>>>> tracy = Employee(name='Tracy', department=hr)
>>>> db_session.add(tracy)
>>>> db_session.commit()

# Testing our GraphQL schema 
We’re now ready to test the API we’ve built. Let’s fire up the server from the command line.

$ python3 ./app.py

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)