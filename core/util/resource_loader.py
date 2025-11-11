import os
from core.config.configuration import Config
from core.util.logger import Logger


class ResourceLoader:
    """
    Static centralized loader for application resources.
    Reads paths from the [resources] section of the config.
    """

    # Initialize resource paths once
    _cfg = Config.get().get("resources", {})

    base = _cfg.get("base", "resources")
    qss = _cfg.get("qss", os.path.join(base, "qss"))
    icons = _cfg.get("icons", os.path.join(base, "icons"))
    images = _cfg.get("images", os.path.join(base, "images"))
    fonts = _cfg.get("fonts", os.path.join(base, "fonts"))
    data = _cfg.get("data", os.path.join(base, "data"))
    temp = _cfg.get("temp", os.path.join(base, "temp"))

    # Ensure temp folder exists
    if not os.path.exists(temp):
        os.makedirs(temp, exist_ok=True)
        Logger.debug(f"Created temp folder: {temp}")

    @staticmethod
    def get_qss(filename: str) -> str:
        path = os.path.join(ResourceLoader.qss, filename)
        if not os.path.exists(path):
            Logger.error(f"QSS file not found: {path}")
        return path

    @staticmethod
    def get_icon(filename: str) -> str:
        path = os.path.join(ResourceLoader.icons, filename)
        if not os.path.exists(path):
            Logger.error(f"Icon file not found: {path}")
        return path

    @staticmethod
    def get_image(filename: str) -> str:
        path = os.path.join(ResourceLoader.images, filename)
        if not os.path.exists(path):
            Logger.error(f"Image file not found: {path}")
        return path

    @staticmethod
    def get_font(filename: str) -> str:
        path = os.path.join(ResourceLoader.fonts, filename)
        if not os.path.exists(path):
            Logger.error(f"Font file not found: {path}")
        return path

    @staticmethod
    def get_data(filename: str) -> str:
        path = os.path.join(ResourceLoader.data, filename)
        if not os.path.exists(path):
            Logger.error(f"Data file not found: {path}")
        return path

    @staticmethod
    def get_temp(filename: str) -> str:
        return os.path.join(ResourceLoader.temp, filename)
