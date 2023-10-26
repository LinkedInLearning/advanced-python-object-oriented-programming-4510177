# %% Color database
color_db = {
    'red': 0xFF0000,
    'green': 0x00FF00,
    'blue': 0x0000FF,
}


class Colors:
    """Dynamically get color from color_db"""
    # FIXME


# %% Test
colors = Colors()

val = colors.green
print(f'green: {val:06X}')  # 00FF00
