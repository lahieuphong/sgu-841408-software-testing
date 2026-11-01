-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: localhost
-- Thời gian đã tạo: Th12 25, 2024 lúc 05:10 AM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `classic-groove`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `album`
--

CREATE TABLE `album` (
  `maAlbum` int(11) NOT NULL,
  `tenAlbum` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `gia` int(11) DEFAULT NULL,
  `moTa` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `hinh` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `tacGia` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `TrangThai` int(11) DEFAULT NULL,
  `soLuong` int(11) DEFAULT NULL,
  `theLoai` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `album`
--

INSERT INTO `album` (`maAlbum`, `tenAlbum`, `gia`, `moTa`, `hinh`, `tacGia`, `TrangThai`, `soLuong`, `theLoai`) VALUES
(1, 'Evo Sessions', 100, 'Evosound proudly presents Chlara\'s evo sessions with 11 tracks on the LP of her favorite classic songs, mainly with acoustic accompaniment. These famous classic songs can resonate throughout different generations from early 20\'s to 21st century like \"Love Me Tender\" or \"Stay With Me\". Chlara is a British-born singer / songwriter recognised as an acoustic songbird, learned to sing and play guitar when she was a young teenager. \"evo sessions\" is her third album release in 4 years. Chlara is not only young and pretty, she possess a lovely sweet voice, and when you hear her sing with a high dynamic range, you can totally feel the passion and energy she puts into her songs. Included in this album is a song she wrote herself called \"Bliss\". The audio of evo sessions was recorded during a live video shoot. The idea of evo sessions started since 2017 summer, the live music video was shot in studio and because of the fabulous sound quality, evosound decided to release as a full album.', 'EvoSessions-Chlara.jpg', 'Chlara', 1, 0, 2),
(2, '#acousticNOW', 200, ' AcousticNow# is the eagerly awaitied fourth album by the 26-year-old Filipino singing sensation Chlara, who will captivate her listeners with a series of acoustic cover versions that include her singles \'The Nights,\' \'Say You Won\'t Let Go,\' and \'ILYSB,\' which have all received over 20 million plays on Spotify. Chlara takes a varied selection of songs - from hits by Ed Sheeran and Aviici to Justin Bieber and Tears For Fears - and reimagines them in her own unique way. Noted for her alluring honey-toned voice and deft acoustic guitar accompaniment, Chlara, who has been described as an \"acoustic songbird\" is flying high at the moment. With three albums and several EPs already under her belt for the Evosound label, she\'s about to unleash her fourth, acousticNow#. The England-born, Philippines-raised singer/song-writer\'s popularity can be measured by that fact that three songs of her songs have generated over 20 million plays each on Spotify.', 'AcousticNow-Chlara.jpg', 'Chlara', 1, 318, 2),
(3, 'It Serves You Right To Suffer', 200, '180-gram 45 RPM double LP Mastered at AcousTech Mastering Plated and pressed at Quality Record PressingsIt\'s back in stock! Newly repressed at 45 RPM by Quality Record Pressings. This recording was originally mastered at the former AcousTech Mastering facility and the sound is fantastic.John Lee Hooker himself did not know his exact date of birth. If he hadn\'t died at around the age of 80, this ageless musician would still be easily pulling the next generation to his gigs. Hooker remains a phenomenon, a mysterious figure of black rhythm and blues, a charismatic king who reigns supreme in rock \'n\' roll\'s Hall of Fame. John W. Peters described his music as a synthesis of scorching emotional ardour, unrelenting rhythmic intensity, and original poetry of a highly personal character. Anyone hearing him for the first time may well be startled at the unfiltered passion and power of his music.', 'ItServeYouRightToSuffer-JohnLeeHooker.jpg', 'John Lee Hooker', 1, 21, 1),
(4, 'Love For Sale', 100, 'Celebrating 10 years since they first recorded together, Tony Bennett & Lady Gaga return for another collaboration featuring the best of the Cole Porter Songbook. It captures the creative and personal relationship of these two world-famous artists. Tony, who turned 95 in 2021, has spent over 7 decades dedicated to performing the Great American Songbook. They are accompanied by the Brian Newman Quintet with arrangements by Marion Evans and Jorge Callandrelli. 180-gram vinyl.', 'LoveForSale-TonyBennett_LadyGaga.jpg', 'Tony Bennett & Lady Gaga', 1, 2, 6),
(5, 'Dawn FM', 120, 'he Weeknd deemed his 2022 album, Dawn FM, a \"sonic experience\" showcasing a unique cast of features from Tyler, the Creator, Lil Wayne, Quincy Jones, Oneohtrix Point Never, and Jim Carrey. (XO Records/Republic)', 'DawnFM-TheWeeknd.jpg', 'TheWeeknd', 1, 3, 5),
(6, 'Fearless (Taylor’s Version) Gold', 250, '\"Fearless was an album full of magic and curiosity, the bliss and devastation of youth. It was the diary of the adventures and explorations of a teenage girl who was learning tiny lessons with every new crack in the facade of the fairytale ending she\'d been shown in the movies. I\'m thrilled to tell you that my new version of Fearless is done and will be with you soon. It\'s called Fearless (Taylor\'s Version) and it includes 26 songs.\" - Taylor Swift. Includes 6 unreleased tracks. Gold 3 LP.', 'Fearless-TaylorSwift.jpg', 'Taylor Swift', 1, 2, 4),
(7, 'Beleive', 100, 'Internationally renowned Italian tenor Andrea Bocelli releases breathtaking new album, Believe, celebrating the power of music to soothe the soul. It follows his record-breaking `Music for Hope\' performance at Easter from Milan\'s historic Duomo cathedral. Features classic favorites, a previously unreleased track from late Italian composer Ennio Morricone, Gratia Plena (from acclaimed film Fatima), duets w/ Alison Krauss & Cecilia Bartoli and interpretations of Ave Maria and Cohen\'s Hallelujah.', 'Believe-AndreaBocelli.jpg', 'Andrea Bocelli', 1, 7, 3),
(8, 'Jordi', 100, 'The eagerly awaited new album from Maroon 5, JORDI, is the band\'s first since the critically acclaimed Red Pill Blues. The album will include the recently released hit single \"Beautiful Mistakes ft. Megan Thee Stallion\" as well as fan favorites \"Memories\" and \"Nobody\'s Love.\" Vinyl LP pressing. 2021 album.', 'Jordi-Maroon5.jpg', 'Maroon 5', 1, 4, 7),
(12, 'J97', 200, 'Thiên lý ơi là MV của Jack ra mắt cách đây tròn 3 tháng, ngày 22/2/2024, trên kênh YouTube J97 của nam ca nhạc sĩ với số lượng người đăng ký lên tới 6,06 triệu người. Cho tới cuối tuần qua (18/5/2024) MV Thiên lý ơi đạt gần 17,7 triệu lượt xem, 253 nghìn lượt thích và lên tới hơn 120 nghìn bình luận. Thông qua Thiên lý ơi có thể nhìn thấy một góc đời sống âm nhạc của giới trẻ hiện nay.', 'ThienLyOi-J97.jpg', 'J97', 1, 2199, 7),
(13, 'Mochiii', 300, 'Cung cấp bởi: ACV Entertainment', 'CanhHoaHeoTanRemix-Mochiii.jpg', 'Mochiii', 1, 0, 7);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `baihat`
--

CREATE TABLE `baihat` (
  `maBaiHat` int(11) NOT NULL,
  `tenBaiHat` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `linkFile` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `baihat`
--

INSERT INTO `baihat` (`maBaiHat`, `tenBaiHat`, `linkFile`) VALUES
(1, 'This Love', 'EvoSessions-ThisLove'),
(2, 'Ocean Deep', 'EvoSessions-OceanDeep'),
(3, 'Say You Won\'t Let Go', 'AcousticNow-SayYouWontLetGo'),
(4, 'Love Yourself', 'AcousticNow-LoveYourself'),
(5, 'Country Boy', 'ItServeYouRightToSuffer-CountryBoy'),
(6, 'You\'re Wrong', 'ItServeYouRightToSuffer-YoureWrong'),
(7, 'It\'s De-Lovely', 'LoveForSale-It\'sDe-Lovely'),
(8, 'Do I Love You', 'LoveForSale-DoILoveYou'),
(9, 'Dawn FM', 'DawnFm-DawnFm'),
(10, 'Take My Breath', 'DawnFm-TakeMyBreath'),
(11, 'Fearless', 'Fearless-Fearless'),
(12, 'Love Story', 'Fearless-LoveStory'),
(13, 'Believe', 'Believe-Hallelujah\r\n'),
(14, 'Ave Maria', 'Believe-AveMaria'),
(15, 'Beautiful Mistakes', 'Jordi-BeautifulMistakes\r\n'),
(16, 'Lost', 'Jordi-Lost'),
(17, 'Stay With Me', 'Chlara  Stay With Me evo sessions Live'),
(18, 'True Colours', 'Chlara  True Colours evo sessions Live'),
(25, 'J97', 'J97'),
(26, 'Cánh Hoa Héo Tàn (Remix)', 'CanhHoaHeoTanRemix-Mochiii-15867138');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `baihat_album`
--

CREATE TABLE `baihat_album` (
  `BaiHat_maBaiHat` int(11) NOT NULL,
  `Album_maAlbum` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `baihat_album`
--

INSERT INTO `baihat_album` (`BaiHat_maBaiHat`, `Album_maAlbum`) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 3),
(6, 3),
(7, 4),
(8, 4),
(9, 5),
(10, 5),
(11, 6),
(12, 6),
(13, 7),
(14, 7),
(15, 8),
(16, 8),
(17, 1),
(18, 1),
(25, 12),
(26, 13);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitiethoadon`
--

CREATE TABLE `chitiethoadon` (
  `album` int(11) NOT NULL,
  `hoaDon` int(11) NOT NULL,
  `soLuong` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chitiethoadon`
--

INSERT INTO `chitiethoadon` (`album`, `hoaDon`, `soLuong`) VALUES
(1, 21, '17'),
(1, 22, '98'),
(1, 23, '12'),
(1, 24, '68'),
(3, 2, '1'),
(4, 3, '99'),
(5, 21, '39'),
(5, 22, '40'),
(5, 23, '22'),
(5, 24, '91'),
(7, 26, '-1'),
(7, 27, '-1'),
(7, 28, '-1'),
(7, 29, '-1'),
(7, 30, '-1'),
(7, 31, '-1'),
(7, 32, '99'),
(7, 33, '84'),
(12, 1, '10'),
(12, 4, '28'),
(12, 5, '1'),
(12, 6, '51'),
(12, 7, '89'),
(12, 8, '27'),
(12, 9, '88'),
(12, 10, '94'),
(12, 11, '1'),
(12, 12, '8'),
(12, 13, '19'),
(12, 14, '39'),
(12, 15, '66'),
(12, 16, '3'),
(12, 17, '17'),
(12, 18, '1'),
(12, 19, '12'),
(12, 20, '63'),
(12, 25, '43');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietphieunhap`
--

CREATE TABLE `chitietphieunhap` (
  `album` int(11) NOT NULL,
  `phieuNhap` int(11) NOT NULL,
  `gia` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `SoLuong` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chitietphieunhap`
--

INSERT INTO `chitietphieunhap` (`album`, `phieuNhap`, `gia`, `SoLuong`) VALUES
(2, 2, '100', '100'),
(2, 3, '100', '100'),
(2, 4, '100', '100'),
(12, 1, '200', '2000');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chucnang`
--

CREATE TABLE `chucnang` (
  `maChucNang` int(11) NOT NULL,
  `tenChucNang` varchar(100) NOT NULL,
  `icon` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chucnang`
--

INSERT INTO `chucnang` (`maChucNang`, `tenChucNang`, `icon`) VALUES
(1, 'Statistic', 'fa-solid fa-chart-column'),
(2, 'Album', 'fa-solid fa-album'),
(3, 'Order', 'fa-regular fa-list'),
(4, 'Account', 'fa-regular fa-user'),
(5, 'Supply', 'fa-regular fa-box-open'),
(6, 'Structure', 'fa-solid fa-puzzle'),
(7, 'Permission', 'fa-regular fa-user-pen');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `giohang`
--

CREATE TABLE `giohang` (
  `maKhachHang` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `maAlbum` int(11) NOT NULL,
  `soLuong` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `giohang`
--

INSERT INTO `giohang` (`maKhachHang`, `maAlbum`, `soLuong`) VALUES
('lahieuphong_customer', 1, 3);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hoadon`
--

CREATE TABLE `hoadon` (
  `maHoaDon` int(11) NOT NULL,
  `tongTien` int(11) DEFAULT NULL,
  `thoiGianDat` date DEFAULT NULL,
  `trangThai` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `khachHang` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `khuyenMai` int(11) DEFAULT NULL,
  `diaChiGiaoHang` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `hoadon`
--

INSERT INTO `hoadon` (`maHoaDon`, `tongTien`, `thoiGianDat`, `trangThai`, `khachHang`, `khuyenMai`, `diaChiGiaoHang`) VALUES
(1, 2015, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(2, 215, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(3, 9915, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(4, 5615, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(5, 215, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(6, 10215, '2024-12-12', 'Pending', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(7, 17815, '2024-12-12', 'Pending', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(8, 5415, '2024-12-12', 'Pending', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(9, 17615, '2024-12-12', 'Pending', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(10, 18815, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(11, 215, '2024-12-12', 'Shipping', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(12, 1615, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(13, 3815, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(14, 7815, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(15, 13215, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(16, 615, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(17, 3415, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(18, 215, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(19, 2415, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(20, 12615, '2024-12-12', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(21, 6410, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(22, 14630, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(23, 3870, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(24, 17750, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(25, 8615, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(26, -85, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(27, -85, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(28, -85, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(29, -85, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(30, -85, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(31, -85, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(32, 9915, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM'),
(33, 8415, '2024-12-14', 'Cancel', 'lahieuphong_customer', NULL, '430/28/5 TA28 Q12 TPHCM');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `khuyenmai`
--

CREATE TABLE `khuyenmai` (
  `maKhuyenMai` int(11) NOT NULL,
  `dieuKien` int(11) DEFAULT NULL,
  `batDau` date DEFAULT NULL,
  `ketThuc` date DEFAULT NULL,
  `phanTram` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `loainguoidung`
--

CREATE TABLE `loainguoidung` (
  `maloai` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tenLoai` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `trangThai` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `loainguoidung`
--

INSERT INTO `loainguoidung` (`maloai`, `tenLoai`, `trangThai`) VALUES
('KH', 'Khách hàng', 'Hoạt động'),
('NV', 'Nhân viên', 'Hoạt động');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nguoidung`
--

CREATE TABLE `nguoidung` (
  `maNguoiDung` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hoTen` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `SDT` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `diaChi` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `TrangThai` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `loainguoidung` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nguoidung`
--

INSERT INTO `nguoidung` (`maNguoiDung`, `hoTen`, `SDT`, `diaChi`, `email`, `TrangThai`, `loainguoidung`) VALUES
('lahieuphong', 'La Hiểu Phong', '0326526898', 'abc', 'hieuphong144@gmail.com', 'Hoạt động', 'KH'),
('lahieuphong_analyst', 'La Hiểu Phong (analyst)', '0326526898', NULL, NULL, 'Hoạt động', 'KH'),
('lahieuphong_customer', 'La Hiểu Phong (customer)', '0987654321', '456/10 ABC Street, District 5, HCM', 'hieuphong144@gmail.com', 'Hoạt động', 'KH'),
('lahieuphong_default', 'La Hiểu Phong (default)', '0326526898', '430/28/5 TA28 Q12 TPHCM', 'hieuphong144@gmail.com', 'Hoạt động', 'NV'),
('lahieuphong_design', 'La Hiểu Phong (design)', '0326526898', NULL, NULL, 'Hoạt động', 'KH'),
('lahieuphong_seller', 'La Hiểu Phong (seller)', '0326526898', NULL, NULL, 'Hoạt động', 'KH'),
('lahieuphong_stocker', 'La Hiểu Phong (stocker)', '0326526898', NULL, NULL, 'Hoạt động', 'KH'),
('lahieuphong_superAdmin', 'La Hiểu Phong (superAdmin)', '0326526898', '430/28/5 TA28 Q12 TPHCM', 'hieuphong144@gmail.com', 'Hoạt động', 'NV'),
('lahieuphong_test', 'La Hiểu Phong (test)', '0326526898', NULL, NULL, 'Hoạt động', 'KH'),
('lhp', 'LHP', '0326526898', 'abc', 'hieuphong144@gmail.com', 'Hoạt động', 'KH'),
('lhp1', 'LHP', '0326526898', 'abc', 'hieuphong144@gmail.com', 'Hoạt động', 'KH'),
('lhp2', 'LHP', '0326526898', 'abc', 'hieuphong144@gmail.com', 'Hoạt động', 'KH');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nhacungcap`
--

CREATE TABLE `nhacungcap` (
  `maNCC` int(11) NOT NULL,
  `tenNCC` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `diaChi` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `SDT` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `TrangThai` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `nhacungcap`
--

INSERT INTO `nhacungcap` (`maNCC`, `tenNCC`, `diaChi`, `SDT`, `email`, `TrangThai`) VALUES
(1, 'Công ty TNHH ABC', '123 Đường A, Quận B, TP C', '0987654321', 'abc@abc.com', 1),
(2, 'Công ty TNHH XYZ', '456 Đường D, Quận E, TP F', '0123456789', 'xyz@xyz.com', 1),
(3, 'Công ty TNHH LM', '789 Đường G, Quận H, TP I', '0987123456', 'lmh@lmn.com', 1),
(4, ' Công ty TNHH PQR', '321 Đường J, Quận K, TP L', '0123789456', 'pqr@pqr.com', 1),
(5, 'Công ty TNHH UVW', '654 Đường M, Quận N, TP O', '0912345678', 'uvw@uvw.com', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phieunhap`
--

CREATE TABLE `phieunhap` (
  `maPhieuNhap` int(11) NOT NULL,
  `ngayNhap` date DEFAULT NULL,
  `nguoiNhap` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `TongGia` int(11) DEFAULT NULL,
  `NCC` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `phieunhap`
--

INSERT INTO `phieunhap` (`maPhieuNhap`, `ngayNhap`, `nguoiNhap`, `TongGia`, `NCC`) VALUES
(1, '2024-12-12', 'lahieuphong_superAdmin', 400000, 1),
(2, '2024-12-23', 'lahieuphong_superAdmin', 10000, 1),
(3, '2024-12-23', 'lahieuphong_superAdmin', 10000, 1),
(4, '2024-12-24', 'lahieuphong_superAdmin', 10000, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `quyen`
--

CREATE TABLE `quyen` (
  `maCTQ` int(11) NOT NULL,
  `NoiDungQuyen` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `chucNang` int(11) DEFAULT NULL,
  `laTieuDe` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `quyen`
--

INSERT INTO `quyen` (`maCTQ`, `NoiDungQuyen`, `chucNang`, `laTieuDe`) VALUES
(1, 'Access', 2, 1),
(2, 'Edit', 2, 0),
(3, 'Delete', 2, 0),
(4, 'Access', 5, 1),
(5, 'Add', 5, 0),
(6, 'Access', 4, 1),
(7, 'Add', 4, 0),
(8, 'Edit', 4, 0),
(10, 'Access', 3, 1),
(11, 'Edit', 3, 0),
(12, 'Access', 6, 1),
(13, 'Edit', 6, 0),
(14, 'Access', 7, 1),
(15, 'Add', 7, 0),
(16, 'Edit', 7, 0),
(17, 'Delete', 7, 0),
(18, 'Access', 1, 1),
(19, 'Add', 2, 0),
(20, 'Add', 6, 0),
(21, 'Delete\r\n', 6, 0);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `slideshow`
--

CREATE TABLE `slideshow` (
  `maHinh` int(11) NOT NULL,
  `tenHinh` varchar(100) NOT NULL,
  `linkTo` int(11) NOT NULL,
  `linkHinh` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `slideshow`
--

INSERT INTO `slideshow` (`maHinh`, `tenHinh`, `linkTo`, `linkHinh`) VALUES
(2, 'slide1', 5, 'Fearless-TaylorSwift.jpg'),
(4, 'slide2', 5, 'AcousticNow-Chlara.jpg'),
(5, 'slide3', 1, 'LoveForSale-TonyBennett_LadyGaga.jpg'),
(6, 'slide4', 4, 'EvoSessions-Chlara.jpg'),
(8, 'slide5', 8, 'Believe-AndreaBocelli.jpg'),
(10, 'slide7', 1, 'Empty.ico'),
(13, 'slide8', 4, 'lytt.png'),
(15, 'slide9', 2, 'ItServeYouRightToSuffer-JohnLeeHooker.jpg');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `taikhoan`
--

CREATE TABLE `taikhoan` (
  `username` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ngayTao` date DEFAULT NULL,
  `TrangThai` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `matKhau` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `vaiTro` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `taikhoan`
--

INSERT INTO `taikhoan` (`username`, `ngayTao`, `TrangThai`, `matKhau`, `vaiTro`) VALUES
('lahieuphong', '2024-12-15', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 1),
('lahieuphong_analyst', '2024-12-12', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 6),
('lahieuphong_customer', '2024-12-12', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 1),
('lahieuphong_default', '2024-12-12', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 2),
('lahieuphong_design', '2024-12-12', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 5),
('lahieuphong_seller', '2024-12-12', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 4),
('lahieuphong_stocker', '2024-12-12', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 7),
('lahieuphong_superAdmin', '2024-12-12', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 3),
('lahieuphong_test', '2024-12-12', 'Hoạt động', '9ad7d74a55dc6a3ff849ca1e265883a1', 8);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `theloai`
--

CREATE TABLE `theloai` (
  `maLoai` int(11) NOT NULL,
  `tenLoai` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `theloai`
--

INSERT INTO `theloai` (`maLoai`, `tenLoai`) VALUES
(1, 'Blues'),
(2, 'Acoustic'),
(3, 'Classical'),
(4, 'Country'),
(5, 'Electronic'),
(6, 'Jazz'),
(7, 'Pop/Rock');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `vaitro`
--

CREATE TABLE `vaitro` (
  `maVaiTro` int(11) NOT NULL,
  `tenVaiTro` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `moTa` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `vaitro`
--

INSERT INTO `vaitro` (`maVaiTro`, `tenVaiTro`, `moTa`) VALUES
(1, 'customer', 'Tài khoản khách hàng dùng ở trang user'),
(2, 'default', 'Quyền nhân viên mặc định'),
(3, 'superAdmin', 'Toàn quyền hệ thống'),
(4, 'seller', 'dành cho nhân viên chuyên bán hàng online'),
(5, 'design', 'Thay đổi giao diện'),
(6, 'analyst', 'phần tích thông kê'),
(7, 'stocker', 'nhập hàng'),
(8, 'test', 'test');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `vaitro_quyen`
--

CREATE TABLE `vaitro_quyen` (
  `VaiTro_maVaiTro` int(11) NOT NULL,
  `Quyen_maCTQ` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `vaitro_quyen`
--

INSERT INTO `vaitro_quyen` (`VaiTro_maVaiTro`, `Quyen_maCTQ`) VALUES
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(3, 5),
(3, 6),
(3, 7),
(3, 8),
(3, 10),
(3, 11),
(3, 12),
(3, 13),
(3, 14),
(3, 15),
(3, 16),
(3, 17),
(3, 18),
(3, 19),
(3, 20),
(3, 21),
(4, 1),
(4, 10),
(4, 11),
(5, 12),
(5, 13),
(5, 20),
(5, 21),
(6, 4),
(6, 10),
(6, 18),
(7, 1),
(7, 4),
(7, 5),
(8, 1),
(8, 4),
(8, 5),
(8, 18);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `yeuthich`
--

CREATE TABLE `yeuthich` (
  `album` int(11) NOT NULL,
  `nguoiDung` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `yeuthich`
--

INSERT INTO `yeuthich` (`album`, `nguoiDung`) VALUES
(4, 'lahieuphong_customer'),
(6, 'lahieuphong_customer');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`maAlbum`),
  ADD KEY `theLoai` (`theLoai`);

--
-- Chỉ mục cho bảng `baihat`
--
ALTER TABLE `baihat`
  ADD PRIMARY KEY (`maBaiHat`);

--
-- Chỉ mục cho bảng `baihat_album`
--
ALTER TABLE `baihat_album`
  ADD PRIMARY KEY (`BaiHat_maBaiHat`,`Album_maAlbum`),
  ADD KEY `Album_maAlbum` (`Album_maAlbum`);

--
-- Chỉ mục cho bảng `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD PRIMARY KEY (`album`,`hoaDon`),
  ADD KEY `hoaDon` (`hoaDon`);

--
-- Chỉ mục cho bảng `chitietphieunhap`
--
ALTER TABLE `chitietphieunhap`
  ADD PRIMARY KEY (`album`,`phieuNhap`),
  ADD KEY `phieuNhap` (`phieuNhap`);

--
-- Chỉ mục cho bảng `chucnang`
--
ALTER TABLE `chucnang`
  ADD PRIMARY KEY (`maChucNang`);

--
-- Chỉ mục cho bảng `giohang`
--
ALTER TABLE `giohang`
  ADD PRIMARY KEY (`maKhachHang`,`maAlbum`),
  ADD KEY `maAlbum` (`maAlbum`);

--
-- Chỉ mục cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD PRIMARY KEY (`maHoaDon`),
  ADD KEY `khachHang` (`khachHang`),
  ADD KEY `khuyenMai` (`khuyenMai`);

--
-- Chỉ mục cho bảng `khuyenmai`
--
ALTER TABLE `khuyenmai`
  ADD PRIMARY KEY (`maKhuyenMai`);

--
-- Chỉ mục cho bảng `loainguoidung`
--
ALTER TABLE `loainguoidung`
  ADD PRIMARY KEY (`maloai`);

--
-- Chỉ mục cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  ADD PRIMARY KEY (`maNguoiDung`),
  ADD KEY `loainguoidung` (`loainguoidung`);

--
-- Chỉ mục cho bảng `nhacungcap`
--
ALTER TABLE `nhacungcap`
  ADD PRIMARY KEY (`maNCC`);

--
-- Chỉ mục cho bảng `phieunhap`
--
ALTER TABLE `phieunhap`
  ADD PRIMARY KEY (`maPhieuNhap`),
  ADD KEY `nguoiNhap` (`nguoiNhap`),
  ADD KEY `NCC` (`NCC`);

--
-- Chỉ mục cho bảng `quyen`
--
ALTER TABLE `quyen`
  ADD PRIMARY KEY (`maCTQ`),
  ADD KEY `chucNang` (`chucNang`);

--
-- Chỉ mục cho bảng `slideshow`
--
ALTER TABLE `slideshow`
  ADD PRIMARY KEY (`maHinh`),
  ADD KEY `linkTo` (`linkTo`);

--
-- Chỉ mục cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD PRIMARY KEY (`username`),
  ADD KEY `vaiTro` (`vaiTro`);

--
-- Chỉ mục cho bảng `theloai`
--
ALTER TABLE `theloai`
  ADD PRIMARY KEY (`maLoai`);

--
-- Chỉ mục cho bảng `vaitro`
--
ALTER TABLE `vaitro`
  ADD PRIMARY KEY (`maVaiTro`);

--
-- Chỉ mục cho bảng `vaitro_quyen`
--
ALTER TABLE `vaitro_quyen`
  ADD PRIMARY KEY (`VaiTro_maVaiTro`,`Quyen_maCTQ`),
  ADD KEY `Quyen_maCTQ` (`Quyen_maCTQ`);

--
-- Chỉ mục cho bảng `yeuthich`
--
ALTER TABLE `yeuthich`
  ADD PRIMARY KEY (`album`,`nguoiDung`),
  ADD KEY `nguoiDung` (`nguoiDung`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `baihat`
--
ALTER TABLE `baihat`
  MODIFY `maBaiHat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  MODIFY `maHoaDon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT cho bảng `slideshow`
--
ALTER TABLE `slideshow`
  MODIFY `maHinh` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `album`
--
ALTER TABLE `album`
  ADD CONSTRAINT `album_ibfk_1` FOREIGN KEY (`theLoai`) REFERENCES `theloai` (`maLoai`);

--
-- Các ràng buộc cho bảng `baihat_album`
--
ALTER TABLE `baihat_album`
  ADD CONSTRAINT `baihat_album_ibfk_2` FOREIGN KEY (`Album_maAlbum`) REFERENCES `album` (`maAlbum`),
  ADD CONSTRAINT `baihat_album_ibfk_3` FOREIGN KEY (`BaiHat_maBaiHat`) REFERENCES `baihat` (`maBaiHat`);

--
-- Các ràng buộc cho bảng `chitiethoadon`
--
ALTER TABLE `chitiethoadon`
  ADD CONSTRAINT `chitiethoadon_ibfk_1` FOREIGN KEY (`album`) REFERENCES `album` (`maAlbum`),
  ADD CONSTRAINT `chitiethoadon_ibfk_2` FOREIGN KEY (`hoaDon`) REFERENCES `hoadon` (`maHoaDon`);

--
-- Các ràng buộc cho bảng `chitietphieunhap`
--
ALTER TABLE `chitietphieunhap`
  ADD CONSTRAINT `chitietphieunhap_ibfk_1` FOREIGN KEY (`album`) REFERENCES `album` (`maAlbum`),
  ADD CONSTRAINT `chitietphieunhap_ibfk_2` FOREIGN KEY (`phieuNhap`) REFERENCES `phieunhap` (`maPhieuNhap`);

--
-- Các ràng buộc cho bảng `giohang`
--
ALTER TABLE `giohang`
  ADD CONSTRAINT `giohang_ibfk_1` FOREIGN KEY (`maAlbum`) REFERENCES `album` (`maAlbum`),
  ADD CONSTRAINT `giohang_ibfk_2` FOREIGN KEY (`maKhachHang`) REFERENCES `nguoidung` (`maNguoiDung`);

--
-- Các ràng buộc cho bảng `hoadon`
--
ALTER TABLE `hoadon`
  ADD CONSTRAINT `hoadon_ibfk_1` FOREIGN KEY (`khachHang`) REFERENCES `nguoidung` (`maNguoiDung`),
  ADD CONSTRAINT `hoadon_ibfk_2` FOREIGN KEY (`khuyenMai`) REFERENCES `khuyenmai` (`maKhuyenMai`);

--
-- Các ràng buộc cho bảng `nguoidung`
--
ALTER TABLE `nguoidung`
  ADD CONSTRAINT `nguoidung_ibfk_2` FOREIGN KEY (`loainguoidung`) REFERENCES `loainguoidung` (`maloai`);

--
-- Các ràng buộc cho bảng `phieunhap`
--
ALTER TABLE `phieunhap`
  ADD CONSTRAINT `phieunhap_ibfk_1` FOREIGN KEY (`nguoiNhap`) REFERENCES `nguoidung` (`maNguoiDung`),
  ADD CONSTRAINT `phieunhap_ibfk_2` FOREIGN KEY (`NCC`) REFERENCES `nhacungcap` (`maNCC`);

--
-- Các ràng buộc cho bảng `quyen`
--
ALTER TABLE `quyen`
  ADD CONSTRAINT `quyen_ibfk_1` FOREIGN KEY (`chucNang`) REFERENCES `chucnang` (`maChucNang`);

--
-- Các ràng buộc cho bảng `slideshow`
--
ALTER TABLE `slideshow`
  ADD CONSTRAINT `slideshow_ibfk_1` FOREIGN KEY (`linkTo`) REFERENCES `album` (`maAlbum`);

--
-- Các ràng buộc cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD CONSTRAINT `taikhoan_ibfk_1` FOREIGN KEY (`vaiTro`) REFERENCES `vaitro` (`maVaiTro`),
  ADD CONSTRAINT `taikhoan_ibfk_2` FOREIGN KEY (`username`) REFERENCES `nguoidung` (`maNguoiDung`);

--
-- Các ràng buộc cho bảng `vaitro_quyen`
--
ALTER TABLE `vaitro_quyen`
  ADD CONSTRAINT `vaitro_quyen_ibfk_1` FOREIGN KEY (`VaiTro_maVaiTro`) REFERENCES `vaitro` (`maVaiTro`),
  ADD CONSTRAINT `vaitro_quyen_ibfk_2` FOREIGN KEY (`Quyen_maCTQ`) REFERENCES `quyen` (`maCTQ`);

--
-- Các ràng buộc cho bảng `yeuthich`
--
ALTER TABLE `yeuthich`
  ADD CONSTRAINT `yeuthich_ibfk_1` FOREIGN KEY (`album`) REFERENCES `album` (`maAlbum`),
  ADD CONSTRAINT `yeuthich_ibfk_2` FOREIGN KEY (`nguoiDung`) REFERENCES `nguoidung` (`maNguoiDung`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
