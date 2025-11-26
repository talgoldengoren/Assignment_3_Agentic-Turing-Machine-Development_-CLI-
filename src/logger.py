"""
Logging Configuration Module

This module sets up structured logging for the Agentic Turing Machine
application with support for file and console output.
"""

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
from typing import Optional

from config import get_config


def setup_logger(
    name: str = "agentic_turing_machine",
    level: Optional[str] = None,
    log_file: Optional[Path] = None
) -> logging.Logger:
    """
    Set up and configure a logger instance.

    Args:
        name: Logger name (typically module name)
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
               If None, uses config value
        log_file: Path to log file. If None, uses config value

    Returns:
        Configured logger instance

    Example:
        >>> logger = setup_logger(__name__)
        >>> logger.info("Starting pipeline")
        >>> logger.error("An error occurred", exc_info=True)
    """
    config = get_config()

    # Get logging configuration
    if level is None:
        level = config.get("logging.level", "INFO")

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))

    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger

    # Create formatters
    log_format = config.get(
        "logging.format",
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    date_format = config.get("logging.date_format", "%Y-%m-%d %H:%M:%S")
    formatter = logging.Formatter(log_format, datefmt=date_format)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (if enabled)
    if config.get("logging.file_logging.enabled", True):
        if log_file is None:
            log_filename = config.get(
                "logging.file_logging.filename",
                "logs/agentic_turing_machine.log"
            )
            log_file = config.project_root / log_filename

        # Create logs directory if it doesn't exist
        log_file.parent.mkdir(parents=True, exist_ok=True)

        # Rotating file handler
        max_bytes = config.get("logging.file_logging.max_bytes", 10485760)  # 10MB
        backup_count = config.get("logging.file_logging.backup_count", 5)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance (convenience function).

    Args:
        name: Logger name (typically __name__)

    Returns:
        Logger instance

    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("Processing started")
    """
    return setup_logger(name)


class LoggerMixin:
    """
    Mixin class to add logging capabilities to any class.

    Usage:
        class MyClass(LoggerMixin):
            def my_method(self):
                self.logger.info("Method called")
    """

    @property
    def logger(self) -> logging.Logger:
        """Get logger instance for this class."""
        if not hasattr(self, '_logger'):
            self._logger = get_logger(self.__class__.__name__)
        return self._logger
