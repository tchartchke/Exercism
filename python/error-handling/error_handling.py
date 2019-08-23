def handle_error_by_throwing_exception():
  raise Exception("This is an exception")


def handle_error_by_returning_none(input_data):
  if input_data.isnumeric():
    return int(input_data)
  return None

def handle_error_by_returning_tuple(input_data):
  if input_data.isnumeric():
    return True, (int(input_data))
  return False, ()


def filelike_objects_are_closed_on_exception(filelike_object):
  if filelike_object.fail_something:
    filelike_object.close()
    filelike_object.do_something()
  filelike_object.close()
  filelike_object.do_something()
