# Dự án kiểm thử Classic Groove

Kiểm thử website bán đĩa than Classic Groove, gồm ứng dụng PHP, Selenium/Pytest và Jest.

| Thư mục | Nội dung |
| --- | --- |
| [black-box/](black-box/) | `BlackBox_ClassicGroove_LaHieuPhong`, bộ test độc lập có thêm kiểm thử tìm đơn hàng admin |
| [Classic Groove (Report Testing)/](Classic%20Groove%20%28Report%20Testing%29/) | Gói tổng hợp giữ nguyên ba thư mục nguồn ứng dụng, BlackBox và WhiteBox |

Trong gói tổng hợp, `ClassicGroove/` là ứng dụng PHP có SQL và bộ test JavaScript; `BlackBoxTestingClassicGroove/` chứa Selenium/Pytest; `WhiteBoxTestingClassicGroove/` chứa Jest. Các bản BlackBox có khác biệt ở test đăng ký, tìm kiếm và tìm đơn hàng, nên giữ riêng.

[Báo cáo tham khảo năm 2023](../../references/classic-groove/) của nhóm khác được đặt trong phần tham khảo.

[Về nhóm dự án](../README.md)
