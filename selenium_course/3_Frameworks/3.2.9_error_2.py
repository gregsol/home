# https://stepik.org/lesson/36285/step/9?unit=162401

a, b = input().split()

def test_substring(full_string, substring):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"

test_substring(a, b)
