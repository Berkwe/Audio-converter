import os, threading, sys, time
from prettytable import PrettyTable, DOUBLE_BORDER
from pydub import AudioSegment
from queue import Queue

# Coded by berkwe_

######## Bu projenin genel yapısı(eylem sırası, queue modülünün kullanımı vb) için yapay zekadan yardım alınmıştır fakat kopyala yapıştır yapılmamıştır. ########

######## Yorum satırlarının fazlalığını gören fazla bilgili(!) kişiler kodları yapay zekaya yazdırdığımı sandığı için yorum satırları azaltılmıştır. ########

######## Yorum satırlarını İngilizcemi geliştirmeye çalışmak için ingilizce eklemeye çalıştım. Arada istekli/isteksiz yazım yanlışları olabilir. ########

supportedExt = {".mp3",".wav", ".aiff", ".aif", ".flac", ".mp4", ".m4a", ".m4b", ".ogg",".wma", ".aac", ".amr", ".3gp", ".webm", ".ac3", ".opus"}
convertedAudios = 1
error = "[!] "
info = "[*] "
success = "[+] "

AudioSegment.ffmpeg = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")

if os.name == 'posix':
    os.system("clear")
    sil = "clear"
elif os.name == 'nt':
    os.system("color a&&cls")
    sil = "cls"
else:
    print(f"{error}Bu işletim sistemi desteklenmiyor.") # MacOs'a boykot!!!!
    time.sleep(5)
    sys.exit()

# Create queue and add files
def createQueue(inPath, inExt):
    fileQueue = Queue()
    try:
        for file in os.listdir(inPath):
            if file.endswith(inExt):
                fileQueue.put(inPath+"\\"+file)
    except Exception as f:
        print(f"{error}Queue'de bir hata oluştu! Lütfen githubdan geliştiriciye bildirin : {f}")
        
        sys.exit()

    return fileQueue

# A function for convert audios (sori for may bad england :(((((()
def convert(fileQueue: Queue, inExt, outExt, outPath):
    global convertedAudios
    while True:
        file = fileQueue.get()
        if file is None:
            break
        try:
            audio = AudioSegment.from_file(file, inExt.replace(".", ""))
            outPathForAudio = os.path.join(outPath, os.path.basename(file).replace(inExt, outExt))
            audio.export(outPathForAudio, format=outExt.replace(".", ""))
            print(f"{success}Başarılı! Dönüştürülen dosyalar : {convertedAudios}, {os.path.basename(file)} --> {os.path.basename(file).replace(inExt, outExt)}")
            convertedAudios += 1
        except Exception as f:
            print(f"{error}Dönüştürülürken bir hata oluştu! Lütfen githubdan geliştiriciye bildirin : {f}")
            
            sys.exit()
        finally:
            fileQueue.task_done()
# For control table
def createTable(inPath, outPath, inExt, outExt, maxThreads, fileVal):
    estimatedTime = ((fileVal-(fileVal % 10))/(maxThread-(maxThread % 10)))*4
    table = PrettyTable()
    
    table.field_names = ["Açıklama", "Değer"]
    
    table.add_row(["Giriş Yolu", inPath])
    table.add_row(["", ""])
    table.add_row(["Çıkış Yolu", outPath])
    table.add_row(["", ""])
    table.add_row(["Giriş Uzantısı", inExt])
    table.add_row(["", ""])
    table.add_row(["Çıkış Uzantısı", outExt])
    table.add_row(["", ""])
    table.add_row(["Threads", maxThreads])
    table.add_row(["", ""])
    table.add_row(["Toplam Dosya", fileVal])
    table.add_row(["", ""])
    table.add_row(["Tahmini Süre", estimatedTime])
    
    table.align = "l"
    table.max_width = 30
    table.set_style(DOUBLE_BORDER)
    return table

def main(inPath, inExt=None, outPath=None, outExt=None, maxThreads=20):
    os.system(sil)
    if not os.path.exists(inPath):
        print(f"{error}Belirttiğiniz giriş klasörü bulunamadı!")
        
        return
    elif not os.path.isdir(inPath):
        print(f"{error}Belirttiğiniz giriş klasörü, bir klasör değil!")
        
        return
    
    if outPath is None  or not os.path.exists(outPath):
        if outPath is None:
            if os.path.exists(f"{os.path.dirname(inPath)}\\outpath"):
                input(f"{info}Bir çıkış dosyası belirtmediniz, giriş dizinin üst dizininde zaten outpath adlı çıkış klasörü var. klasör kullanılsınmı? (devam etmek için enter)")
            else:
                os.mkdir(f"{os.path.dirname(inPath)}\\outpath")
                print(f"{info}Bir çıkış dizini belirtmediniz, giriş dizinin üst dizinine outpath adlı bir çıkış klasörü oluşturuldu.")
            outPath = f"{os.path.dirname(inPath)}\\outpath"
            
        elif not os.path.exists(outPath):
            if os.path.exists(f"{os.path.dirname(inPath)}\\outpath"):
                input(f"{info}Belirttiğiniz çıkış klasörü bulunamadı, giriş dizinin üst dizininde zaten outpath adlı çıkış klasörü var. klasör kullanılsınmı? (devam etmek için enter)")
            else:
                os.mkdir(f"{os.path.dirname(inPath)}\\outpath")
                print(f"{info}Belirttiğiniz çıkış klasörü bulunamadı, giriş dizinin üst dizinine outpath adlı bir çıkış klasör oluşturuldu.")
            outPath = f"{os.path.dirname(inPath)}\\outpath"
    
    if inExt is None:
        input(f"{info}Değiştirilecek uzantıyı belirtmediniz, giriş klasöründeki ilk dosyanın uzantısı kullanılsınmı?(devam etmek için entere basın.)")
        for file in os.listdir(inPath):
            inExt = os.path.splitext(file)[1]
            if inExt not in supportedExt or inExt == outExt:
                continue
            else:
                break
        if inExt not in supportedExt:
            print(f"{error}Klasörde desteklenen bir uzantı bulunamadı, lütfen farklı bir klasörle deneyin.")
            
            return
        if outExt == inExt:
            print(f"{error}Klasörde belirttiğiniz çıkış uzantısından farklı bir uzantıya sahip dosya bulunamadı, lütfen farklı bir klasörle veya farklı bir --outExt uzantısı kullanarak deneyin.")
            
            return
        print(f"{success}Uzantı seçildi. giriş uzantısı : {inExt}")

    if outExt is None:
        input(f"{info}Dönüştürülecek uzantıyı belirtmediniz, giriş klasöründeki ikinci dosyanın uzantısı kullanılsınmı?(devam etmek için entere basın.)")
        for file in os.listdir(inPath):
            if not file.endswith(inExt):
                outExt = os.path.splitext(file)[1]
                if outExt not in supportedExt:
                    continue
                else:
                    break
        if outExt not in supportedExt:
            print(f"{error}Klasör içerisinde desteklenen bir uzantı bulunamadı. Lütfen inPath argümanına farklı bir klasör verin veya --outExt argümanına dönüştürülecek uzantıyı girin.")
            
            return
        elif outExt is None:
            print(f"{error}Klasör içerisinde farklı uzantıya sahip bir dosya bulunamadı. Lütfen çıktı uzantısını belirtip tekrar deneyin.")
            
            return
        
        print(f"{success}Uzantı seçildi. Çıkış uzantısı : {outExt}")
    os.system(sil)
    print(createTable(inPath=inPath, outPath=outPath, inExt=inExt, outExt=outExt, maxThreads=maxThreads,fileVal=len([file for file in os.listdir(inPath) if os.path.splitext(file)[1] == inExt])))
    input("Kontrol edin, devam etmek için entere basın.".center(200))
    fileQueue = createQueue(inPath, inExt)
    threads = []
    for _ in range(maxThreads):
        thread = threading.Thread(target=convert, args=(fileQueue, inExt, outExt, outPath))
        threads.append(thread)
        thread.start()
    fileQueue.join()
    for _ in range(maxThreads):
        fileQueue.put(None)
    for thread in threads:
        thread.join()
    
def help(lang="tr"):
    if lang == "tr":
        help = """
                <>Kullanılabilecek komutların listesi</>


        --help, -h -> Bu mesajı döndürür.(default=tr)
      
        --inPath, -i -> Ses dosyalarının seçileceği klasör. (zorunlu)
      
        --outPath, -o -> Uzantısı değiştirilen ses dosyalarının yazılacağı klasör.
      
        --inExt, -ie -> Değiştirmek için seçilecek uzantı.
      
        --outExt, -oe -> Seçilen uzantılı dosyaların değiştirileceği uzantı.
      
        --maxT -> Kullanılacak thread sayısı, arttırdıkça hız artar fakat kullanılan bellek artar.(default=20)
      

        Örnek kullanım -> python converter.py -i "C:\\sesDosyalarım\\" -o "C:\\mp3UzantılıSesDosyalarım" --inExt ma4 --outExt mp3 -t 50
        
        Not : 

        * örnek kullanım bilerek karışık gösterilmiştir. Lütfen dosya yollarını tırnak içinde girin ve sonuna \\ veya / gibi ifadeler olmadığına dikkat edin. ("C:\\myfiles")
        * zorunlu argümanlar dışındaki argümanları kullanmasanız da program çalışacaktır, önerilmez.
        * Bir hata alırsanız githubda "issues" kısmında sorununuzu belirtebilirsiniz.
        """
        return help
    
    if lang == "eng":
        help = """
                <>The following commands are available</>

                
        --help, -h -> Returns this message. (default=en)

        --inPath, -i -> Folder to select audio files (required)

        --outPath, -o -> Folder to files of changed extention.
      
        --inExt, -ie -> Select the extension to replace.
      
        --outExt, -oe -> Replace files with the selected extension using the specified extension.
      
        --maxT -> Number of threads to use. Use more threads for faster speed, but be aware that this will also use more memory. (default=20)

        
        Example usage -> python converter.py -i “C:\\myAudioFiles\\” -o “C:\\mp3ExtendedAudioFiles” --inExt ma4 --outExt mp3 -t 50

        Note: 

        * The example usage is intentionally complicated. Please put file paths in quotation marks and make sure that they are not followed by \\ or /. (‘C:\\myfiles’)
        * The program will run even if you don't use arguments other than the mandatory arguments, but it is not recommended.
        * If you get an error, you can report it in the "issues" section on github.
        """
        return help
    else:
        return "Desteklenen diller : tr, eng"

if __name__ == "__main__":
    maxThread = None
    outPath = None
    outExt = None
    inExt = None
    inPath = None
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h" and len(sys.argv) <= 3:
                try:
                    print(help(sys.argv[2]))
                except IndexError:
                    print(help())
                finally:
                    
                    sys.exit()


        for index, argv in enumerate(sys.argv):
            if (argv == "--inPath" or argv == "-i") and not inPath:
                inPath = sys.argv[index + 1]
                
            elif (argv == "--outPath" or argv == "-o") and not outPath:
                outPath = sys.argv[index + 1]

            elif (argv == "--inExt" or argv == "-ie") and not inExt:
                inExt = sys.argv[index + 1]
                if not inExt.startswith("."):
                    inExt = "." + inExt
                if inExt not in supportedExt:
                    print(f"{error}--inExt ile belirttiğiniz uzantı desteklenmiyor!")
                    
                    sys.exit()

            elif (argv == "--outExt" or argv == "-oe") and not outExt:
                outExt = sys.argv[index + 1]
                if not outExt.startswith("."):
                    outExt = "." + outExt
                if outExt not in supportedExt:
                    print(f"{error}--outExt ile belirttiğiniz uzantı desteklenmiyor!")
                    
                    sys.exit()

            elif argv == "--maxT" and not maxThread:
                try:
                    maxThread = int(sys.argv[index + 1])
                except ValueError:
                    print(f"{error}Lütfen {argv} argümanında sadece sayı kullanın.")
                    
                    sys.exit()

            elif argv.startswith("-") or argv.startswith("--"):
                print(f"{error}Bilinmeyen argüman, kullanılabilir komutlar için '--help tr/eng' yazın.")
                
                sys.exit()

        controlLst = [i for i in sys.argv if i.startswith("-") and i != sys.argv[0]]
        argValLst = [i for i in sys.argv if i != sys.argv[0] and not i.startswith("-")]
        
        if not maxThread:
            maxThread = 20
        if len(controlLst) != len(argValLst):
            print(f"{error}Bilinmeyen argüman, kullanılabilir komutlar için '--help tr/eng' yazın.")
            
            sys.exit()

    except IndexError:
        print(f"{error}Lütfen en az bir argüman girin, girdiyseniz doğru olduğundan emin olun. Kullanılabilir komutlar için '--help tr/eng' yazın.")
        time.sleep(5)
        sys.exit()
    except Exception as f:
        print(f"{error}Çalıştırılırken bir hata oluştu! Lütfen githubdan geliştiriciye bildirin : {f}")
        
        sys.exit()

    if inPath:
        main(inExt=inExt, inPath=inPath, outExt=outExt, outPath=outPath, maxThreads=maxThread)
    else:
        print(f"{error}--inPath argümanı girilmesi zorunlu bir argümandır. Lütfen girip tekrar deneyin.")
        
