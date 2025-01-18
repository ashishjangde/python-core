# hybrid inheritance is a combination of more than one type of inheritance.
class base_class :
    pass

class derived_class(base_class):
    pass

class derived_class_one(base_class):
    pass;

class derived_derived_class(derived_class, derived_class_one):
    pass

# heirarchy inheritance is a type of inheritance in which more than one derived class is inherited from a single base class.

class base_class_one:
    pass

class derived_class_one(base_class_one):
    
    pass

class derived_class_two(derived_class_one):
    pass

class derived_class_three(derived_class_one):
    pass

class derived_class_four(derived_class_one):
    pass
