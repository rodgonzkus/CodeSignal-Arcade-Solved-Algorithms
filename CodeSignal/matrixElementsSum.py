"""
Example idea:

input_1: matrix = [[0, "1", "1", 2], 
                   [0, 5, 0, 0], 
                   [2, 0, 3, 3]]
input_1: matrix = [[no disp, disp(1), disp(1), disp(2)],
                   [no disp, disp(5), no disp, no disp],
                   [no disp, no disp, no disp, no disp]]
output_1:1+1+2+5

    
input_2: matrix = [[1, 1, 1, 0], 
                   [0, 5, 0, 1], 
                   [2, 1, 3, 10]]
input_2: matrix= [[disp(1), disp(1), disp(1), no disp],
                  [no disp, disp(5), no disp, no disp],
                  [no disp, disp(1), no disp, no disp]]
output_2: 1+1+1+5+1                            
"""
def solution(matrix):
    haunted_room = list()
    sum_matrix = 0
    for row in range(0, len(matrix)):     
        #print(f"{row}: {matrix[row]}")
        for col in range(len(matrix[0])):
            #print(f"matrix_{row}{col}= {matrix[row][col]}")
            if matrix[row][col] == 0:
                haunted_room.append(col)
        for col in range(len(matrix[0])):
            if col not in haunted_room:
                sum_matrix += matrix[row][col]
    return sum_matrix