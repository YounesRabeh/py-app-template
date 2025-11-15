from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, Signal
from typing import Optional, Callable


class UIFactory:
    """Reusable factory for building common UI elements with consistent styling."""

    @staticmethod
    def create_label(text: str = "", align: Qt.Alignment = Qt.AlignCenter) -> QLabel:
        """
        Creates a styled QLabel with specified text and alignment.

        Args:
            text: The label text content
            align: Text alignment (default: Qt.AlignCenter)

        Returns:
            Configured QLabel instance
        """
        label = QLabel(text)
        label.setAlignment(align)
        return label

    @staticmethod
    def create_button(text: str, on_click: Optional[Callable] = None) -> QPushButton:
        """
        Creates a styled QPushButton with consistent sizing.

        Args:
            text: Button text label
            on_click: Optional callback function for click events

        Returns:
            Configured QPushButton instance
        """
        btn = QPushButton(text)
        if on_click:
            btn.clicked.connect(on_click)
        btn.setMinimumWidth(120)
        return btn


class BaseStage(QWidget):
    """
    Base class for all application stages with standardized navigation.

    Provides a consistent layout structure with title, content area, and
    bottom navigation buttons. Emits signals for stage navigation.
    """

    # Signals for stage navigation
    next_stage = Signal()
    prev_stage = Signal()

    def __init__(self, config: dict, title: str):
        """
        Initialize the base stage.

        :param config: Application configuration dictionary
        :param title: Stage title displayed at the top
        """
        super().__init__()
        self.config = config
        self.title = title
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Set up the main UI layout structure."""
        # Main Layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)
        self.main_layout.setAlignment(Qt.AlignTop)

        # Title
        self.main_layout.addWidget(UIFactory.create_label(self.title))

        # Content Area - to be populated by subclasses
        self.content_layout = QVBoxLayout()
        self.main_layout.addLayout(self.content_layout)

        # Spacer to push buttons to bottom
        self.main_layout.addStretch(1)

        # Bottom Navigation Bar
        self.nav_layout = QHBoxLayout()
        self.nav_layout.setContentsMargins(0, 10, 0, 0)
        self.nav_layout.setSpacing(20)
        self.main_layout.addLayout(self.nav_layout)

    def add_nav_buttons(self, back_text: Optional[str] = None, next_text: Optional[str] = None) -> None:
        """
        Adds navigation buttons to the bottom of the stage.

        :param back_text: Text for the back button (None hides the button)
        :param next_text: Text for the next button (None hides the button)
        """
        # Back button (left aligned)
        if back_text:
            back_btn = UIFactory.create_button(back_text, self.prev_stage.emit)
            self.nav_layout.addWidget(back_btn)

        # Spacer pushes Next button to the right
        self.nav_layout.addSpacerItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        )

        # Next button (right aligned)
        if next_text:
            next_btn = UIFactory.create_button(next_text, self.next_stage.emit)
            self.nav_layout.addWidget(next_btn)