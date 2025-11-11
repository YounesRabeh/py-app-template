
import os

from PySide6.QtWidgets import QWidget

from core.util.logger import Logger


class Styles:
    """
    Simple helper to load and apply QSS stylesheets to widgets.
    """

    @staticmethod
    def apply(widget: QWidget, path: str):
        """
        Apply a QSS file to a widget.

        :param widget: The QWidget to style
        :param path: Full path to the .qss file
        """
        if not os.path.exists(path):
            Logger.error(f"QSS file not found: {path}")
            return

        try:
            with open(path, "r", encoding="utf-8") as f:
                qss = f.read()
                widget.setStyleSheet(qss)
                Logger.debug(f"Applied stylesheet from {path} to widget {widget.objectName()}")
        except Exception as e:
            Logger.error(f"Failed to apply stylesheet: {e}")