import  main_functions


class Dogs:
    def __init__(self, dog_breed):
        self.dog_breed = dog_breed

    def call_hello_world(self):
        main_functions.print_hello_world()

    def call_true(self):
        main_functions.print_true()