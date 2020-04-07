import os
from django.utils import timezone


def function_a():
    print(timezone.now())


if __name__ == "__main__":
    function_a()
