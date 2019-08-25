def handle_error_by_throwing_exception():
  raise Exception("This is an exception")


def handle_error_by_returning_none(input_data):
  if input_data.isnumeric():
    return int(input_data)
  return None

def handle_error_by_returning_tuple(input_data):
  if input_data.isnumeric():
    return True, int(input_data)
  return False, () 
# fail can return anytihng with the false becuse dont matter

def filelike_objects_are_closed_on_exception(filelike_object):
  with filelike_object as f:
    f.do_something()
  # with = try-finally. Runs enter and exit automatically.
  # try: 
  #   filelike_object.open()
  #   filelike_object.do_something
  # finally :
    # filelike_object.close()