def arrange_points(img_matrix, center):

    arranged_points = []

    while(True):

        img_matrix[center[0]][center[1]] = 0

        arranged_points.append(center)

        if(img_matrix[center[0] + 1][center[1]] == 1):
            center = [center[0] + 1, center[1]]
        elif(img_matrix[center[0] + 1][center[1] + 1] == 1):
            center = [center[0] + 1, center[1] + 1]
        elif(img_matrix[center[0]][center[1] + 1] == 1):
            center = [center[0], center[1] + 1]
        elif(img_matrix[center[0] - 1][center[1] + 1] == 1):
            center = [center[0] - 1, center[1] + 1]
        elif(img_matrix[center[0] - 1][center[1]] == 1):
            center = [center[0] - 1, center[1]]
        elif(img_matrix[center[0] - 1][center[1] - 1] == 1):
            center = [center[0] - 1, center[1]-1]
        elif(img_matrix[center[0]][center[1] - 1] == 1):
            center = [center[0], center[1] - 1]
        elif(img_matrix[center[0] + 1][center[1] - 1] == 1):
            center = [center[0] + 1, center[1] - 1]
        else:
            break
        
    return arranged_points
    
