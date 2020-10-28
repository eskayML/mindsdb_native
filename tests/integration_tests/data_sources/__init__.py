import os
import json
import time
import random
import string

_var_name = 'DATABASE_CREDENTIALS_STRINGIFIED_JSON'
_var_value = os.getenv(_var_name)

assert _var_value is not None, _var_name + ' ' + 'is not set'

DB_CREDENTIALS = json.loads(_var_value)

# RUN_ID = os.getenv('GITHUB_RUN_ID')
RUN_ID = ''.join(
    random.Random(int(time.time() * 1e6)).choices(
        string.ascii_letters + string.digits,
        k=16
    )
)