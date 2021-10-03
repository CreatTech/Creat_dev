

class pycharm:

    def execute(self):
        print("Compiling")
        print("Running")



class myEditor:

    def execute(self):
        print("spell check")
        print("convention check")
        print("Compiling")
        print("Running")


class laptop:

    def code(self,ide):
        ide.execute()

ide = pycharm()
lap1 = laptop()
lap1.code(ide)