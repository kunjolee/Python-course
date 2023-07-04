class TestClass:
    # Properties
    my_types = ('a tuple test', 'this is a tuple')

    # to declare an instance method you don't have to put any decorator and they receive the self instance. You have to instance the class to be able to use these methods. 
    def my_instance_method(self):
        print('This is my self instance', self)

    # Class method receives the class as a parameter. And you can call these class methods without instanciating the class 
    # If the method has on top a decorator named @classmethod. This mean the method is going to be a classmethod
    @classmethod
    def my_class_method(cls):
        print("I'm calling class method",cls)

    @classmethod
    def test_class_method(cls):
        print('Do you join here correclty?', cls)


    # It does not receive anything as a parameter. You can call this static method without instanciating the class. It is like a regular function, but you can't interact with the class because it does not receive either the class or self instance
    @staticmethod
    def my_static_method():
        print('Called static method')


TestClass.my_class_method()

