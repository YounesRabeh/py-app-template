import os
from types import MethodType
from typing import Optional

from core.util.logger import Logger


class Resources:
    """
    Dynamic resource manager.

    Automatically loads all resource directories defined in [resources]
    in the configuration file.

    For each entry (qss, icons, images, fonts, data, temp...), it:
      • Creates an absolute path attribute (e.g. Resources.qss)
      • Ensures the directory exists
      • Indexes all contained files
      • Dynamically adds methods:
          - get_all_<name>() → list of files
          - get_<name>(filename_or_path) → full absolute path

    Example:
        Resources.get_qss("button1.qss")
    """

    _cfg = {}
    _resources = {}

    # --- Helpers ---

    @classmethod
    def _list_files(cls, directory: str) -> list[str]:
        """Recursively list all files in a directory."""
        files = []
        if not os.path.exists(directory):
            return files
        for root, _, filenames in os.walk(directory):
            for f in filenames:
                files.append(os.path.join(root, f))
        return files

    @classmethod
    def _create_get_all_method(cls, name: str):
        """Create get_all_<name>()"""
        def method(self_or_cls):
            return cls._resources.get(name, [])
        method.__name__ = f"get_all_{name}"
        setattr(cls, method.__name__, MethodType(method, cls))

    @classmethod
    def _create_get_method(cls, name: str):
        """Create get_<name>(filename_or_path)"""
        def method(self_or_cls, path: str):
            base_path = getattr(cls, name)
            candidate = os.path.join(base_path, path)
            abs_path = os.path.abspath(candidate)

            if not os.path.exists(abs_path):
                Logger.error(f"Resource not found: {abs_path}")
                raise FileNotFoundError(f"Resource not found: {abs_path}")

            return abs_path
        method.__name__ = f"get_{name}"
        setattr(cls, method.__name__, MethodType(method, cls))

    # --- Initialization ---

    @classmethod
    def initialize(cls, cfg: Optional[dict] = None):
        if cfg is not None:
            # Filter keys starting with 'RESOURCES_'
            cls._cfg = {k.replace("RESOURCES_", "").lower(): v
                        for k, v in cfg.items() if k.startswith("RESOURCES_")}
        elif not hasattr(cls, "_cfg") or not cls._cfg:
            Logger.error("No configuration provided and Resources._cfg is empty!")
            return

        base = cls._cfg.get("base", "resources")

        for key, path in cls._cfg.items():
            if key == "base":
                setattr(cls, key, os.path.abspath(path))
                continue

            abs_path = os.path.abspath(
                path if os.path.isabs(path) else os.path.join(base, os.path.basename(path))
            )

            setattr(cls, key, abs_path)
            os.makedirs(abs_path, exist_ok=True)

            cls._resources[key] = cls._list_files(abs_path)

            cls._create_get_all_method(key)
            cls._create_get_method(key)

            Logger.debug(f"Indexed {len(cls._resources[key])} {key} files from: {abs_path}")

    # --- API ---

    @classmethod
    def get_all(cls) -> dict[str, list[str]]:
        """Return the dict of all indexed resources."""
        return cls._resources
