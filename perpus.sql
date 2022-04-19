-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 16 Apr 2022 pada 14.53
-- Versi server: 10.4.21-MariaDB
-- Versi PHP: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpus`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_buku`
--

CREATE TABLE `data_buku` (
  `id_buku` varchar(5) NOT NULL,
  `subjek` varchar(50) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `penulis` varchar(50) NOT NULL,
  `info` varchar(50) NOT NULL,
  `stok` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_buku`
--

INSERT INTO `data_buku` (`id_buku`, `subjek`, `judul`, `penulis`, `info`, `stok`) VALUES
('001', 'Orang-orang Biasa', 'Andrea Hirata', 'Novel Lt 1 Rak No 23', '', 30),
('002', 'Negeri Para Bedebah', 'Tere Liye', 'Novel', '', 30);

-- --------------------------------------------------------

--
-- Struktur dari tabel `kembali`
--

CREATE TABLE `kembali` (
  `id_kembali` int(11) NOT NULL,
  `id_buku` varchar(5) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `tgl_kembali` varchar(50) NOT NULL,
  `jumlah` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `kembali`
--

INSERT INTO `kembali` (`id_kembali`, `id_buku`, `nama`, `tgl_kembali`, `jumlah`) VALUES
(1, '001', 'tester', '2022-04-16', 2),
(2, '001', 'dk', '2022-04-16 13:30:21', 12);

--
-- Trigger `kembali`
--
DELIMITER $$
CREATE TRIGGER `del_in` BEFORE DELETE ON `kembali` FOR EACH ROW BEGIN
	UPDATE barang SET stok= stok - OLD.jumlah
	WHERE id_buku = OLD.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_kembali` AFTER INSERT ON `kembali` FOR EACH ROW BEGIN
	UPDATE data_buku SET stok= stok + NEW.jumlah
	WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `peminjam`
--

CREATE TABLE `peminjam` (
  `id_pinjam` int(11) NOT NULL,
  `id_buku` varchar(5) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `tgl_keluar` date NOT NULL,
  `jumlah` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `peminjam`
--

INSERT INTO `peminjam` (`id_pinjam`, `id_buku`, `nama`, `tgl_keluar`, `jumlah`) VALUES
(1, '001', 'tester', '2022-04-16', 2),
(2, '002', 'teste2', '2022-04-16', 4),
(3, '001', 'dk', '2022-04-16', 12);

--
-- Trigger `peminjam`
--
DELIMITER $$
CREATE TRIGGER `del_out` AFTER DELETE ON `peminjam` FOR EACH ROW BEGIN
	UPDATE data_buku SET stok= stok + OLD.jumlah
	WHERE id_buku = OLD.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_out` AFTER INSERT ON `peminjam` FOR EACH ROW BEGIN
	UPDATE data_buku SET stok= stok - NEW.jumlah
	WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `data_buku`
--
ALTER TABLE `data_buku`
  ADD PRIMARY KEY (`id_buku`);

--
-- Indeks untuk tabel `kembali`
--
ALTER TABLE `kembali`
  ADD PRIMARY KEY (`id_kembali`);

--
-- Indeks untuk tabel `peminjam`
--
ALTER TABLE `peminjam`
  ADD PRIMARY KEY (`id_pinjam`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `kembali`
--
ALTER TABLE `kembali`
  MODIFY `id_kembali` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `peminjam`
--
ALTER TABLE `peminjam`
  MODIFY `id_pinjam` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
