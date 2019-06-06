import copy

class CallableDict(dict):
    ...

    def __getitem__(self, key):
        val = super().__getitem__(key)
        if callable(val):
            return val()
        return val


class CounterMachine():
    def __init__(self, input):
        self.registers = input
        self.rule = 1
        self.halt = False
        # pass

    def run(self):
        print(self.registers)
        # self.increment('R0')
        # print(self.registers)
        # self.decrement('R6')
        self.multiply('R6', 'R7')
        print(self.registers)

    def set_halt(self, bool):
        self.halt = bool

    def increment(self, Ri):
        for key, value in self.registers.items():
            last = value[-1]
            if key == Ri:
                self.registers[key].append(last+1)
            else:
                self.registers[key].append(last)
        self.rule += 1

    def set2zero(self, Ri):
        for key, value in self.registers.items():
            last = value[-1]
            if key == Ri:
                self.registers[key].append(0)
            else:
                self.registers[key].append(last)
        self.rule += 1

    def if_equal(self, Ri, Rj, jump):
        for key, value in self.registers.items():
            last = value[-1]
            # print("last", last)
            if key == Ri:
                # print("other", self.registers[Rj][-1])
                if last == self.registers[Rj][-1]:
                    self.rule = jump
                    # print(rule)
            self.registers[key].append(last)
        if self.rule != jump:
            self.rule += 1

    def copy(self, Ri, Rj):
        previous_rule = copy.deepcopy(self.rule)
        self.rule = 1
        self.halt = False
        rules = CallableDict({1: lambda: self.set2zero(Rj),
                              2: lambda: self.if_equal(Ri, 'R00', jump=8),
                              3: lambda: self.increment('R00'),
                              4: lambda: self.increment(Rj),
                              5: lambda: self.if_equal(Ri, Rj, jump=7),
                              6: lambda: self.if_equal('R00', Rj, jump=3),
                              7: lambda: self.set2zero('R00'),
                              8: lambda: self.set_halt(True)})

        while not self.halt:
            # print("R4: ", self.registers['R4'][-1])
            # print("C", self.rule)
            rules[self.rule]
        self.halt=False
        self.rule = previous_rule+1

    def decrement(self, Ri):
        previous_rule = copy.deepcopy(self.rule)
        self.rule = 1
        rules = CallableDict({1: lambda: self.increment('R2'),
                              2: lambda: self.if_equal('R2', Ri, jump=5),
                              3: lambda: self.increment('R0'),
                              4: lambda: self.if_equal('R0', 'R2', jump=1),
                              5: lambda: self.copy('R0', Ri),
                              6: lambda: self.set2zero('R2'),
                              7: lambda: self.set2zero('R0'),
                              8: lambda: self.set_halt(True)})

        while not self.halt:
            # print("R0: ", self.registers['R0'][-1])
            # print("R4: ", self.registers['R4'][-1])
            # print("D", self.rule)
            rules[self.rule]
        self.halt = False
        self.rule = previous_rule+1

    def multiply(self, Ri, Rj):
        previous_rule = copy.deepcopy(self.rule)
        self.rule = 1
        rules = CallableDict({1: lambda: self.copy(Rj, 'R5'),
                              2: lambda: self.if_equal('R5', 'R000', jump=10),
                              3: lambda: self.copy(Ri, 'R4'),
                              4: lambda: self.if_equal('R4', 'R000', jump=8),
                              5: lambda: self.decrement('R4'),
                              6: lambda: self.increment('R3'),
                              7: lambda: self.if_equal('R000', 'R000', jump=4),
                              8: lambda: self.decrement('R5'),
                              9: lambda: self.if_equal('R000', 'R000', jump=2),
                              10: lambda: self.set_halt(True)})

        while not self.halt:
            # print("R4: ", self.registers['R4'][-1])
            print("M", self.rule)
            # print(self.registers)
            rules[self.rule]
        self.halt = False
        self.rule = previous_rule+1



if __name__ == '__main__':
    input = {'R000': [0],
             'R00': [0],
             'R0': [0],
             'R1': [0],
             'R2': [0],
             'R3': [0],
             'R4': [0],
             'R5': [0],
             'R6': [3],
             'R7': [2]
             }
    CM = CounterMachine(input=input)
    CM.run()