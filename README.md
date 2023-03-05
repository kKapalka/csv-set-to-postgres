# csv-set-to-postgres

A one-stop shop for moving all of your CSV files into your PostgreSQL database.

Run it once, leave it, and have your data stored neatly in the database.

## Packages required:
- Pandas
- SqlAlchemy

## How to use

- In line 10, change the line with the example Postgres connection data into your own database
- Move the script where your CSV files are
- Run the script

Done!

### CSV requirements:

- CSV files are expected to be written in PascalCase. Their names will get turned into a table name written in snake_case.


### Potential improvements

- Detect foreign keys in the generated tables, and auto-assign them.
- Do some better detection of the column data types. For now, the generated columns have one of these 3 types: bigint, text, or double_precision. For basic use it can work, but it would probably be a good idea to add a greater variety of the column types, like date, enum, varchar, and what not.