import per4m
import per4m.offgil
import per4m.pytrace
import per4m.script


assert per4m.__version__ == "0.1.0"
assert hasattr(per4m.pytrace, "start")

per4m.pytrace.start()


def traced_function(value):
    return value + 1


assert traced_function(41) == 42
per4m.pytrace.stop()
