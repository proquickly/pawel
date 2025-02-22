"""
The **dot product** (also known as the scalar product) is a
mathematical operation that takes two vectors of the same
length and outputs a single scalar. It essentially evaluates
how much one vector is aligned with another.
The operation has applications in geometry, physics, and
machine learning.

pip install notebook
pip install numpy
jupyter notebook
"""
input_vector = [1.72, 1.23]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]

# Computing the dot product of input_vector and weights_1
first_indexes_mult = input_vector[0] * weights_1[0]
second_indexes_mult = input_vector[1] * weights_1[1]
dot_product_1 = first_indexes_mult + second_indexes_mult

print(f"The dot product is: {dot_product_1}")

import numpy as np

dot_product_1 = np.dot(input_vector, weights_1)
print(f"The dot product is: {dot_product_1}")

dot_product_2 = np.dot(input_vector, weights_2)
print(f"The dot product is: {dot_product_2}")

