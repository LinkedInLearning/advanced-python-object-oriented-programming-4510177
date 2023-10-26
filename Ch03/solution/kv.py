# %%
import sqlite3
from collections.abc import MutableMapping

# %% Create
schema_sql = '''
CREATE TABLE IF NOT EXISTS kv (
    key TEXT PRIMARY KEY,
    value TEXT
);
'''

conn = sqlite3.connect(':memory:')
conn.executescript(schema_sql)

# %% Set
set_sql = '''
INSERT INTO kv
    (key, value)
VALUES
    (:key, :value)
ON CONFLICT (key) DO
    UPDATE SET key=:key
;
'''

entry = {'key': 'fish', 'value': 'water'}
conn.execute(set_sql, entry)

# %% Get
get_sql = '''
SELECT value
FROM kv
WHERE key = :key
'''

cur = conn.execute(get_sql, {'key': 'fish'})
print(cur.fetchone())

# %% Delete
del_sql = '''
DELETE FROM kv
WHERE key = :key
'''

conn.execute(del_sql, {'key': 'fish'})
cur = conn.execute(get_sql, {'key': 'fish'})
print(cur.fetchone())

# %% Keys
keys_sql = '''
SELECT key FROM kv
'''

entry = {'key': 'fish', 'value': 'water'}
conn.execute(set_sql, entry)
entry = {'key': 'horse', 'value': 'land'}
conn.execute(set_sql, entry)
for row in conn.execute(keys_sql):
    print('key:', row[0])

# %% Len
len_sql = '''
SELECT COUNT(key) FROM kv
'''

cur = conn.execute(len_sql)
row = cur.fetchone()
print('len:', row[0])

# %% DB
class DB(MutableMapping):
    """sqlite3 backed mapping"""
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.executescript(schema_sql)

    def __getitem__(self, key):
        cur = self.conn.execute(get_sql, {'key': key})
        row = cur.fetchone()
        if row is None:
            raise KeyError(key)
        return row[0]

    def __setitem__(self, key, value):
        with self.conn:
            entry = {'key': key, 'value': value}
            self.conn.execute(set_sql, entry)

    def __delitem__(self, key):
        with self.conn:
            self.conn.execute(del_sql, {'key': key})

    def __iter__(self):
        for row in self.conn.execute(keys_sql):
            yield row[0]

    def __len__(self):
        return self.conn.execute(len_sql).fetchone()[0]


# %% Test
db = DB('/tmp/animals.db')
db['fish'] = 'water'
db['horse'] = 'land'
print('<db> len:', len(db))
print('<db> fish:', db['fish'])
print('<db> keys:')
for key in db:
    print(f'- {key}')
print('<db> len:', len(db))
del db['fish']
print('<db> len (delete):', len(db))
