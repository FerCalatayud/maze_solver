# Internal
from maze_solver.cell import Cell

# Python
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ) -> None:

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        print(f"=============\n Breaking walls \n=============")
        self.break_walls_r(0, 0)

        print(f"=============\n Reseting Visited Cells property \n=============")
        self._reset_cells_visited()

    def _create_cells(self):
        # Create cells base on the number of rows and columns
        print(f"=============\n Creating the cells \n=============")
        self.cells = []
        for col in range(1 , self.num_cols + 1):
            #print(f"Appending to Column: {col}")
            column = []
            for row in range(1, self.num_rows + 1):
                #print(f"Appending to Row: {row}")
                column.append(Cell(self.__win))
            
            self.cells.append(column)

        print(f"=============\n Now we go to Drawing the cells \n=============")

        for column_indx in range(0, len(self.cells)):
            # Each cell that here is within a column is in fact in a row 
            # because each slot in a column represents a row
            for row_indx in range(0, len(column)):
                #print(f"Drawing a cell in column: {column_indx}, and row: {row_indx}")
                self._draw_cell(column_indx, row_indx)
    
    def _draw_cell(self, column_indx, row_indx):
        if self.__win is None:
            return

        current_cell = self.cells[column_indx][row_indx]

        # This calculates the left x coordinate of each cell
        x_top_left = self.x1 + (column_indx * self.cell_size_x)
        # This calculates the top y coordinate of each cell
        y_top_left = self.y1 + (row_indx * self.cell_size_y)

        x_bottom_right = x_top_left + self.cell_size_x
        y_bottom_right = y_top_left + self.cell_size_y

        #print(f"Drawing Cell with Point_a: ({x_top_left},{y_top_left}) and Point_d: ({x_bottom_right},{y_bottom_right})")

        current_cell.draw(x_top_left, 
                          y_top_left, 
                          x_bottom_right, 
                          y_bottom_right)

        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        
        self.__win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        self.cells[0][0].top_wall = False
        self._draw_cell(0, 0)

        self.cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def break_walls_r(self, column_idx, row_idx):
        self.cells[column_idx][row_idx].visited = True

        next_column_right = True
        next_column_left = True
        next_row_up = True
        next_row_down = True

        while True:
            visiting = []

            if column_idx + 1 > (len(self.cells) - 1):
                next_column_right = False
            if column_idx - 1 < 0:
                next_column_left = False
            if row_idx + 1 > (len(self.cells[0]) - 1):
                next_row_up = False
            if row_idx - 1 < 0:
                next_row_down = False
            

            # columns
            if next_column_right and not self.cells[column_idx + 1][row_idx].visited:
                visiting.append((column_idx + 1, row_idx))
            if next_column_left and not self.cells[column_idx - 1][row_idx].visited:
                visiting.append((column_idx - 1, row_idx))

            # rows
            if next_row_up and not self.cells[column_idx][row_idx + 1].visited:
                visiting.append((column_idx, row_idx + 1))
            if next_row_down and not self.cells[column_idx][row_idx - 1].visited:
                visiting.append((column_idx, row_idx - 1))

            # check if there is any adjacent cells to visit
            if len(visiting) == 0:
                self._draw_cell(column_idx, row_idx)
                return
            else:
                # randomly select the next cell to visit
                rand_num = random.randint(0, (len(visiting) - 1))
                #print(f"This is the random visition number: {rand_num}")
                next_cell_coordinates = visiting[rand_num]

            if column_idx < next_cell_coordinates[0]:
                # right
                self.cells[column_idx][row_idx].right_wall = False
                self.cells[next_cell_coordinates[0]][next_cell_coordinates[1]].left_wall = False
            if column_idx > next_cell_coordinates[0]:
                # left
                self.cells[column_idx][row_idx].left_wall = False
                self.cells[next_cell_coordinates[0]][next_cell_coordinates[1]].right_wall = False
            if row_idx < next_cell_coordinates[1]:
                # down
                self.cells[column_idx][row_idx].bottom_wall = False
                self.cells[next_cell_coordinates[0]][next_cell_coordinates[1]].top_wall = False
            if row_idx > next_cell_coordinates[1]:
                # down
                self.cells[column_idx][row_idx].top_wall = False
                self.cells[next_cell_coordinates[0]][next_cell_coordinates[1]].bottom_wall = False
            
            self.break_walls_r(next_cell_coordinates[0], next_cell_coordinates[1])

    def _reset_cells_visited(self):
        for columns in self.cells:
            for cell in columns:
                cell.visited = False

    def solve(self):
        print(f"=============\n Solving the Maze \n=============")
        return self._solve_r(0, 0)

    def _solve_r(self, column_idx, row_idx):

        self._animate()
        self.cells[column_idx][row_idx].visited = True

        # base case
        if column_idx == (len(self.cells) - 1) and row_idx == (len(self.cells[0]) - 1):
            return True
        
        # Checks for out of maze bounds
        next_column_right = True
        next_column_left = True
        next_row_up = True
        next_row_down = True

        if column_idx + 1 > (len(self.cells) - 1):
            next_column_right = False
        if column_idx - 1 < 0:
            next_column_left = False
        if row_idx + 1 > (len(self.cells[0]) - 1):
            next_row_down = False
        if row_idx - 1 < 0:
            next_row_up = False

        
        for direction in ["right", "left", "up", "down"]:
            if direction == "left":
                if next_column_left and not self.cells[column_idx][row_idx].left_wall and not self.cells[column_idx - 1][row_idx].visited:
                    self.cells[column_idx][row_idx].draw_move(self.cells[column_idx - 1][row_idx])
                    result =  self._solve_r(column_idx - 1, row_idx)

                    if result:
                        return True
                    else:
                        self.cells[column_idx][row_idx].draw_move(self.cells[column_idx - 1][row_idx], undo=True)
            elif direction == "right":
                if next_column_right and not self.cells[column_idx][row_idx].right_wall and not self.cells[column_idx + 1][row_idx].visited:
                    self.cells[column_idx][row_idx].draw_move(self.cells[column_idx + 1][row_idx])
                    result =  self._solve_r(column_idx + 1, row_idx)

                    if result:
                        return True
                    else:
                        self.cells[column_idx][row_idx].draw_move(self.cells[column_idx + 1][row_idx], undo=True)
            elif direction == "up":
                if next_row_up and not self.cells[column_idx][row_idx].top_wall and not self.cells[column_idx][row_idx - 1].visited:
                    self.cells[column_idx][row_idx].draw_move(self.cells[column_idx][row_idx - 1])
                    result =  self._solve_r(column_idx, row_idx - 1)

                    if result:
                        return True
                    else:
                        self.cells[column_idx][row_idx].draw_move(self.cells[column_idx][row_idx - 1], undo=True)
            elif direction == "down":
                if next_row_down and not self.cells[column_idx][row_idx].bottom_wall and not self.cells[column_idx][row_idx + 1].visited:
                    self.cells[column_idx][row_idx].draw_move(self.cells[column_idx][row_idx + 1])
                    result =  self._solve_r(column_idx, row_idx + 1)

                    if result:
                        return True
                    else:
                        self.cells[column_idx][row_idx].draw_move(self.cells[column_idx][row_idx + 1], undo=True)
        
        return False
            