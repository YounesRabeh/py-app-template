from enum import Enum

class LogLevel(Enum):
    """
    Logging levels for application logging configuration.
    :cvar DEBUG: Detailed debug information.
    :cvar INFO: General informational messages.
    :cvar WARNING: Warnings about potential issues.
    :cvar ERROR: Error messages indicating failures.
    :cvar CRITICAL: Critical errors causing application shutdown.
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"