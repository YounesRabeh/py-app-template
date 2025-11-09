from pathlib import Path
from typing import Any, Union
from core.enums.log_level import LogLevel
from core.enums.app_themes import AppTheme


class ConfigValidator:
    """
    Validation utilities for configuration values
    Provides static methods to validate and convert configuration values

    """

    @staticmethod
    def ensure_positive_int(value: Any, default: int, field_name: str = "value") -> int:
        """
        Ensure value is a positive integer.

        Args:
            value: The value to validate and convert
            default: Default value to use if validation fails
            field_name: Name of the field for error messages

        Returns:
            Positive integer value

        Raises:
            ValueError: If value cannot be converted to positive integer
        """
        try:
            int_value = int(value)
            if int_value > 0:
                return int_value
            else:
                raise ValueError(f"{field_name} must be positive")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid {field_name}: {value} - {str(e)}") from e

    @staticmethod
    def ensure_boolean(value: Any, default: bool, field_name: str = "value") -> bool:
        """
        Ensure value is a boolean.

        Args:
            value: The value to validate and convert
            default: Default value to use if validation fails
            field_name: Name of the field for error messages

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be converted to boolean
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            if value.lower() in ('true', 'yes', '1', 'on'):
                return True
            elif value.lower() in ('false', 'no', '0', 'off'):
                return False
        raise ValueError(f"Invalid {field_name}: {value}")

    @staticmethod
    def ensure_string(value: Any, default: str, field_name: str = "value") -> str:
        """
        Ensure value is a string.

        Args:
            value: The value to validate and convert
            default: Default value to use if validation fails
            field_name: Name of the field for error messages

        Returns:
            String value
        """
        if value is None:
            return default
        return str(value)

    @staticmethod
    def parse_log_level(level: str) -> LogLevel:
        """
        Parse log level string to enum.

        Args:
            level: Log level string (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR')

        Returns:
            LogLevel enum value

        Raises:
            ValueError: If level is not a valid LogLevel
        """
        try:
            return LogLevel(level.upper())
        except ValueError:
            raise ValueError(f"Invalid log level: {level}")

    @staticmethod
    def parse_theme_mode(mode: str) -> AppTheme:
        """
        Parse theme mode string to enum.

        Args:
            mode: Theme mode string (e.g., 'DARK', 'LIGHT', 'AUTO')

        Returns:
            AppTheme enum value

        Raises:
            ValueError: If mode is not a valid AppTheme
        """
        try:
            return AppTheme(mode.upper())
        except ValueError:
            raise ValueError(f"Invalid theme mode: {mode}")

    @staticmethod
    def validate_file_path(path: str, must_exist: bool = False) -> str:
        """
        Validate file path.

        Args:
            path: File path to validate
            must_exist: If True, raises error if file doesn't exist

        Returns:
            Validated file path as string

        Raises:
            ValueError: If path is invalid or file doesn't exist when required
        """
        path_obj = Path(path)
        if must_exist and not path_obj.exists():
            raise ValueError(f"File not found: {path}")
        return str(path_obj)

    @staticmethod
    def validate_directory_path(path: str, create_if_missing: bool = False) -> str:
        """
        Validate directory path.

        Args:
            path: Directory path to validate
            create_if_missing: If True, creates directory if it doesn't exist

        Returns:
            Validated directory path as string

        Raises:
            ValueError: If path is invalid or cannot create directory
        """
        path_obj = Path(path)
        if create_if_missing and not path_obj.exists():
            path_obj.mkdir(parents=True, exist_ok=True)
        return str(path_obj)