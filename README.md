CSV to REST API
===============

Pass a CSV file to the program as argument, and the program results in a nice
REST API which can paginate, order and filter data.

```
$ pipenv shell
$ csv2rest -h
usage: csv2rest [-h] csv blueprint port

Create a simple REST API socket file from a CSV file.

positional arguments:
  csv         Path of the CSV to open
  blueprint   Path of the blueprint JSON file about the CSV
  port        Port to open for the testing HTTP server

optional arguments:
  -h, --help  show this help message and exit
```


Preamble
--------

I made this project as a proof of skill for a job interview.
It just need WSGI implementation then it can be considered as production ready.

Checkout `README` from commit `540c5bc5c8e63a569006379a9432885646e7f444` for
production features (WSGI socket file, redundancy, page limiting, etc..).

I applied for a Java developer job, but we had the choice of the language,
so I decided to write this project in Python3 since its a very simple project.
Java would be super overkill in this case.

As required, I respected all those points :

- Simplicity of the API (only 6 query parameters !)
- Nice technological choices (Python and generic libraries)
- Overall quality (elegant code and flake8)
- Performance (chained comprehension list for sorting and filtering)
- Tests (some unit tests)
- Documentation (this friendly README filled with examples)
- Not using a real database engine


Installation procedure
----------------------

Python3.6 is required since this project is targeted for servers systems
and not directly for consumers.

You will first need to ensure that pipenv is installed :

```bash
pip3 install pipenv
```

Fetch the repository :

```bash
git clone https://github.com/dctremblay/csv2rest.git
cd csv2rest
```

Initialize pipenv and dependencies :

```bash
pipenv install
```

Do not forget to enter in the env shell :

```bash
pipenv shell
python3 csv2rest
```


Launch the server
-----------------

This is the command how to start the REST server in a local port :

```bash
csv2rest \
    ~/tvshow_views.csv \
    ~/tvshow_views.json \
    4242
```

All the program positional arguments are shown in this example,
which are simply :`csv`, `blueprint` and `port`.


Editing the blueprint
---------------------

The blueprint is a JSON file which gives extra information about
the CSV file format and its columns types.

```json
{
    "encoding": "iso-8859-1",
    "has_header": true,
    "delimiter": ",",
    "quotechar": "",
    "columns": [
        {
            "name": "id",
            "type": "string"
        },
        {
            "name": "provider",
            "type": "string"
        },
        {
            "name": "title",
            "type": "string"
        },
        {
            "name": "views",
            "type": "integer"
        }
    ]
}
```

The columns orders in the blueprint must represent the same order as of inside
the CSV file. The `type` value can be `disabled`, `integer` or `string`.

If the `type` is set to `disabled`, this will cause this field to be hidden
in the output to client. It's still required to specify a unique field name.

We recommend using a `string` type when the column is a hash, because its
way lighter to compare few `char` than to compare a whole n bits hash.


Querying REST API
-----------------

The presented parameters for the requests are GET parameters that you must
put into the URL. (ex: `/?page_n_row=10&page_no=4`)

### Pagination

`page_n_row` is an integer which is optional and defaults at `1`.

`page_no` is an integer which is optional, begins and defaults at `0`.


### Sorting

`sort_col` is a string which is optional and has no default.

`sort_order` is a signed byte which defaults at 0 :
```
-1 : order descending
 0 : no order (as in the CSV)
 1 : order ascending
```

### Filtering

**Disclaimer :** The filtering feature is very simplistic and may be enhanced
in the future using a JSON DOM Query filter style.

`filter_col` is a string, the name of the column to filter, which is optional.
It must be the column name as shown in the blueprint, **and not** in the
CSV header, which is completely ignored.

`filter_val` is a string or integer, is optional and defaults at `is not null`.


JSON REST API Querying examples
-------------------------------

In this example, we will have a CSV file representing a list of TV shows
and the number of views during the previous day.

The columns are : `id`, `provider`, `title`, `views`.

Those are represented as JSON format, but its only for human readable
example purpose. For real they are GET parameters (as also shown).

**Top 10 most watched TV shows for a specific provider :**

`/?page_n_row=10&sort_col=views&sort_order=-1&filter_col=provider&filter_val=XXX`

```json
{
    "page_n_row": 10,
    "sort_col": "views",
    "sort_order": -1,
    "filter_col": "provider",
    "filter_val": "XXX",
}
```

**TV shows in alphabetical order for a specific provider using pagination :**

`/?page_n_row=10&page_no=42&sort_col=title&sort_order=1&filter_col=provider&filter_val=XXX`

```json
{
    "page_n_row": 10,
    "page_no": 42,
    "sort_col": "title",
    "sort_order": 1,
    "filter_col": "provider",
    "filter_val": "XXX",
}
```

**Top 20 most watched TV shows :**

`/?page_n_row=20&sort_col=views&sort_order=-1`

```json
{
    "page_n_row": 20,
    "sort_col": "views",
    "sort_order": -1,
}
```


How to run tests
----------------


Do not forget to enter in the env shell :

```
pipenv shell
```

Just go in the package folder and write this command :

```bash
python3 -m unittest
```

Before commiting, you will need to ensure linting is ok :

```bash
flake8 .
```


License
-------

This project is released under Apache License 2.0, don't hesitate to read
the `LICENSE` file for further informations.


Contributing to this tool
-------------------------

We absolutely appreciate patches, feel free to contribute
directly on the GitHub project.

Repositories / Development website / Bug Tracker:

https://github.com/dctremblay/csv2rest

Do not hesitate to join us and post comments, suggestions,
questions and general feedback directly on the issues tracker.

Author : David Côté-Tremblay <imdc.technologies@gmail.com>
