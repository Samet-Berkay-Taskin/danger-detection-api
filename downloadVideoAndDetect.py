from detectionVideo import detectVideo
from pytube import YouTube
import ssl
import time
import os

ssl._create_default_https_context = ssl._create_stdlib_context


def download_video(url, output_path='uploaded_videos'):
    try:
        # YouTube video nesnesini oluştur
        yt = YouTube(url)
        print(yt.title , 'yt')

        # Video kalitesini
        video = yt.streams.first()

        # İndirme işlemi
        print(f"İndiriliyor: {yt.title}...")
        downloaded_file_path = video.download(output_path)
        print("İndirme tamamlandı!")

        # İndirilen video dosyasının adını küçük harfe dönüştür ve boşlukları kaldır
        downloaded_file_name = os.path.basename(downloaded_file_path)
        renamed_file_path = os.path.join(output_path, downloaded_file_name.lower().replace(" ", ""))

        # Dosyayı yeniden adlandır
        os.rename(downloaded_file_path, renamed_file_path)

        print("İndirme ve yeniden adlandırma tamamlandı!")

        # Yeniden adlandırılmış video dosyasının adını döndür
        return os.path.basename(renamed_file_path)

    except Exception as e:
        print(f"Hata: {e}")
        return None


def download_video_url(url, model_name):
    video_name = download_video(url)
    detectVideo(video_name, model_name)

