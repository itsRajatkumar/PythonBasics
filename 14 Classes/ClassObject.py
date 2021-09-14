class Dog:

    attr1='mammal'
    attr2='dog'

    def fun(self):
        print("I'm a ",self.attr1)
        print("I'm a ",self.attr2)

r=Dog()
print(r.attr1)
r.fun()
