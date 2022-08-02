import numpy as np


class Draw:
    def __init__(self) -> None:
        pass
    
    def bbox(self, image: np.ndarray) -> str:
        image = np.where(image)
        bbox = np.min(image[0]), np.max(image[0]), np.min(image[1]), np.max(image[1])
        
        return f'x: {bbox[0]}, y: {bbox[2]}, h: {bbox[3]}, w: {bbox[1]}'
        

if __name__ == '__main__':
    draw = Draw()
    
    # Test Case #1
    matrix = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ])
    coords = draw.bbox(matrix)
    print('Test Case #1: ', coords)

    print('-'*10)
    
    # Test Case #2
    matrix = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ])    
    coords = draw.bbox(matrix)
    print('Test Case #2: ', coords)
