import numpy as np
import matplotlib.pyplot as plt

class HopfieldModel:

    def __init__(self):
        """
        Initializes the model with empty arrays for start and end weights
        """

        self.weights = []
        self.finals = []

    def display(self):
        """
        Displays the weight matrices as distinct plots using a purple/white
        color scheme
        """
        for count, w in enumerate(self.weights):
            plt.imshow(w,
                       cmap=plt.cm.BuPu_r,
                       interpolation='none')
            plt.title(f'Weight matrix for pattern #{count + 1}:')
            plt.show()
            count += 1

        plt.imshow(self.finals,
                   cmap=plt.cm.BuPu_r,
                   interpolation='none')
        plt.title('Matrix of final weights:')
        plt.show()

    def memorize_patterns(self, patterns, debug = False):
        """
        Constructs a weight matrix for each pattern type.
        """
        for index, pattern in enumerate(patterns):
            self.add_weight_pattern(pattern, index + 1, debug)

        self.finals = self.weights[0]
        for weight in self.weights:
            self.finals = self.finals + weight

        self.finals = self.finals - self.weights[0]

    def add_weight_pattern(self, pattern, pattern_id, debug = False):
        weight = np.zeros((pattern.size, pattern.size))

        pattern = pattern.flatten()

        # W(x, y) = P(x) * P(y)
        for x in range(pattern.size):
            for y in range(pattern.size):
                if debug:
                    print(f'Pattern #{pattern_id} is processing cell {(x, y)}')
                weight[x][y] = pattern[x] * pattern[y]

        self.weights.append(weight)

    def update(self, pattern):
        original = pattern.shape
        pattern = pattern.flatten()
        result = np.zeros(pattern.shape)

        for i in range(len(pattern)):
            interactions = 0
            for j in range(len(pattern)):
                interactions += self.finals[i][j] * pattern[j]

            result[i] = interactions

        result = result.reshape(original)
        return result