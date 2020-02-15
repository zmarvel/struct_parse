"""Parse the format defined in the :py:module:`struct` standard library module.
Single-file parser for the string format specified by the :py:module:`struct`
standard library module. This enables the use of strings describing the layout
of packed binary data for other things besides just packing and unpacking, like
generating C struct definitions.
"""


from typing import List
import enum


class ByteOrder(enum.Enum):
    NATIVE = 0
    LITTLE = 1
    BIG = 2
    NETWORK = 3


BYTE_ORDER = {
    '@': ByteOrder.NATIVE,
    '=': ByteOrder.NATIVE,
    '<': ByteOrder.LITTLE,
    '>': ByteOrder.BIG,
    '!': ByteOrder.NETWORK,
}


ORDER_STRING = {}
for k, v in BYTE_ORDER.items():
    ORDER_STRING[v] = k
ORDER_STRING[ByteOrder.NATIVE] = '@'


class FieldType(enum.Enum):
    """Type of a field in the struct. Represented by a single character in the
    format string.
    """
    PAD = 0
    CHAR = 1
    SIGNED_CHAR = 2
    UNSIGNED_CHAR = 3
    BOOL = 4
    SHORT = 5
    UNSIGNED_SHORT = 6
    INT = 7
    UNSIGNED_INT = 8
    LONG = 9
    UNSIGNED_LONG = 10
    LONG_LONG = 11
    UNSIGNED_LONG_LONG = 12
    SSIZE_T = 13
    SIZE_T = 14
    HALF_PRECISION_FLOAT = 15
    FLOAT = 16
    DOUBLE = 17
    CHAR_ARRAY = 18
    VOID_POINTER = 19


FIELD_TYPE = {
    'x': FieldType.PAD,
    'c': FieldType.CHAR,
    'b': FieldType.SIGNED_CHAR,
    'B': FieldType.UNSIGNED_CHAR,
    '?': FieldType.BOOL,
    'h': FieldType.SHORT,
    'H': FieldType.UNSIGNED_SHORT,
    'i': FieldType.INT,
    'I': FieldType.UNSIGNED_INT,
    'l': FieldType.LONG,
    'L': FieldType.UNSIGNED_LONG,
    'q': FieldType.LONG_LONG,
    'Q': FieldType.UNSIGNED_LONG_LONG,
    'n': FieldType.SSIZE_T,
    'N': FieldType.SIZE_T,
    'e': FieldType.HALF_PRECISION_FLOAT,
    'f': FieldType.FLOAT,
    'd': FieldType.DOUBLE,
    's': FieldType.CHAR_ARRAY,
    'p': FieldType.CHAR_ARRAY,
    'P': FieldType.VOID_POINTER,
}


FORMAT_STRING = {}
for k, v in FIELD_TYPE.items():
    FORMAT_STRING[v] = k
FORMAT_STRING[FieldType.CHAR_ARRAY] = 's'


class FieldList:
    """Simply a list of fields, along with a byte_order.
    """
    def __init__(self, fields: List[FieldType] = [],
                 byte_order: ByteOrder = ByteOrder.NATIVE):
        self.fields = fields  # type: List[FieldType]
        self.byte_order = byte_order  # type: ByteOrder

    @classmethod
    def from_string(cls, fmt_string: str) -> 'FieldList':
        """Construct a :py:class:`FieldList` from a format string.

        Args:
            fmt_string: Format string conformant to the specification in
                :py:module:`struct`.

        Returns:
            :py:class:`FieldList` object representing the parsed string as a
            flat AST.
        """
        if len(fmt_string) == 0:
            return FieldList()

        start = 0
        byte_order = ByteOrder.NATIVE
        if fmt_string[0] in BYTE_ORDER:
            start = 1
            byte_order = BYTE_ORDER[fmt_string[0]]

        if len(fmt_string) == start:
            return FieldList()

        return FieldList([FIELD_TYPE[c] for c in fmt_string[start:]],
                         byte_order)

    def to_string(self) -> str:
        """Convert the list of fields back into a format string.

        Returns:
            Format string.
        """
        if len(self.fields) == 0:
            return ''

        # TODO distinguish between "native" orderings

        return ORDER_STRING[self.byte_order] + ''.join(map(
            lambda field: FORMAT_STRING[field],
            self.fields
        ))

    def __len__(self):
        return len(self.fields)

    def __getitem__(self, item: int) -> FieldType:
        return self.fields[item]

    def __contains__(self, item: int):
        return item in self.fields


def parse(format_str: str) -> FieldList:
    """Helper to parse a format string into a :py:class:`FieldList`.

    Args:
        format_str: Format string, as specified by :py:module:`struct`.

    Returns:
        :py:class:`FieldList` object representing the parsed format string.
    """
    return FieldList.from_string(format_str)

