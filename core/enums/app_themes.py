from enum import Enum

class AppTheme(Enum):
    """
    Application themes available for the user interface.
    :cvar LIGHT: Light theme with bright colors.
    :cvar DARK: Dark theme with muted colors.
    :cvar AUTO: Automatically switch theme based on system settings.
    """
    LIGHT = "LIGHT"
    DARK = "DARK"
    AUTO = "AUTO"