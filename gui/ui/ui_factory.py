from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QMenuBar, QMenu
)
from PySide6.QtCore import Qt


class UIFactory:
    """
    A reusable factory class for creating common UI elements with consistent styling.

    This factory provides static methods to create various UI components with
    predefined styles and behaviors, promoting consistency across the application.
    """

    @staticmethod
    def create_label(text: str, align: Qt.AlignmentFlag = Qt.AlignCenter,
                     tooltip: str = None, stylesheet: str = None) -> QLabel:
        """
        Creates a styled QLabel with optional alignment, tooltip, and custom styling.

        Args:
            text (str): The text to display on the label
            align (Qt.AlignmentFlag): Text alignment. Defaults to Qt.AlignCenter
            tooltip (str, optional): Tooltip text to show on hover
            stylesheet (str, optional): Custom CSS stylesheet for the label

        Returns:
            QLabel: Configured label widget
        """
        label = QLabel(text)
        label.setAlignment(align)

        if tooltip:
            label.setToolTip(tooltip)

        if stylesheet:
            label.setStyleSheet(stylesheet)

        return label

    @staticmethod
    def create_button(text: str, on_click: callable = None, tooltip: str = None,
                      min_width: int = 120, enabled: bool = True,
                      stylesheet: str = None) -> QPushButton:
        """
        Creates a styled QPushButton with consistent sizing and optional styling.

        Args:
            text (str): Button display text
            on_click (callable, optional): Callback function for click events
            tooltip (str, optional): Tooltip text to show on hover
            min_width (int): Minimum button width in pixels. Defaults to 120
            enabled (bool): Whether the button is initially enabled. Defaults to True
            stylesheet (str, optional): Custom CSS stylesheet for the button

        Returns:
            QPushButton: Configured button widget
        """
        btn = QPushButton(text)

        if on_click:
            btn.clicked.connect(on_click)

        btn.setMinimumWidth(min_width)
        btn.setEnabled(enabled)

        if tooltip:
            btn.setToolTip(tooltip)

        if stylesheet:
            btn.setStyleSheet(stylesheet)

        return btn

    @staticmethod
    def create_menu_bar(menu_structure: dict, parent: QWidget) -> QMenuBar:
        """
        Creates a complete menu bar from a hierarchical structure definition.

        Args:
            menu_structure (dict): Dictionary defining the menu hierarchy.
                Format: { "Menu Name": [action_entries] }
                Action entries can be:
                - (text, callback, shortcut) for regular actions
                - (text, callback) for actions without shortcuts
                - None for separators
            parent (QWidget): Parent widget for the menu bar

        Returns:
            QMenuBar: Fully configured menu bar

        Raises:
            ValueError: If menu structure format is invalid
        """
        if not menu_structure:
            raise ValueError("Menu structure cannot be empty")

        menubar = QMenuBar(parent)

        for menu_name, actions in menu_structure.items():
            if not actions:
                continue

            menu = QMenu(menu_name, parent)

            for action_entry in actions:
                # Handle separators
                if action_entry is None:
                    menu.addSeparator()
                    continue

                # Validate action entry format
                if not isinstance(action_entry, (list, tuple)) or len(action_entry) < 2:
                    raise ValueError(f"Invalid action entry format: {action_entry}")

                try:
                    text, callback, *rest = action_entry
                    shortcut = rest[0] if rest else None

                    if not isinstance(text, str):
                        raise ValueError(f"Action text must be string, got {type(text)}")

                    action = QAction(text, parent)

                    if shortcut:
                        if not isinstance(shortcut, str):
                            raise ValueError(f"Shortcut must be string, got {type(shortcut)}")
                        action.setShortcut(shortcut)

                    if callback:
                        if not callable(callback):
                            raise ValueError(f"Callback must be callable, got {type(callback)}")
                        action.triggered.connect(callback)

                    menu.addAction(action)

                except (ValueError, TypeError) as e:
                    raise ValueError(f"Error processing action entry {action_entry}: {e}")

            menubar.addMenu(menu)

        return menubar

    @staticmethod
    def create_drag_drop_area(width: int, height: int, allowed_extensions: list = None,
                              on_files_selected: callable = None) -> QWidget:
        """
        Creates a widget area that supports drag and drop file operations.

        Args:
            width (int): Width of the drag-drop area
            height (int): Height of the drag-drop area
            allowed_extensions (list, optional): List of allowed file extensions (e.g. ['.txt', '.pdf'])
            on_files_selected (callable, optional): Callback function called with list of file paths

        Returns:
            QWidget: Configured drag and drop area widget

        Note:
            This is a stub implementation. Actual drag-drop functionality needs to be implemented
            by subclassing QWidget and implementing dragEnterEvent and dropEvent.

        Example:
            >>> drop_area = UIFactory.create_drag_drop_area(
            ...     400, 200, ['.jpg', '.png'], self.handle_dropped_files
            ... )
        """
        pass