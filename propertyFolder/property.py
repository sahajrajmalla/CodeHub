class bio:
    def __init__(this, age):
        this.age = age

    def getvalue(this):
        print("getting values")
        return this.age

    def setvalues(this, age):
        print("setting values")
        if this.age < 0:
            raise ValueError
        else:
            this.age = age

    def delvalues(this):
        print("deleting values!")
        del this.age

    ages = property(getvalue, setvalues, delvalues)


sahaj = bio(20)
print(sahaj.ages)

sahaj.ages = 18

print(sahaj.ages)
