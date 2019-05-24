#trabalhando com objeto classe em python

class MinhaCLasse:

    membro_cls = 90
    def __init__(self):
        self.membro_inst = 0

    def func(self):
        print(self.membro_cls)
        print(self.membro_inst)
        print(MinhaCLasse.membro_cls)


i1 = MinhaCLasse()
#i1.func()

print(i1.membro_cls)
print(MinhaCLasse.membro_cls)