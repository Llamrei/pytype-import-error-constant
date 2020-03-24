from package.foo import FOO_BAR
from package.foo import BAR

from .package_mod import Printer

Printer(FOO_BAR).print()
Printer(repr(BAR)).print()

