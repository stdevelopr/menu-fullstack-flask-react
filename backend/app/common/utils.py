def clean_null_values_from_json(json_data):
    json_resp = {key: value for key, value in json_data.items() if value is not None}
    return json_resp