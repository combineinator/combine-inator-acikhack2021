# combine-inator-acikhack2021

Birçok farklı kaynaktaki verileri işleyebilen Combine-Inator ile tanışın! Adını Fineas ve Ferb adlı çizgi-diziden alan Combine-Inator adlı projemiz ses, metin ve görüntü şeklinde alınan verileri kullanarak doğal dil işleme projelerine dönüştürebilmektedir.

![](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4943c953-a53e-40f5-adb6-0b6778e88a61/d6qyszz-dd34d2a2-850a-4ef0-a10b-f5de4d5d5d90.jpg/v1/fill/w_1024,h_722,q_75,strp/dr__doofenshmirtz_and_the_combine_inator__by_zackary_d6qyszz-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzIyIiwicGF0aCI6IlwvZlwvNDk0M2M5NTMtYTUzZS00MGY1LWFkYjYtMGI2Nzc4ZTg4YTYxXC9kNnF5c3p6LWRkMzRkMmEyLTg1MGEtNGVmMC1hMTBiLWY1ZGU0ZDVkNWQ5MC5qcGciLCJ3aWR0aCI6Ijw9MTAyNCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.HDuDRFU94zTKi6_QNwo2q44stlJRsVyWTZEe9EXFPN0)

## Amacımız

* Proje fikri kapsamında; metin, ses ve görüntü verileri gibi farklı kaynaklardan elde edilen bilgilerin Türkçe dili özelinde anlamlı hale getirilmesini sağlayacak yapay zeka uygulamaları yer almaktadır. 

* Bahsedilen problemlerin son kullanıcının dahi kullanabileceği şekilde kolay bir yapı içerisinde sunulması ve geliştiriciler tarafından kolay bir şekilde kullanılabilecek bir kütüphane ve kullanım kolaylığı açısından web arayüzü olarak sunulması amaçlanmıştır. 

* Projenin kapsamının, derin öğrenmenin birçok alanından gelen çıktılarının (Görüntü işleme, Sinyal İşleme vb.) doğal dil işlemeye yönelik kullanımlarını içermesi ve kullanıcı dostu bir yapı içerisinde sunuluyor olması nedeni ile "Türkçe Doğal Dil İşleme" alanında oldukça faydalı olacağına inanmaktayız.

* Kütüphane dahilinde sunduğumuz Türkçe veri toplama aracı ile de özellikle sınıflandırma problemlerinde karşılaşılan Türkçe veri yetersizliği sorununun çözülebileceğini düşünmekteyiz.

* Python kodlama dili kullanılan çalışmada literatürdeki en güncel algoritmalara ve mimarilere (State-Of-Art) de yer verilmiş, bu sayede doğruluk oranlarının yüksek olması hedeflenmiştir.

## Gereksinimler
python
numpy -- 

## Modüller

### Wikipedia Web Scrapper

Türkçe dili için veri yetersizliğine çözüm olacak bu modül sayesinde yalnızca birkaç parametre ile tonlarca veri toplanabilmektedir. 


#### Kullanım:
python
import categorical_scraper


#### Benzer Kütüphaneler:
* [Wikipedia-API](https://pypi.org/project/Wikipedia-API/) : Bu kütüphanenin sağladığı özellikler yalnızca İngilizce dili ile sınırlıdır. Ancak geliştirdiğimiz... 
* [wikipedia](https://pypi.org/project/wikipedia/) : Bu kütüphanenin sağladığı özellikler yalnızca İngilizce dili ile sınırlıdır. Ancak geliştirdiğimiz... 

#### Yararlanılan Kaynaklar:
* blabla

### Speech Translator Modülü

Bu modül sayesinde kullanıcıdan Türkçe veya İngilizce olarak alınan ses verisi uçtan uca oluşturulmuş yapı sayesinde hedeflenen dilde tercümesi yapılıp, kullanıcının sesi şeklinde veya metin şeklinde çıktı verilebilmektedir. 

![](https://images.squarespace-cdn.com/content/v1/5a4908d949fc2b8e312bdf53/1518166057021-0GJ15P9C7Y6LBFJT2J12/speech.png?format=750w) 

#### Örnek Çalışma:
|Verilen Ses Kaydındaki Cümle|Text'te Dönüştürülen Cümle| Çevirilen Cümle |
 |:------:|:------:|:------:|
|Merhaba nasılsın günün iyi geçiyor mu|Merhaba nasılsın günün iyi geçiyor mu|hello how are you having a good day|

MP3, WAV Files Verilen ses dosyalarının çevirilmesi ile oluşan ve farklı dilde telaffuz ettirilerek kaydedilen dosya ikililerine [buradan]() ulaşabilirsiniz.

#### Kullanım:
python
import speech_translator



#### Benzer Kütüphaneler:
* [marcominerva](https://github.com/marcominerva)/**[TranslatorService](https://github.com/marcominerva/TranslatorService)** : Bu kütüphanenin kullanımı için Azure servislerine kayıt gereklidir. Ancak geliştirdiğimiz kütüphanede açık kaynaklı transformatör modelleri kullanıldığından dolayı herhangi bir servise bağımlılığı yoktur.

* [Google Cloud Speech Translation](https://cloud.google.com/architecture/speech-translation-android-microservice) Bu kütüphanenin kullanımı için Google Cloud servislerine kayıt gerekli ve hizmet bedeli alınmaktadır. Ancak geliştirdiğimiz kütüphanede açık kaynaklı transformatör modelleri kullanıldığından dolayı herhangi bir servise bağımlılığı olmamakla birlikte herhangi bir hizmet bedeline de gereksinim duyulmamaktadır.

* [respeaker](https://github.com/respeaker)/**[Python-Speech-Translate](https://github.com/respeaker/Python-Speech-Translate)** : Azure servislerine ihtiyaç duyan kütüphane ayrıca Python 2 diline yönelik yazılmıştır. Hem servis bağlılığı bulunan hem de Python'ın eski sürümünü kullanan bu kütüphanenin kullanımı sırasında paket uyumsuzluğu gibi durumlarla karşılaşılabilir. Oysa Python 3.6 sürümü ile yazılmış kütüphanemiz kullanılan paketler açısından güncelliğini korumaktadır. 

* [auto-translation](https://pypi.org/project/auto-translation/) : Selenium kütüphanesi yardımıyla Google Translate üzerinden çeviri yapan bu kütüphanenin kullanımı için online bir çeviri hizmeti sunulmasından dolayı çevrimiçi bağlantıya ihtiyaç duyulmaktadır. Geliştirdiğimiz kütüphane ilgili transformatör tabanlı modelleri içe aktardığından, modellerin içe aktarılması sonrasında internet bağlantısına ihtiyaç duymamakta ve offline olarak çalışabilmektedir.

#### Yararlanılan Kaynaklar:
* blabla

### LXMERT Modülü

Kullanıcıdan alınan görselin işlenerek metin halinde görsele dair sorulan bir sorunun cevabını verebilen bu modül sayesinde görüntü işleme ve doğal dil işleme alanları birleştirilmiştir. 

#### Kullanım:
python
import lxmert


#### Yararlanılan Kaynaklar:
* [LXMERT: Learning Cross-Modality Encoder Representations from Transformers](https://arxiv.org/abs/1908.07490)

## Mimari Yapı

(Diyagram fotosu eklenecek)

## Kullanılan Veri Setleri

|Veri Seti|Açıklaması|Kullanım Alanı|
|:------:|:------:|:------:|
|Veri seti 1|Kısa cümlelerden oluşan Türkçe veri setidir.|.. modelinin eğitimi sırasında kullanılmıştır.|

## Ekibimiz

![](https://user-images.githubusercontent.com/52993055/130331713-ec2b7a7d-9886-44de-9855-6e489c5d1b76.png)


### [Oğuzhan Ölmez](https://github.com/oguzhanolm) (Takım Kaptanı)
1999 yılında doğmuş olup, Celal Bayar Üniversitesi Yazılım Mühendisliği mezunudur. Eylül 2020-Ocak 2021 arasında BulutMD Yazılım Şirketi’nde Java Developer olarak staj yapmış ve bir segmentasyon projesi üzerine çalışmıştır. 2021 Mart-2021 Temmuz ayları arasında AdresGezgini şirketinde makine öğrenmesi ve derin öğrenme üzerine araştırma stajyeri olarak görev almıştır. Şuan içerisinde bulunduğu araştırma grubu ile NLP alanında araştırmalar yapmaya devam etmektedir.

### [Seçilay Kutal](https://github.com/seccily)

1999 yılında doğmuş olup, Marmara Üniversitesi Mekatronik Mühendisliği mezunudur. Teknofest Roket Yarışması’nda 2 sene Marmara Dynamics roket takımı kaptanlığı ve 1-2 sene gibi çeşitli sürelerde çeşitli kulüplerin yönetim kurulu üyeliği görevlerini üstlenmiştir. Yapay zeka üzerine son 1.5 yıldır, doğal dil işleme özelinde ise son 6 aydır çalışmaktadır. Bitirme projesini panoramik röntgenler üzerinden derin öğrenme ile diş ve hastalık tespiti üzerine gerçekleştirmiştir. Doğal dil işleme alanında ise geçtiğimiz aylarda tamamlamış olduğu transformatör mimarilerine dayanan bir akademik yayın çalışması mevcuttur. Medium üzerinde "Deeper Deep Learning" kanalında bilgilerini paylaşmaya çalışmakta ve bir yandan makine öğrenmesi, derin öğrenme alanlarında kendini geliştirmeye devam etmektedir.
