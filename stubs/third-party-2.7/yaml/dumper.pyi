# Stubs for yaml.dumper (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from yaml.emitter import *
from yaml.serializer import *
from yaml.representer import *
from yaml.resolver import *

class BaseDumper(Emitter, Serializer, BaseRepresenter, BaseResolver):
    def __init__(self, stream, default_style=None, default_flow_style=None, canonical=None, indent=None, width=None, allow_unicode=None, line_break=None, encoding=None, explicit_start=None, explicit_end=None, version=None, tags=None): ...

class SafeDumper(Emitter, Serializer, SafeRepresenter, Resolver):
    def __init__(self, stream, default_style=None, default_flow_style=None, canonical=None, indent=None, width=None, allow_unicode=None, line_break=None, encoding=None, explicit_start=None, explicit_end=None, version=None, tags=None): ...

class Dumper(Emitter, Serializer, Representer, Resolver):
    def __init__(self, stream, default_style=None, default_flow_style=None, canonical=None, indent=None, width=None, allow_unicode=None, line_break=None, encoding=None, explicit_start=None, explicit_end=None, version=None, tags=None): ...
