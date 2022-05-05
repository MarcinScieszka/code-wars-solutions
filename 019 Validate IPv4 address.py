import unittest


def chceck_if_valid_ipv4_address(ip: str) -> bool:
    """Fuction checks if provided string can be considered as a vaild IPv4 address.
       An IPv4 address should consist of four octets from 0 to 255 separated by three dots.""" 

    ip_octets = ip.split('.')

    # check if address consist of four octets
    if len(ip_octets) != 4:
        return False

    for ip_octet in ip_octets:
        # check if an octet contains leading zeroes
        if (ip_octet != '0'):
            if (len(ip_octet) - len(ip_octet.lstrip('0'))) > 0:
                return False

        # check if an octet can be an integer
        try:
            ip_octet = int(ip_octet)
        except ValueError:
            return False

        # check if an octet is in a valid range
        if (ip_octet > 255 or ip_octet < 0):
            return False

    return True


class TestValidateIPAddress(unittest.TestCase):
    def test_too_long_address_should_return_false(self):
        # given
        ip = '100.100.100.100.100'

        # then
        self.assertFalse(chceck_if_valid_ipv4_address(ip))

    def test_leading_zeroes_in_address_should_return_false(self):
        # given
        ip = '127.00.0.1'

        # then
        self.assertFalse(chceck_if_valid_ipv4_address(ip))

    def test_octet_outside_range_should_return_false(self):
        # given
        ip = '1.1.300.1'

        # then
        self.assertFalse(chceck_if_valid_ipv4_address(ip))
    
    def test_correct_address_should_return_true(self):
        # given
        ip = '192.168.0.1'

        # then
        self.assertTrue(chceck_if_valid_ipv4_address(ip))


if __name__ == '__main__':
    unittest.main()
