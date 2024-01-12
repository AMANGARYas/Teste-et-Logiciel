import unittest
from function import find_exit

def test_find_exit(self):
    maze_example = [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 9]
    ]
    start_position = (0, 0)

    exit_position = find_exit(maze_example, start_position)

    # Vérifie que les coordonnées de la sortie sont correctes
    self.assertEqual(exit_position, (0, 0))


if __name__ == '__main__':
    unittest.main()

