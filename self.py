class person:
    name="Aarati"
    occupation="Computer engineer"
    networth=20
    def info(self):
        print(f"{self.name} is a {self.occupation} with a networth of a {self.networth}")

a=person()
a.name="Jatin"
a.occupation="Bussinessmaan"
a.networth=100
print(a.name,a.occupation,a.networth)
print(a.info())
b=person()
print(b.info())