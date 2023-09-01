```
 .
├──  project
│   ├──  mutation                # Mutation Root type is created by combining all the
│   │   ├──  __init__.py         # mutations together into a single root-level object.
│   │   └──  add_post.py
│   ├──  query                   # same for Query Root type
│   │   ├──  __init__.py
│   │   ├──  posts.py
│   │   └──  post.py
│   └──  types                   # GraphQL types are created by defining a class
│       ├──  __init__.py         # inside `[type_name]/__init__.py` file
│       ├──  comment
│       │   ├──  __init__.py
│       │   └──  post.py         # nested resolvers are defined inside `[type_name]/[field_name].py`
│       └──  post
│           ├──  __init__.py
│           └──  comments.py
```