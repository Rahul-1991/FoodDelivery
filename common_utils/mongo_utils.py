import json
from bson import json_util


def serialize_document(result):
    x = [json.dumps(row, default=json_util.default) for row in result]
    return [json.loads(item) for item in x]