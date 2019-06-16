class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blu",10)
alu=parrot("alu",20)
print("blu is a {}".format(blu.__class__.species))
print("alu is a {}".format((alu.__class__.species)))

print("{} is {} year old".format(blu.name,blu.age))
print("{} is {} year old".format(alu.name,alu.age))