import pandas as pd
import sqlalchemy
import glob
import os
import re
def pascal_to_snake(s):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_files = glob.glob(script_dir+"/*.csv")
engine = sqlalchemy.create_engine('postgresql://username:password@host:port/database_name')
for file in csv_files:
    df = pd.read_csv(file, header=0, na_values='None')
    tablename = pascal_to_snake(os.path.splitext(os.path.basename(file))[0])
    df.to_sql(tablename, engine, if_exists='replace', index=False)
    with engine.connect() as conn:
        query = 'SELECT * FROM '+tablename
        result = conn.execute(sqlalchemy.text(query))
        df_from_table = pd.DataFrame(result.fetchall(), columns=result.keys())
    print(df_from_table.head())
inspector = sqlalchemy.inspect(engine)
print(inspector.get_table_names())
