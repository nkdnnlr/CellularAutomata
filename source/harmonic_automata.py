import matplotlib.pyplot as plt


class HarmonicAutomata:
    def __init__(self, initial_string):
        """
        Initialize class
        :param initial_string: initial string of the form ['0', '1', ... , '0']
        """
        # self.rule = rule
        self.rules = self.get_rules()
        self.output = [initial_string]
        self.length = len(initial_string)

    def run(self, steps):
        """
        Runs cellular automata with rules as rule110
        :param steps:
        :return:
        """
        for step in range(steps):
            next_line = self.get_next_line(self.output[-1])
            self.output.append(next_line)
        self.plot_output(self.output)

    @staticmethod
    def get_rules():
        """
        Gets rules
        :return:
        """
        ## TODO: Rewrite this
        rules = {'110': {'14': '0',
                         '110': '1',
                         '101': '1',
                         '100': '0',
                         '011': '1',
                         '010': '1',
                         '001': '1',
                         '000': '0'},

                 '30': {'111': '0',
                        '110': '0',
                        '101': '0',
                        '100': '1',
                        '011': '1',
                        '010': '1',
                        '001': '1',
                        '000': '0'},
                 }

        return rules

    def get_next_line(self, previous_line):
        """
        Gets next line
        :param previous_line:
        :return:
        """
        next_line = []
        for i in range(len(previous_line)):
            #TODO: Rewrite this!
            head = '000'
            # if i == 0:
            #     head = '0'+ previous_line[i] + previous_line[i+1]
            # elif i == self.length-1:
            #     head = previous_line[i-1] + previous_line[i] + '0'
            # else:
            #     head = previous_line[i-1] + previous_line[i] + previous_line[i+1]

            next_line.append(self.rules[head])

        return next_line

    def plot_output(self, output, savefig=True):
        """
        Plots output matrix as image.
        :param self:
        :param output: output matrix
        :param savefig: bool
        :return:
        """
        output = [[int(i) for i in line] for line in output]
        plt.imshow(output)

        if savefig:
            plt.savefig("../output/rule{}.png".format(self.rule))
        plt.show()


if __name__ == '__main__':
    # n_zeros_leading = 80
    # n_ones = 1
    # n_zeros_trailing = 3
    #
    # zeros_leading = ['0' for zero in range(n_zeros_leading)]
    # ones = ['1' for zero in range(n_ones)]
    # zeros_trailing = ['0' for zero in range(n_zeros_trailing)]
    #
    # initial_string = zeros_leading + ones + zeros_trailing
    # initial_string = ['0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0']

    # >> > l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
    # >> > [x + 1 if x >= 45 else x + 5 for x in l]
    keyboard_size = 12
    input = '047'
    # initial_string = ['1' for note in range(len(keyboard_size))]
    initial_string = ['1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0']

    # print(initial_string)
    rule110 = HarmonicAutomata(initial_string=initial_string)
    rule110.run(steps=10)