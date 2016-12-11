Testing our GraphQL schema
--------------------------

We're now ready to test the API we've built. Let's fire up the server
from the command line.

    $ python ./app.py

     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Go to `localhost:5000/graphql <http://localhost:5000/graphql>`__ and
type your first query!

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