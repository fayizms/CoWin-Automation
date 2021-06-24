string_json = str({'userID': 3579})             # This is the string format of a json file converted by using str(). This file is jsonc(json with comments) which doesn't suport variable names in single quotes, but only support double quotes
print(string_json)                              # Just printing the original file
string_json = string_json.replace("'", '"' )    # Now replacing the original single quotes with double quotes with replace method of string
print(string_json)                              # Now printing again
