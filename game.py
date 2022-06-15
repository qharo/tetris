from blocks import Four, Three
import random


# GAME CLASS : PRACTICALLY THE ENV CLASS
class Game:

    # Introduces a new shape
    def __intro_shape(self):
        shapes = [Three((random.randint(1,6),2)), Four((random.randint(1,6),2))]
        self.main_shape = shapes[random.randint(0,1)]
        self.matrix = self.main_shape.editMatrix(self.matrix)
    
    # Reconstructs the matrix 
    def __old_matrix(self, rows, columns):
        toRet = []
        for y in range(rows):
            row = []
            for x in range(columns):
                if (y, x) not in self.old:
                    row.append(0)
                else:
                    row.append(3)
            toRet.append(row)
        return toRet


    def __init__(self, rows, columns):
        self.score = 0
        self.rows = rows
        self.columns = columns
        self.old = []
        self.matrix = self.__old_matrix(rows=self.rows, columns=self.columns)
        # print(len(self.matrix))
        # print(len(self.matrix[0]))
        self.__intro_shape()


    # Checks the next position to see if it is valid; if it is, we go ahead, else, we introduce a new block
    def __checkPos(self, dir):
        new_pos = self.main_shape.ifMove(dir)        
       # print(new_pos)
        go_ahead = True
        for value in new_pos:
            if value[0] not in range(20) or value in self.old:
                go_ahead = False
                break
            
            if value[1] not in range(10):
                print("sides")
                return self.__checkPos(3)
        
        if go_ahead:
            return dir
        else:
            return -1

    # Checks to see if any rows are full, i.e. need to be cleared
    def __checkClear(self):
        #print(self.rows, self.columns)
        all_rows = [0 for x in range(self.rows)]
        #print(len(all_rows))
        #print(self.old)
        for value in self.old:
            #print(value)
            all_rows[value[0]] += 1
        return [x for x in range(len(all_rows)) if all_rows[x] > self.columns-1]

    # Clears rows
    def __clear(self, toRem):

        self.old = [x for x in self.old if x[0] not in toRem]

        stop = False
        count = 0
        while not stop:
            new_old = []
            for value in self.old:
                if (value[0] + 1, value[1]) not in self.old and value[0] + 1 < self.rows:
                    new_old.append((value[0]+1, value[1]))
                    count += 1
                else:
                    new_old.append(value)
            if count == 0:
                stop = True
            self.old = new_old
            count = 0

    ### UPDATE FUNCTION ###

    def update(self, dir):
        check = self.__checkPos(dir)

        if check > 0:
            self.matrix = self.main_shape.move(self.__old_matrix(self.rows, self.columns), check)
        else:
            self.old += self.main_shape.pos
            # for value in self.main_shape.pos:
            #     self.old.append(value)
            self.__intro_shape()
            self.score += 2

        cc = self.__checkClear()
        if []:
            print("THIS IS TOOOOOOOOOOOOOO CHEEEEEEEEEEEEEEECK")
        if cc:
            self.score += 100*len(cc)
            self.__clear(cc)
       # print(f"score: {self.score}")

    # Returns matrix
    def retBlox(self):
        return self.matrix

    ### __________ ###