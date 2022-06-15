

# DIR 2: RIGHT, 3: DOWN, 4: LEFT, 5: ROTATE

from pyparsing import col

class Three: # T SHAPE
    def __getPos(self, start_pos):
        if self.rotated == 1:
            return [
                (start_pos[0]-1, start_pos[1]),
                (start_pos[0], start_pos[1]),
                (start_pos[0]+1, start_pos[1]),
                (start_pos[0], start_pos[1]+1),
            ]
        if self.rotated == 2:
                #new_start_pos = self.start_pos
                return [
                    (start_pos[0], start_pos[1]-1),
                    (start_pos[0], start_pos[1]),
                    (start_pos[0]+1, start_pos[1]),
                    (start_pos[0], start_pos[1]+1),
                ]
        
        if self.rotated == 3:
            return [
                (start_pos[0]-1, start_pos[1]),
                (start_pos[0], start_pos[1]),
                (start_pos[0]+1, start_pos[1]),
                (start_pos[0], start_pos[1]-1),
            ]

        else:
            return [
                (start_pos[0], start_pos[1]-1),
                (start_pos[0], start_pos[1]),
                (start_pos[0]-1, start_pos[1]),
                (start_pos[0], start_pos[1]+1),
            ]
 
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.rotated = 0
        self.pos = self.__getPos(self.start_pos)
    
    def editMatrix(self, matrix):
       # print(self.pos)
        for pos in self.pos:
            matrix[pos[0]][pos[1]] = 2
        return matrix

    def ifMove(self, dir):
        if dir == 2:
            new_start_pos = (self.start_pos[0], self.start_pos[1]+1)
            return self.__getPos(new_start_pos)

        if dir == 3:
            new_start_pos = (self.start_pos[0]+1, self.start_pos[1])
            return self.__getPos(new_start_pos)

        if dir == 4:
            new_start_pos = (self.start_pos[0], self.start_pos[1]-1)
            return self.__getPos(new_start_pos)
        
        if dir == 5:
            if self.rotated == 0:
                new_start_pos = self.start_pos
                return [
                    (new_start_pos[0]-1, new_start_pos[1]),
                    (new_start_pos[0], new_start_pos[1]),
                    (new_start_pos[0]+1, new_start_pos[1]),
                    (new_start_pos[0], new_start_pos[1]+1),
                ]

            if self.rotated == 1:
                new_start_pos = self.start_pos
                return [
                    (new_start_pos[0], new_start_pos[1]-1),
                    (new_start_pos[0], new_start_pos[1]),
                    (new_start_pos[0]+1, new_start_pos[1]),
                    (new_start_pos[0], new_start_pos[1]+1),
                ]

            if self.rotated == 2:
                new_start_pos = self.start_pos
                return [
                    (new_start_pos[0], new_start_pos[1]-1),
                    (new_start_pos[0], new_start_pos[1]),
                    (new_start_pos[0], new_start_pos[1]+1),
                    (new_start_pos[0]-1, new_start_pos[1]),
                ]

            else:
                new_start_pos = self.start_pos
                return [
                    (new_start_pos[0]-1, new_start_pos[1]),
                    (new_start_pos[0], new_start_pos[1]),
                    (new_start_pos[0], new_start_pos[1]-1),
                    (new_start_pos[0]+1, new_start_pos[1]),
                ]


    def move(self, matrix, dir):
        if dir == 2:
            self.start_pos = (self.start_pos[0], self.start_pos[1]+1)
            self.pos = self.__getPos(self.start_pos)
            return self.editMatrix(matrix)

        if dir == 3:
            self.start_pos = (self.start_pos[0] + 1, self.start_pos[1])
            self.pos = self.__getPos(self.start_pos)
            return self.editMatrix(matrix)

        if dir == 4:
            self.start_pos = (self.start_pos[0], self.start_pos[1] - 1)
            self.pos = self.__getPos(self.start_pos)
            return self.editMatrix(matrix)
        

        if dir == 5:
            if self.rotated < 3:
                self.rotated += 1
                self.pos = self.__getPos(self.start_pos)
                return self.editMatrix(matrix)
            
            if self.rotated == 3:
                self.rotated = 0
                self.pos = self.__getPos(self.start_pos)
                return self.editMatrix(matrix)



class Four: # SLEEPING LINE
    
    def __getPos(self, start_pos):
        if self.rotated:
            return [
                (start_pos[0], start_pos[1]),
                (start_pos[0]+1, start_pos[1]),
                (start_pos[0]+2, start_pos[1]),
                (start_pos[0]+3, start_pos[1]),
            ]
        else:
            return [
                (start_pos[0], start_pos[1]),
                (start_pos[0], start_pos[1]+1),
                (start_pos[0], start_pos[1]+2),
                (start_pos[0], start_pos[1]+3),
            ]

 
    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.rotated = False
        self.pos = self.__getPos(self.start_pos)
    
    def editMatrix(self, matrix):
        for pos in self.pos:
            matrix[pos[0]][pos[1]] = 2
        return matrix
    
    # def __getPos(self, start_pos):
    #     if self.rotated:
    #         return [
    #             (start_pos[0], start_pos[1]),
    #             (start_pos[0]+1, start_pos[1]),
    #             (start_pos[0]+2, start_pos[1]),
    #             (start_pos[0]+3, start_pos[1]),
    #         ]
    #     else:
    #         return [
    #             (start_pos[0], start_pos[1]),
    #             (start_pos[0]+1, start_pos[1]),
    #             (start_pos[0]+2, start_pos[1]),
    #             (start_pos[0]+3, start_pos[1]),
    #         ]

    def ifMove(self, dir):
        if dir == 2:
            new_start_pos = (self.start_pos[0], self.start_pos[1]+1)
            return self.__getPos(new_start_pos)

        if dir == 3:
            new_start_pos = (self.start_pos[0]+1, self.start_pos[1])
            return self.__getPos(new_start_pos)

        if dir == 4:
            new_start_pos = (self.start_pos[0], self.start_pos[1]-1)
            return self.__getPos(new_start_pos)
        
        if dir == 5:
            if not self.rotated:
                new_start_pos = (self.start_pos[0]-1, self.start_pos[1] + 2)
                return [
                    (new_start_pos[0], new_start_pos[1]),
                    (new_start_pos[0]+1, new_start_pos[1]),
                    (new_start_pos[0]+2, new_start_pos[1]),
                    (new_start_pos[0]+3, new_start_pos[1]),
                ]
            else:
                new_start_pos = (self.start_pos[0] + 1, self.start_pos[1] - 2)
                return [
                    (new_start_pos[0], new_start_pos[1]),
                    (new_start_pos[0], new_start_pos[1]+1),
                    (new_start_pos[0], new_start_pos[1]+2),
                    (new_start_pos[0], new_start_pos[1]+3),
                ]
                


    def move(self, matrix, dir):
        if dir == 2:
            self.start_pos = (self.start_pos[0], self.start_pos[1]+1)
            self.pos = self.__getPos(self.start_pos)
            return self.editMatrix(matrix)

        if dir == 3:
            self.start_pos = (self.start_pos[0]+1, self.start_pos[1])
            self.pos = self.__getPos(self.start_pos)
            return self.editMatrix(matrix)

        if dir == 4:
            self.start_pos = (self.start_pos[0], self.start_pos[1]-1)
            self.pos = self.__getPos(self.start_pos)
            return self.editMatrix(matrix)
        
        if dir == 5:
            if self.rotated:
                self.start_pos = (self.start_pos[0] + 1, self.start_pos[1] - 2)
                self.rotated = False
                self.pos = self.__getPos(self.start_pos)
                return self.editMatrix(matrix)

            else:
                self.rotated = True
                self.start_pos = (self.start_pos[0] - 1, self.start_pos[1] + 2)
                self.pos = self.__getPos(self.start_pos)
                return self.editMatrix(matrix)
        