import unittest

from struct_parse import FieldList, FieldType, ByteOrder, BYTE_ORDER, FIELD_TYPE


class TestFieldListConstructor(unittest.TestCase):
    def test_empty(self):
        field_list = FieldList()
        self.assertEqual(len(field_list.fields), 0)
        self.assertEqual(field_list.fields, [])

    def test_basic(self):
        field_list = FieldList([FieldType.BOOL])
        self.assertEqual(len(field_list.fields), 1)
        self.assertTrue(FieldType.BOOL in field_list)
        self.assertEqual(field_list.fields, [FieldType.BOOL])


class TestFieldListFromString(unittest.TestCase):
    def test_only_endianness(self):
        for c in BYTE_ORDER.keys():
            field_list = FieldList.from_string(c)
            self.assertEqual(field_list.byte_order, ByteOrder.NATIVE)
            self.assertEqual(len(field_list), 0)
            self.assertEqual(field_list.fields, [])

    def test_single_element(self):
        for c, typ in FIELD_TYPE.items():
            field_list = FieldList.from_string(c)
            self.assertEqual(len(field_list), 1)
            self.assertEqual(field_list.fields, [typ])

    def test_single_element_with_endianness(self):
        for order_c, order in BYTE_ORDER.items():
            for c, typ in FIELD_TYPE.items():
                field_list = FieldList.from_string(order_c + c)
                self.assertEqual(len(field_list), 1)
                self.assertEqual(field_list.byte_order, order)
                self.assertEqual(field_list.fields, [typ])

    def test_multiple_elements(self):
        field_list = FieldList.from_string('xcbB?hHiIlLqQnNefdspP')
        self.assertEqual(field_list.byte_order, ByteOrder.NATIVE)
        self.assertEqual(field_list.fields, [
            FieldType.PAD,
            FieldType.CHAR,
            FieldType.SIGNED_CHAR,
            FieldType.UNSIGNED_CHAR,
            FieldType.BOOL,
            FieldType.SHORT,
            FieldType.UNSIGNED_SHORT,
            FieldType.INT,
            FieldType.UNSIGNED_INT,
            FieldType.LONG,
            FieldType.UNSIGNED_LONG,
            FieldType.LONG_LONG,
            FieldType.UNSIGNED_LONG_LONG,
            FieldType.SSIZE_T,
            FieldType.SIZE_T,
            FieldType.HALF_PRECISION_FLOAT,
            FieldType.FLOAT,
            FieldType.DOUBLE,
            FieldType.CHAR_ARRAY,
            FieldType.CHAR_ARRAY,
            FieldType.VOID_POINTER,
        ])

    def test_multiple_elements_with_endianness(self):
        for order_c, order in BYTE_ORDER.items():
            field_list = FieldList.from_string(
                order_c + 'xcbB?hHiIlLqQnNefdspP')
            self.assertEqual(field_list.byte_order, order)
            self.assertEqual(field_list.fields, [
                FieldType.PAD,
                FieldType.CHAR,
                FieldType.SIGNED_CHAR,
                FieldType.UNSIGNED_CHAR,
                FieldType.BOOL,
                FieldType.SHORT,
                FieldType.UNSIGNED_SHORT,
                FieldType.INT,
                FieldType.UNSIGNED_INT,
                FieldType.LONG,
                FieldType.UNSIGNED_LONG,
                FieldType.LONG_LONG,
                FieldType.UNSIGNED_LONG_LONG,
                FieldType.SSIZE_T,
                FieldType.SIZE_T,
                FieldType.HALF_PRECISION_FLOAT,
                FieldType.FLOAT,
                FieldType.DOUBLE,
                FieldType.CHAR_ARRAY,
                FieldType.CHAR_ARRAY,
                FieldType.VOID_POINTER,
            ])

    def test_two_byte_orders_throws(self):
        with self.assertRaises(KeyError):
            FieldList.from_string('@<')

    def test_invalid_format_char_throws(self):
        with self.assertRaises(KeyError):
            FieldList.from_string('z')


class TestFieldListToString(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(FieldList([]).to_string(), '')

    def test_single_element(self):
        for typ_s, typ in FIELD_TYPE.items():
            if typ_s == 'p':
                continue
            self.assertEqual(FieldList([typ]).to_string(), '@' + typ_s)

    def test_single_element_with_endianness(self):
        for order_s, order in BYTE_ORDER.items():
            if order_s == '=':
                continue
            for typ_s, typ in FIELD_TYPE.items():
                if typ_s == 'p':
                    continue
                self.assertEqual(FieldList([typ], order).to_string(),
                                 order_s + typ_s)

    def test_multiple_elements(self):
        self.assertEqual(FieldList([
            FieldType.PAD,
            FieldType.CHAR,
            FieldType.SIGNED_CHAR,
            FieldType.UNSIGNED_CHAR,
            FieldType.BOOL,
            FieldType.SHORT,
            FieldType.UNSIGNED_SHORT,
            FieldType.INT,
            FieldType.UNSIGNED_INT,
            FieldType.LONG,
            FieldType.UNSIGNED_LONG,
            FieldType.LONG_LONG,
            FieldType.UNSIGNED_LONG_LONG,
            FieldType.SSIZE_T,
            FieldType.SIZE_T,
            FieldType.HALF_PRECISION_FLOAT,
            FieldType.FLOAT,
            FieldType.DOUBLE,
            FieldType.CHAR_ARRAY,
            FieldType.VOID_POINTER,
        ]).to_string(), '@xcbB?hHiIlLqQnNefdsP')

    def test_multiple_elements_with_endianness(self):
        for order_s, order in BYTE_ORDER.items():
            if order_s == '=':
                continue
            self.assertEqual(FieldList([
                FieldType.PAD,
                FieldType.CHAR,
                FieldType.SIGNED_CHAR,
                FieldType.UNSIGNED_CHAR,
                FieldType.BOOL,
                FieldType.SHORT,
                FieldType.UNSIGNED_SHORT,
                FieldType.INT,
                FieldType.UNSIGNED_INT,
                FieldType.LONG,
                FieldType.UNSIGNED_LONG,
                FieldType.LONG_LONG,
                FieldType.UNSIGNED_LONG_LONG,
                FieldType.SSIZE_T,
                FieldType.SIZE_T,
                FieldType.HALF_PRECISION_FLOAT,
                FieldType.FLOAT,
                FieldType.DOUBLE,
                FieldType.CHAR_ARRAY,
                FieldType.VOID_POINTER,
            ], order).to_string(), order_s + 'xcbB?hHiIlLqQnNefdsP')


if __name__ == '__main__':
    unittest.main()
