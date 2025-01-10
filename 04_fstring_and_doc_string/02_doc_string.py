#about doc string
#  A docstring is a string literal that occurs as the first statement in a 
# module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object.
# All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings.
# Public methods (including the __init__ constructor) should also have docstrings.
# A package may be documented in the module docstring of the __init__.py file in the package directory.
# Docstrings can be accessed using the __doc__ attribute of the object or using the help() function.

# Example
# Add a docstring to the function:
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything. 
    """ # this is doc string keep above the function body
    pass #pass means do nothing

print(my_function.__doc__)  # Do nothing, but document it.

