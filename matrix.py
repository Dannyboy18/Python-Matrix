class Matrix(object):

    def __init__(self, matrix_string):    
        # matrix_string = "1 2\n3 4\n5 6"
        splitted = matrix_string.split('\n')

        # splitted = ["1 2", "3 4", "5 6"]
        self.rows = []
        self.columns = []
        for item in splitted:
            # item = "1 2"
            row = []
            numbers = item.split(" ")
            # for number in item.split(" "):
            for i in range(len(numbers)):
                # number = "1"
                row.append(int(numbers[i]))
                try:
                    self.columns[i]
                except IndexError:
                    self.columns.append([])
                self.columns[i].append(int(numbers[i]))
            # row = [1, 2]
            self.rows.append(row)
            # rows = [[1, 2], [3,4], [5,6]]



    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
        # column = []

        # for row in self.rows:
        #     column.append(row[index-1])

        # return column

    def __eq__(self, other_matrix):
        return self.rows == other_matrix.rows

    def add(self, other_matrix):
       return self.plus_oder_minus(other_matrix, "plus")  

    def subtract(self, other_matrix):
       return self.plus_oder_minus(other_matrix, "minus")

    def plus_oder_minus(self, other_matrix, operation):
        result_matrix_string = ""
        result_row_strings = []
        if (len(self.rows) != len(other_matrix.rows)):
            raise Exception("Das geht nicht: Unterschiedlich viele Zeilen")

        for i in range(len(self.rows)):
            result_row = []
            self_row = self.row(i+1)
            other_row = other_matrix.row(i+1)

            if (len(self_row) != len(other_row)):
                raise Exception("Das geht nicht: Unterschiedlich lange Zeilen")
                
            for j in range(len(self_row)):
               if (operation == 'plus'): 
                  result_string = str(self_row[j] + other_row[j])
               if (operation == 'minus'):
                  result_string = str(self_row[j] - other_row[j])

               result_row.append(result_string) 
            separator = " "
            result_row_string = separator.join(result_row)
            result_row_strings.append(result_row_string)
        separator = "\n"
        result_matrix_string = separator.join(result_row_strings)
        return Matrix(result_matrix_string) 
       
    def multiplication(self, other_matrix):
        ergebnis_matrix = ""
        for z in self.rows:
            ergebnis_zeile = ""
            for s in other_matrix.columns:
                summe = 0
                for i in range(len(z)):
                    summe = z[i] * s[i] + summe
                ergebnis_zeile = ergebnis_zeile + str(summe) + " "                
            ergebnis_matrix = ergebnis_matrix + ergebnis_zeile.rstrip() + "\n"
        return Matrix(ergebnis_matrix.rstrip("\n"))
                

    #   rows_A = len(self.rows[0])
    #   columns_A = len(self.columns[0])
    #   #rows_B = len(other_matrix.row[0])
    #   columns_B = len(other_matrix.columns[0])

    # #   if columns_A[0] != rows_B[0]:
    # #     print ("Matrizen koennen nicht multiziert werden. Falsche Demension")
        
    #     # return 
    #   C = [[0 for row in range(columns_B)]for col in range(rows_A)]
    #   print(C) 
    
    #   for i in range(rows_A):
    #       for j in range(columns_B):
    #           for k in range(columns_A):
    #               C[i][j] += rows_A[i][k] * columns_B[k][j]
    #   return  (C)    
    
    # ergebnis_matrix = ""
    # fuer jede Zeile z von A:
    #   ergebnis_zeile = ""
    #   fuer jede spalte s von B:
    #     summe = 0
    #     fuer i=0 bis laenge von z:
    #       summe = summe + z[i] * s[i]
    #     ergebnis_zeile = ergebnis_zeile + str(summe) + " " 
    #   ergebnis_matrix = ergebnis_zeile + "\n"
    # print(ergebnis_matrix)