import os
from django.utils import timezone


def function_a():
    os.system("echo a {} >> a.txt".format(timezone.now()))


if __name__ == "__main__":
    function_a()
