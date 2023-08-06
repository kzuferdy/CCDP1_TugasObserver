class Request:
    def __init__(self, jenis, detail):
        self.jenis = jenis
        self.detail = detail


from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next_handler(self, handler):
        pass

    @abstractmethod
    def handle_request(self, request):
        pass 

class FloraHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if request.jenis == 'flora':
            # Lakukan penanganan permintaan informasi flora berdasarkan detail permintaan
            print("Menampilkan informasi flora tentang:", request.detail)
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)


class FaunaHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if request.jenis == 'fauna':
            # Lakukan penanganan permintaan informasi fauna berdasarkan detail permintaan
            print("Menampilkan informasi fauna tentang:", request.detail)
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)


class NotFoundHandler(Handler):
    def handle_request(self, request):
        # Jika tidak ada handler yang sesuai, tampilkan pesan kesalahan
        print("Data tidak ditemukan.")
def main():
    # Inisialisasi handler
    flora_handler = FloraHandler()
    fauna_handler = FaunaHandler()
    not_found_handler = NotFoundHandler()

    # Konfigurasi rantai handler
    flora_handler.set_next_handler(fauna_handler)
    fauna_handler.set_next_handler(not_found_handler)

    # Contoh penggunaan pola Chain of Responsibility
    request_flora = Request('flora', 'Mawar')
    request_fauna = Request('fauna', 'Harimau')
    request_unknown = Request('gejala', 'Ini adalah permintaan yang tidak valid')

    # Kirim permintaan ke awal rantai handler
    flora_handler.handle_request(request_flora)
    flora_handler.handle_request(request_fauna)
    flora_handler.handle_request(request_unknown)

if __name__ == "__main__":
    main()
