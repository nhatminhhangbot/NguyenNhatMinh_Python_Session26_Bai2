# Tính đa hình: hệ thống chỉ tương tác với phương thức use_ultimate(), tự động gọi đúng hành vi tương ứng của từng hệ tướng qua đối tượng hero
# Game chỉ văng lỗi NotImplementedError vào thời điểm vòng lặp for chạy đến phần tử Assassin và gọi hero.use_ultimate()
# Người chơi đang giao tranh thì game đột ngột văng lỗi => gây ức chế => tăng nguy cơ tụt rank, mất chuỗi thắng => giảm tỷ lệ giữ chân người dùng
# Thời điểm văng lỗi khi sử dụng thư viện abc: lúc loading ván đấu
# Code đúng:

from abc import ABC, abstractmethod

# Lớp cha: Khuôn mẫu tướng (áp dụng ABC)


class Hero(ABC):
    @abstractmethod
    def use_ultimate(self):
        """Phương thức trừu tượng: Ép buộc tất cả các lớp con phải ghi đè."""
        pass

# Lớp con 1: Pháp sư


class Mage(Hero):
    def use_ultimate(self):
        print("Pháp Sư tung chiêu: MƯA SAO BĂNG!")

# Lớp con 2: Sát thủ


class Assassin(Hero):
    def use_ultimate(self):
        print("Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


# --- KỊCH BẢN LỖI RUNTIME ---
print("--- LOADING TRẬN ĐẤU ---")
# Nếu lúc này Assassin chưa ghi đè use_ultimate => văng lỗi TypeError
team_heroes = [Mage(), Assassin()]
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
# Vòng lặp Đa hình
for hero in team_heroes:
    hero.use_ultimate()
