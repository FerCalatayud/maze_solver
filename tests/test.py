# Python
import unittest

# Internal
from maze_solver.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
        
    def test_maze_re_draw_start_finish_cells(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(100, 100, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.cells[0][0].top_wall,
            False,
        )
        self.assertEqual(
            m1.cells[num_cols - 1][num_rows - 1].bottom_wall,
            False,
        )


if __name__ == "__main__":
    unittest.main()
