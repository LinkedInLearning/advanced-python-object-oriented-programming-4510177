# %% Color database
color_db = {
    'red': 0xFF0000,
    'green': 0x00FF00,
    'blue': 0x0000FF,
}


class Colors:
    """Dynamically get color from color_db"""
    def __getattr__(self, attr):
        val = color_db.get(attr)
        if val is None:
            raise AttributeError(attr)
        return val

# %% Test
colors = Colors()

val = colors.green
print(f'green: {val:06X}')  # 00FF00
