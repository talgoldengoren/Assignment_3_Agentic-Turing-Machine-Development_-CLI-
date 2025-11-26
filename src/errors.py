"""
Custom Exception Classes for Agentic Turing Machine

This module defines custom exceptions for better error handling and
debugging throughout the application.
"""


class AgenticTuringMachineError(Exception):
    """Base exception class for all Agentic Turing Machine errors."""

    def __init__(self, message: str, details: dict = None):
        """
        Initialize the exception.

        Args:
            message: Human-readable error message
            details: Optional dictionary with additional error details
        """
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

    def __str__(self):
        """Return string representation of the error."""
        if self.details:
            details_str = ", ".join(f"{k}={v}" for k, v in self.details.items())
            return f"{self.message} ({details_str})"
        return self.message


class ConfigurationError(AgenticTuringMachineError):
    """Raised when there's a configuration error."""
    pass


class APIError(AgenticTuringMachineError):
    """Raised when an API call fails."""
    pass


class SkillNotFoundError(AgenticTuringMachineError):
    """Raised when a required skill file is not found."""
    pass


class InvalidNoiseLevel(AgenticTuringMachineError):
    """Raised when an invalid noise level is provided."""
    pass


class TranslationError(AgenticTuringMachineError):
    """Raised when a translation operation fails."""
    pass


class AnalysisError(AgenticTuringMachineError):
    """Raised when analysis operations fail."""
    pass


class ValidationError(AgenticTuringMachineError):
    """Raised when input validation fails."""
    pass


class FileOperationError(AgenticTuringMachineError):
    """Raised when file operations fail."""
    pass


class PluginError(AgenticTuringMachineError):
    """Raised when plugin operations fail."""
    pass
