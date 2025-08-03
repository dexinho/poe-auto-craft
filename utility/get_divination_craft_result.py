from PIL import Image, ImageChops
import pyautogui
import os

from utility.config import REGIONS

print(REGIONS)


def preload_reference_images(folder, stack_size):
    images = []
    for i in range(stack_size):
        filename = f"divination_card_stack_{i + 1}.png"
        path = os.path.join(folder, filename)
        image = Image.open(path).convert("RGB")
        images.append((filename, image))
    return images


def images_are_equal(img1, img2):
    diff = ImageChops.difference(img1, img2)
    return not diff.getbbox()


def get_divination_craft_result(folder, stack_size):
    target_image = pyautogui.screenshot(
        region=REGIONS["horticrafting_divination_stack"]
    ).convert("RGB")
    card_number = 1

    reference_images = preload_reference_images(folder, stack_size)

    for filename, saved_image in reference_images:
        if images_are_equal(target_image, saved_image):
            return card_number
        card_number += 1

    return 0
