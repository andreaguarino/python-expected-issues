def sample():
  try:
    do_something()
  except* OSError:
    handle_os_exception()
  except* ValueError:
    handle_value_exception()
