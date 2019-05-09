import matplotlib.pyplot as plt


class HarmonicAutomata:
    def __init__(self, initial_string, rule):
        """
        Initialize class
        :param initial_string: initial string of the form ['0', '1', ... , '0']
        """
        self.rule = rule
        self.rules = self.get_rules(self.rule)
        self.output = [initial_string]
        self.length = len(initial_string)
        self.keyboard_size = 12
        self.repetition = int(self.length/self.keyboard_size)

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
    def get_rules(rule):
        """
        Gets rules
        :return:
        """
        rules = {
            '110': {
                '111': '0',
                '110': '1',
                '101': '1',
                '100': '0',
                '011': '1',
                '010': '1',
                '001': '1',
                '000': '0'},

            '110neg': {
                '111': '1',
                '110': '1',
                '101': '1',
                '100': '0',
                '011': '0',
                '010': '0',
                '001': '0',
                '000': '1'},

            '30': {
                '111': '0',
                '110': '0',
                '101': '0',
                '100': '1',
                '011': '1',
                '010': '1',
                '001': '1',
                '000': '0'},
        }



        return rules[rule]

    def get_next_line(self, previous_line):
        """
        Gets next line
        :param previous_line:
        :return:
        """
        next_line = []
        for i in range(12):
            #TODO: Rewrite this!
            head = previous_line[i] + previous_line[i+4] + previous_line[i+7]

            next_line.append(self.rules[head])
        next_line = next_line*self.repetition

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
            plt.savefig("../output/harmonic/{}.png".format('dur'))
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
    # initial_string = ['1' for get_note in range(len(keyboard_size))]
    initial_string = ['1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0']

    # print(initial_string)
    rule110 = HarmonicAutomata(initial_string=initial_string, rule='30')
    rule110.run(steps=50)
    print(rule110.output)