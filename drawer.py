import enum
import pygame

COLOR = [(255, 255, 255), (0,0,0), (255, 0, 0), (50,50,50)]


class UI:
    def __init__(self, surface):
        self.surface = surface

    def __rect(self, color, pos):
        pygame.draw.rect(self.surface, color, pygame.Rect(pos[0], pos[1], pos[2], pos[3]))

    def drawMatrix(self, matrix, start_pos, margin, size):
        row = start_pos[1]
        column = start_pos[0]

        for i, r in enumerate(matrix[0]):
            # print(f"matrix[0]: {len(matrix[0])}")
            for j, c in enumerate(matrix):
                # print(f"matrix: {len(matrix)}")
                self.__rect(COLOR[matrix[j][i]], (row, column, size, size))
                column += size + margin
            column = start_pos[0]
            row += size + margin