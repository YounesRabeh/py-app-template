import os

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QMenu, QSizePolicy
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtCore import Qt

from core.util.resources import Resources
from core.util.logger import Logger

class FileEntry(QWidget):
    """
    Generic file-entry row with default icon, showing file name, size, and a menu.
    """
    DEFAULT_ICON, ERROR_ICON = None, None

    def __init__(self, file_path: str, on_edit=None, on_delete=None, parent=None, show_error_if_missing=True):
        super().__init__(parent)

        # Lazy-load class-level icons if not already loaded
        if self.__class__.DEFAULT_ICON is None:
            self.__class__.DEFAULT_ICON = Resources.get_in_icons("sys/default_file_entry.png")
        if self.__class__.ERROR_ICON is None:
            self.__class__.ERROR_ICON = Resources.get_in_icons("sys/error.png")

        self.file_path = file_path
        self.show_error_if_missing = show_error_if_missing

        # Determine if the file exists
        self.file_exists = os.path.exists(file_path)
        if self.show_error_if_missing and not self.file_exists:
            self.file_name = "File not found !"
        else:
            self.file_name = os.path.basename(file_path)

        self.on_edit = on_edit
        self.on_delete = on_delete

        self._build_ui()

    def _build_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(12)

        # ========== ICON ==========
        icon_label = QLabel()
        icon_label.setFixedSize(64, 64)

        # Show error icon if file is missing and flag is True
        icon_path = self.ERROR_ICON if self.show_error_if_missing and not self.file_exists else self.DEFAULT_ICON
        pix = QPixmap(icon_path) if os.path.exists(icon_path) else QPixmap(64, 64)
        if pix.isNull():
            pix = QPixmap(64, 64)
            pix.fill(Qt.darkGray)
        else:
            pix = pix.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        icon_label.setPixmap(pix)

        # ========== TEXT ==========
        text_container = QVBoxLayout()
        text_container.setSpacing(2)

        name_label = QLabel(self.file_name)
        name_label.setToolTip(self.file_name)
        name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        # File size
        size_bytes = 0
        if self.file_exists:
            try:
                size_bytes = os.path.getsize(self.file_path)
            except Exception:
                Logger.warning(f"Could not get size for: {self.file_path}")
        size_label = QLabel(self._format_size(size_bytes))
        size_label.setStyleSheet("font-size: 11px; opacity: 0.6;")

        text_container.addWidget(name_label)
        text_container.addWidget(size_label)

        # ========== MENU BUTTON ==========
        menu_button = QPushButton("▼")
        menu_button.setFixedSize(28, 28)
        menu_button.setCursor(Qt.PointingHandCursor)

        menu = QMenu(self)
        action_edit = QAction("✏️ Edit", self)
        action_delete = QAction("⛔ Hide", self)
        menu.addAction(action_edit)
        menu.addAction(action_delete)
        menu_button.clicked.connect(
            lambda: menu.exec_(menu_button.mapToGlobal(menu_button.rect().bottomLeft()))
        )

        if self.on_edit:
            action_edit.triggered.connect(lambda: self.on_edit(self.file_path))
        if self.on_delete:
            action_delete.triggered.connect(lambda: self.on_delete(self.file_path))

        # ========== ASSEMBLE ==========
        layout.addWidget(icon_label)
        layout.addLayout(text_container)
        layout.addStretch()
        layout.addWidget(menu_button)

    def _format_size(self, size_bytes):
        for unit in ["B", "KB", "MB", "GB"]:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"

    def paintEvent(self, event):
        super().paintEvent(event)
