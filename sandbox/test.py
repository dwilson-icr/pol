from pol.objects import POLComponent

p = POLComponent()
print p.uuid
p.Export('test.pkl')
p2 = POLComponent()
p2.Import('test.pkl')
print p2.uuid
