"""
ZSPOOF ULTIMATE - Advanced Network Identity Manipulation Framework

A comprehensive tool for network security research, penetration testing,
and educational purposes.

Author: Ziad SAGHIR (Zeus)
License: MIT
Version: 2.1.0
"""

__version__ = "2.1.0"
__author__ = "Ziad SAGHIR (Zeus)"
__email__ = "ziadsghir8@gmail.com"
__license__ = "MIT"

# Import main components for package usage
try:
    from .zspoof_ultimate import ZSpoofUltimate, MACEngine, ARPSpoofer
    __all__ = ['ZSpoofUltimate', 'MACEngine', 'ARPSpoofer', '__version__']
except ImportError:
    # Handle case where dependencies aren't installed
    __all__ = ['__version__']
