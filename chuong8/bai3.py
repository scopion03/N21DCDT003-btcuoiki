class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        """
        Nhập thông tin của một album vào từ điển.
        
        :param ten_album: Tên của album
        :param danh_sach_bai_hat: Danh sách các bài hát trong album, mỗi bài hát là một dictionary với các thông tin
                                  'ten_bai_hat', 'ten_nhac_si', và 'ten_ca_si'.
        """
        if ten_album in self.albums:
            print(f"Album '{ten_album}' đã tồn tại trong từ điển.")
            return

        self.albums[ten_album] = danh_sach_bai_hat

    def XemAlbum(self, ten_album):
        """
        Hiển thị thông tin của album có tên là 'ten_album'.
        
        :param ten_album: Tên của album cần hiển thị thông tin
        :return: None
        """
        if ten_album not in self.albums:
            print(f"Album '{ten_album}' không có trong từ điển.")
            return

        print(f"Album: {ten_album}")
        danh_sach_bai_hat = self.albums[ten_album]
        for bai_hat in danh_sach_bai_hat:
            print(f"  - Tên bài hát: {bai_hat['ten_bai_hat']}")
            print(f"    Nhạc sĩ: {bai_hat['ten_nhac_si']}")
            print(f"    Ca sĩ: {bai_hat['ten_ca_si']}")
            print()

# Ví dụ sử dụng lớp TuDien
td = TuDien()
td.NhapAlbum("Album 1", [
    {"ten_bai_hat": "Bài hát 1", "ten_nhac_si": "Nhạc sĩ 1", "ten_ca_si": "Ca sĩ 1"},
    {"ten_bai_hat": "Bài hát 2", "ten_nhac_si": "Nhạc sĩ 2", "ten_ca_si": "Ca sĩ 2"},
])

td.NhapAlbum("Album 2", [
    {"ten_bai_hat": "Bài hát 3", "ten_nhac_si": "Nhạc sĩ 3", "ten_ca_si": "Ca sĩ 3"},
    {"ten_bai_hat": "Bài hát 4", "ten_nhac_si": "Nhạc sĩ 4", "ten_ca_si": "Ca sĩ 4"},
])

# Xem thông tin album
td.XemAlbum("Album 1")
td.XemAlbum("Album 2")
td.XemAlbum("Album 3")  # Album không tồn tại
