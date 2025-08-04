def scale_coordinates(x, y, display_settings):
    return (
        int(x * display_settings["display_width"] / display_settings["reference_width"]),
        int(
            y * display_settings["display_height"] / display_settings["reference_height"]
        ),
    )


def scale_region(x, y, w, h, display_settings):
    return (
        int(x * display_settings["display_width"] / display_settings["reference_width"]),
        int(
            y * display_settings["display_height"] / display_settings["reference_height"]
        ),
        int(w * display_settings["display_width"] / display_settings["reference_width"]),
        int(
            h * display_settings["display_height"] / display_settings["reference_height"]
        ),
    )
