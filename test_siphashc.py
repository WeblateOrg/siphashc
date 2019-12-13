"""Test for siphashc module."""
import unittest

from siphashc import siphash


class TestSiphashC(unittest.TestCase):
    """Test for siphashc module."""

    def test_hash(self):
        """Test simple hashing."""
        result = siphash("sixteencharstrng", "i need a hash of this")
        self.assertEqual(10796923698683394048, result)

        result = siphash("0123456789ABCDEF", "a")
        self.assertEqual(12398370950267227270, result)

    def test_errors(self):
        """Test error handling."""
        with self.assertRaises(ValueError):
            siphash("not long enough", "a")
        with self.assertRaises(ValueError):
            siphash("toooooooooooooooooooooooo long", "a")
        with self.assertRaises(ValueError):
            siphash("", "a")

    def test_reference_vectors(self):
        """Test reference vectors."""
        vectors = [
            0x726FDB47DD0E0E31,
            0x74F839C593DC67FD,
            0x0D6C8009D9A94F5A,
            0x85676696D7FB7E2D,
            0xCF2794E0277187B7,
            0x18765564CD99A68D,
            0xCBC9466E58FEE3CE,
            0xAB0200F58B01D137,
            0x93F5F5799A932462,
            0x9E0082DF0BA9E4B0,
            0x7A5DBBC594DDB9F3,
            0xF4B32F46226BADA7,
            0x751E8FBC860EE5FB,
            0x14EA5627C0843D90,
            0xF723CA908E7AF2EE,
            0xA129CA6149BE45E5,
            0x3F2ACC7F57C29BDB,
            0x699AE9F52CBE4794,
            0x4BC1B3F0968DD39C,
            0xBB6DC91DA77961BD,
            0xBED65CF21AA2EE98,
            0xD0F2CBB02E3B67C7,
            0x93536795E3A33E88,
            0xA80C038CCD5CCEC8,
            0xB8AD50C6F649AF94,
            0xBCE192DE8A85B8EA,
            0x17D835B85BBB15F3,
            0x2F2E6163076BCFAD,
            0xDE4DAAACA71DC9A5,
            0xA6A2506687956571,
            0xAD87A3535C49EF28,
            0x32D892FAD841C342,
            0x7127512F72F27CCE,
            0xA7F32346F95978E3,
            0x12E0B01ABB051238,
            0x15E034D40FA197AE,
            0x314DFFBE0815A3B4,
            0x027990F029623981,
            0xCADCD4E59EF40C4D,
            0x9ABFD8766A33735C,
            0x0E3EA96B5304A7D0,
            0xAD0C42D6FC585992,
            0x187306C89BC215A9,
            0xD4A60ABCF3792B95,
            0xF935451DE4F21DF2,
            0xA9538F0419755787,
            0xDB9ACDDFF56CA510,
            0xD06C98CD5C0975EB,
            0xE612A3CB9ECBA951,
            0xC766E62CFCADAF96,
            0xEE64435A9752FE72,
            0xA192D576B245165A,
            0x0A8787BF8ECB74B2,
            0x81B3E73D20B49B6F,
            0x7FA8220BA3B2ECEA,
            0x245731C13CA42499,
            0xB78DBFAF3A8D83BD,
            0xEA1AD565322A1A0B,
            0x60E61C23A3795013,
            0x6606D7E446282B93,
            0x6CA4ECB15C5F91E1,
            0x9F626DA15C9625F3,
            0xE51B38608EF25F57,
            0x958A324CEB064572,
        ]
        k = "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
        message = ""
        for i in range(64):
            self.assertEqual(siphash(k, message), vectors[i])
            message += chr(i)
