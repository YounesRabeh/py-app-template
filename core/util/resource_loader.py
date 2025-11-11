import os
from core.config.configuration import Config
from core.util.logger import Logger


class ResourceLoader:
    """
    Centralized loader for application resources.
    Uses the [resources] section from the configuration.
    """

    def __init__(self):
        cfg = Config.get().get("resources", {})

        # Base resource folder
        self.base = cfg.get("base", "resources")
        self.qss = cfg.get("qss", os.path.join(self.base, "qss"))
        self.icons = cfg.get("icons", os.path.join(self.base, "icons"))
        self.images = cfg.get("images", os.path.join(self.base, "images"))
        self.fonts = cfg.get("fonts", os.path.join(self.base, "fonts"))
        self.data = cfg.get("data", os.path.join(self.base, "data"))
        self.temp = cfg.get("temp", os.path.join(self.base, "temp"))

        # Ensure temp folder exists
        if not os.path.exists(self.temp):
            os.makedirs(self.temp, exist_ok=True)
            Logger.debug(f"Created temp folder: {self.temp}")

    def get_qss(self, filename: str) -> str:
        """Return full path to a QSS file"""
        path = os.path.join(self.qss, filename)
        if not os.path.exists(path):
            Logger.error(f"QSS file not found: {path}")
        return path

    def get_icon(self, filename: str) -> str:
        """Return full path to an icon file"""
        path = os.path.join(self.icons, filename)
        if not os.path.exists(path):
            Logger.error(f"Icon file not found: {path}")
        return path

    def get_image(self, filename: str) -> str:
        """Return full path to an image file"""
        path = os.path.join(self.images, filename)
        if not os.path.exists(path):
            Logger.error(f"Image file not found: {path}")
        return path

    def get_font(self, filename: str) -> str:
        """Return full path to a font file"""
        path = os.path.join(self.fonts, filename)
        if not os.path.exists(path):
            Logger.error(f"Font file not found: {path}")
        return path

    def get_data(self, filename: str) -> str:
        """Return full path to a data file"""
        path = os.path.join(self.data, filename)
        if not os.path.exists(path):
            Logger.error(f"Data file not found: {path}")
        return path

    def get_temp(self, filename: str) -> str:
        """Return full path to a temporary file"""
        return os.path.join(self.temp, filename)
