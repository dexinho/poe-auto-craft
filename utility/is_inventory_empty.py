from utility.config import REGIONS, FOLDER_PATHS, FILE_NAMES, PIXEL_SIZES
from utility.find_image import find_image


def is_inventory_empty(rows=5, cols=12):
    image_name = FILE_NAMES["empty_inventory_slot"]
    slot_size = PIXEL_SIZES["inventory"]["slot"]
    region_x, region_y, _, _ = REGIONS["inventory"]

    for i in range(rows):
        for j in range(cols):
            region = (
                region_x + j * slot_size,
                region_y + i * slot_size,
                slot_size,
                slot_size,
            )

            image_result = find_image(
                folder=FOLDER_PATHS["images"]["inventory"],
                image_name=image_name,
                region=region,
            )

            if not image_result["is_found"]:
                print("Inventory is not empty")
                return False

    print("Inventory is empty")
    return True
