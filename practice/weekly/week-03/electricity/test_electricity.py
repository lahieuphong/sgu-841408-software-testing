import unittest

def tinh_tien_dien(so_kw):
    # Đơn giá cho các bậc
    gia_bac_1 = 1678
    gia_bac_2 = 1734
    gia_bac_3 = 2014
    gia_bac_4 = 2536
    gia_bac_5 = 2834
    gia_bac_6 = 2927

    # Số kWh cho từng bậc
    bac_1 = 50
    bac_2 = 50
    bac_3 = 100
    bac_4 = 100
    bac_5 = 100

    # Tính tiền điện theo bậc
    if so_kw <= bac_1:
        tien_dien = so_kw * gia_bac_1
    elif so_kw <= bac_1 + bac_2:
        tien_dien = (bac_1 * gia_bac_1) + ((so_kw - bac_1) * gia_bac_2)
    elif so_kw <= bac_1 + bac_2 + bac_3:
        tien_dien = (bac_1 * gia_bac_1) + (bac_2 * gia_bac_2) + ((so_kw - bac_1 - bac_2) * gia_bac_3)
    elif so_kw <= bac_1 + bac_2 + bac_3 + bac_4:
        tien_dien = (bac_1 * gia_bac_1) + (bac_2 * gia_bac_2) + (bac_3 * gia_bac_3) + ((so_kw - bac_1 - bac_2 - bac_3) * gia_bac_4)
    elif so_kw <= bac_1 + bac_2 + bac_3 + bac_4 + bac_5:
        tien_dien = (bac_1 * gia_bac_1) + (bac_2 * gia_bac_2) + (bac_3 * gia_bac_3) + (bac_4 * gia_bac_4) + ((so_kw - bac_1 - bac_2 - bac_3 - bac_4) * gia_bac_5)
    else:
        tien_dien = (bac_1 * gia_bac_1) + (bac_2 * gia_bac_2) + (bac_3 * gia_bac_3) + (bac_4 * gia_bac_4) + (bac_5 * gia_bac_5) + ((so_kw - bac_1 - bac_2 - bac_3 - bac_4 - bac_5) * gia_bac_6)

    return tien_dien

class TestTinhTienDien(unittest.TestCase):
    def test_case_1(self):
        self.assertAlmostEqual(tinh_tien_dien(20), 33560)

    def test_case_2(self):
        self.assertAlmostEqual(tinh_tien_dien(75), 127250)

    def test_case_3(self):
        self.assertAlmostEqual(tinh_tien_dien(124), 218936)

    def test_case_4(self):
        self.assertAlmostEqual(tinh_tien_dien(250), 498800)

    def test_case_5(self):
        self.assertAlmostEqual(tinh_tien_dien(320), 682280)

    def test_case_6(self):
        self.assertAlmostEqual(tinh_tien_dien(475), 1128525)

if __name__ == '__main__':
    unittest.main()
