import my_module
print(my_module.greeting("Hello Prabhat Rai"))
from my_module import greeting
print(greeting("Prabhat"))
from my_module import greeting,age
print(greeting("Prabhat"), "Age =", age)