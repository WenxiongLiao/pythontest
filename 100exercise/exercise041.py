class static_default:
    StaticVar = 5

    def get_var(self):
        self.StaticVar =  self.StaticVar + 1
        return self.StaticVar

if __name__ == '__main__':
    print(static_default.StaticVar)
    d = static_default()

    for i in range(5):
        print(d.get_var())