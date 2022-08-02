import cv2
import numpy as np


class AlphaBlend:
    def __init__(self, image_dir: str) -> None:
        self.image_dir = image_dir
    
    def compute(self, foreground: np.ndarray, background: np.ndarray) -> np.ndarray:
        resultant = cv2.add(foreground, background)
        resultant[np.where((resultant == [0,0,0]).all(axis=2))] = [0, 0, 255]        

        return resultant
        
    def blend(self, input_image: np.ndarray, alpha_mask: np.ndarray) -> str:
        foreground = input_image.astype(float)
        alpha = alpha_mask.astype(float)/255        
        
        foreground = cv2.multiply(alpha, foreground)
        cv2.imwrite(f'{self.image_dir}/foreground.jpg', foreground)
        
        background = foreground.copy()
        background = cv2.multiply(1.0 - alpha, background)
        cv2.imwrite(f'{image_dir}/background.jpg', background)

        resultant = self.compute(foreground, background)
        cv2.imwrite(f'{image_dir}/resultant.jpg', resultant)    
        
        return '** computed results w/ red bg & blended input image and mask.'
    
    def driver(self) -> str:
        input_image = cv2.imread(f'{self.image_dir}/input.jpg')
        alpha_mask = cv2.imread(f'{self.image_dir}/alpha.png')
        input_image = cv2.resize(input_image, (alpha_mask.shape[1], alpha_mask.shape[0]), interpolation=cv2.INTER_AREA)
        status = self.blend(input_image, alpha_mask)
        
        return status 


if __name__ == '__main__':
    image_dir = './images'
    blender = AlphaBlend(image_dir)
    status = blender.driver() 
    print(status)
