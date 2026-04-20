import numpy as np

def create_matrix():
    m = 4
    n = 5
    a = np.full((m, n), 0.5)
    np.fill_diagonal(a, -1)
    return a

a = create_matrix()

if __name__ == "__main__":
    print(a)