CSV to REST API
===============

Pass a CSV file to the program as argument, and the program results in a nice
REST API which can paginate, order and filter data.

Plus it supports redudancy-type high availability using a reverse proxy,
fallbacking to different socket files.


Preamble
--------

I made this project as a proof of skill for a job interview.

This project cannot be considered as production ready, since the exam requires
us to **not use a real database engine**, which is very disappointing.

As required, I respected all those points :

- Simplicity of the API (only 6 query parameters !)
- Nice technological choices (Python and generic libraries)
- Overall quality (elegant code and flake8)
- Performance (C bindings for sorting and filtering)
- Tests (unit tests and socketfile integration tests)
- Documentation (this friendly README filled with examples)
- Not using a real database engine



Launch the server
-----------------

This is the command how to start the REST server in a UNIX socket file which
can be later reverse-proxied using Nginx and such.

```bash
csv2rest \
    --csv ~/tvshow_views.csv \
    --blueprint ~/tvshow_views.yml \
    --socket ~/tvshow_views.sock
```

All the program parameters are shown in this example, which are simply :
`csv`, `blueprint` and `socket`.


High availability
-----------------

If the CSV changes for example every day, you will need to restart the
csv2rest process, causing a downtime.

To avoid that issue, what you can do is to run two instances of the csv2rest
process, the first socketfile being fallbacked by the second process socketfile
by the reverse proxy server.


Editing the blueprint
---------------------

The blueprint is a Yaml file which gives extra information about
the CSV file format and its columns types.

```yaml
has_header: true
delimiter: ,
quotechar: null
columns:
  - name: id
    type: string
  - name: provider
    type: string
  - name: title
    type: string
    strip: true
  - name: views
    type: integer
```

The columns orders in the blueprint must represent the same order as of inside
the CSV file. The `type` value can be whether `integer` or `string`.

When the type of the column is a `string`, the `strip` parameter is to trim
both the begin and the end of the string if needed. Is optional and if not
specified, defaults at `false`. Enabling this feature can greatly decrease
performances.

We recommend using a `string` type when the column is a hash, because its
way lighter to compare few `char` than to compare a whole n bits hash.


Querying REST API
-----------------

### Pagination

`n_row_per_page` is an integer which is optional and defaults at `1`.

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
`filter_val` is a string or integer, is optional and defaults at `not null`.

The `filter_col` value must be the column name as shown in the blueprint,
**and not** in the CSV header, which is completely ignored.


JSON REST API Querying examples
-------------------------------

In this example, we will have a CSV file representing a list of TV shows
and the number of views during the previous day.

The columns are : `id`, `provider`, `title`, `views`.

**Fetch the top 10 most watched TV shows for a specific provider :**

```json
{
    "n_row_per_page": 10,
    "sort_col": "views",
    "sort_order": -1,
    "filter_col": "provider",
    "filter_val": "XXX",
}
```

**TV shows in alphabetical order for a specific provider using pagination :**

```json
{
    "n_row_per_page": 10,
    "page_no": 42,
    "sort_col": "title",
    "sort_order": 1,
    "filter_col": "provider",
    "filter_val": "XXX",
}
```
