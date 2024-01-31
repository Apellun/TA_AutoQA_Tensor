from pylenium.log import logger as log
from typing import List
from pylenium.element import Element

def check_images_have_same_sizes(images: List[Element]) -> bool:
    """
    Проверяет что размеры изображений в списке элементов совпадают.
    """
    log.this(f"Проверка совпадения размеров изображений")
    
    width = None
    height = None
    
    for image in images:
        image_height = image.get_attribute('height')
        image_width = image.get_attribute('width')

        if width is None and height is None:
            width, height = image_width, image_height
        else:
            if width != image_width or height != image_height:
                log.this(f"Размеры изображений не совпадают")
                return False
            
    log.this(f"Размеры изображений совпадают")
    return True