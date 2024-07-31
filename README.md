# 🛠️ Audio Converter

Audio Converter, ses dosyalarını kolayca dönüştürmenizi sağlayan güçlü bir araçtır. Bu proje, farklı ses formatları arasında dönüştürme işlemleri yapmanıza olanak tanır ve geniş ses desteği ile birlikte gelir.


## 🚀 Özellikler

- 🤝   **Çoklu Format Desteği:** MP3, WAV, FLAC, OGG ve daha fazlası.
   <details><summary></summary>".mp3",".wav", ".aiff", ".aif", ".flac", ".mp4", ".m4a", ".m4b", ".ogg",".wma", ".aac", ".amr", ".3gp", ".webm", ".ac3", ".opus"</details>
- 📈 **Hızlı Dönüştürme:** Aynı anda birden fazla dosyayı hızlı bir şekilde dönüştürme kapasitesi.
- ⏳ **Kolaylık ve Otomatiklik:** Basit bir şekilde tek argümanla dönüştürün!
- 🔀 **Çoklu İş Parçacığı (Threading):** Performansı artırmak için çoklu iş parçacığı kullanımı.
- 💻 **Komut arayüzü tabanlı(TUI):** Komut arayüzünde basit komutlar ile kullanım.

## 📦 Kurulum

### Not:
⚠️ **Kurulum basit ve anlaşılır anlatılmıştır. Önerilen kaynak kodunun (python dosyasının) indirilmesidir. İnternette, githubda bile olsa kaynak kodu bilinmeyen dosyaları indirmeyin.**

## 💾 Exe Şeklinde

- **+** Gereksinim yok
- **+** Kurulum yok
- **-** Kaynak kodu düzenlenemez
- **-** Smart screen hatası.

### Adımlar
1. **Exe'yi indirin:**
   [AudioConverter.exe](https://github.com/Berkwe/Audio-converter/releases/download/1.0/AudioConverter.exe)


2. **Cmd veya powershell ile çalıştırın:**
   
   <img src="https://github.com/user-attachments/assets/3f626631-7b22-42bb-ba75-720d2efd047a" alt="" height="100">
   

   - **Terminalde Audio Converter'in olduğu klasörü açın.**
   - **[Buradan kullanımı öğrenin](https://github.com/Berkwe/Audio-converter?tab=readme-ov-file#-exe-ile)**
   
## 🐍 Python Şeklinde:

### Gereksinimler

- Python 3.6 veya üzeri
- Pydub
- FFmpeg

### Adımlar

1. **Python ve Pydub Kurulumu:**

   ```bash
   pip install pydub
   ```

2. **FFmpeg İndirimi ve Kurulumu:**

   - Windows için indirin(yeniden başlatma gerekebilir):
     
     ```bash
     winget install "FFmpeg (Essentials Build)"
     ```
     
   - [Farklı bir dağıtım mı? FFmpeg İndir](https://ffmpeg.org/download.html) ve işletim sisteminize uygun olanı kurun.
   - FFmpeg'in kurulu olduğundan emin olmak için terminalde şu komutu çalıştırın:

     ```bash
     ffmpeg -version
     ```

4. **Projeyi İndirme:**

   - **[Zip](https://github.com/Berkwe/Audio-converter/archive/refs/heads/main.zip)'i indirin**
     ### **Veya**
   - **Git ile klonlayın:**
     
   ```bash
   git clone https://github.com/Berkwe/Audio-converter
   cd Audio-converter
   ```

## 🛠️ Kullanım

### 💾 Exe ile:

   ```bash
   .\AudioConverter --inPath "giriş_klasörü" --outPath "çıkış_klasörü" --inExt giriş_uzantısı --outExt çıkış_uzantısı --maxT iş_parçacığı_sayısı
   ```

   Örnek Kullanım:

   ```bash
   .\AudioConverter --inPath "C:\\sesDosyalarım\\" --outPath "C:\\mp3UzantılıSesDosyalarım" --inExt wav --outExt mp3 --maxT 10
   ```
   
### 🐍 Python ile:
   ```bash
   python AudioConverter.py --inPath "giriş_klasörü" --outPath "çıkış_klasörü" --inExt giriş_uzantısı --outExt çıkış_uzantısı --maxT iş_parçacığı_sayısı
   ```

   Örnek Kullanım:

   ```bash
   python AudioConverter.py --inPath "C:\\sesDosyalarım\\" --outPath "C:\\mp3UzantılıSesDosyalarım" --inExt wav --outExt mp3 --maxT 10
   ```
  
## </> Komutlar ve Seçenekler:

   - `--help, -h`: Yardım mesajını gösterir.
   - `--inPath, -i`: Ses dosyalarının seçileceği klasör. (zorunlu)
   - `--outPath, -o`: Uzantısı değiştirilen ses dosyalarının yazılacağı klasör.
   - `--inExt, -ie`: Değiştirilecek uzantı.
   - `--outExt, -oe`: Seçilen uzantılı dosyaların değiştirileceği uzantı.
   - `--maxT`: Kullanılacak iş parçacığı sayısı. (varsayılan=20)

## ⓘ Performans

Sorun ve önerileriniz için [Issues](https://github.com/Berkwe/Audio-converter/issues) kısmını kullanabilirsiniz.

## 🌟 Diğer Projelerim

-  **[ADB Brute-Force](https://github.com/Berkwe/ADB-bruteforce): Wirelles ADB açık olan cihazlara Brute-Force uygulamak.**
-  **[Valorant-İnstalocker](https://github.com/Berkwe/Valorant-instalocker): Python ile Valorant için İnstalocker.**
  
## 📞 İletişim

<a href="https://discord.gg/Xagnh5aYSy" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="F7qaRp22bW" height="30" width="40" /></a>



## 📝 Lisans

Bu proje [GPL Lisansı](https://github.com/Berkwe/Audio-converter?tab=GPL-3.0-1-ov-file) altında lisanslanmıştır.
