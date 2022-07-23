def create_stack():
    """Creating an empty stack."""
    return []


def check_stack(stack):
    if type(stack) == 'array':
        return True
    return False


def check_empty(stack):
    """Return the true if the stack is empty"""
    if not check_stack(stack):
        return 'Value specified is not a stack'
    if len(stack) == 0:
        return True
    return False


def push(stack, value):
    """Push an item, if he doesn't exist already, am return the stack"""
    if not check_stack(stack):
        return 'Value specified is not a stack'
    if not stack.__contains__(value):
        return stack.append(value)


val = create_stack()

print(check_stack(val))
print(check_empty(val))
push(val, "Hello")
print(val)
