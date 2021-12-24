# Green Scene 

![readme](https://user-images.githubusercontent.com/89387904/147282281-d8bcb7a6-2397-4950-a567-9c77fb3ba48e.png)

Green Scene adalah sebuah website dinamis yang dapat membantu masyarakat untuk memahami pentingnya kebersihan lingkungan. Green Scene dilengkapi dengan fitur deteksi Machine Learning sehingga dapat mendeteksi kebersihan lingkungan dari gambar yang diupload. 
Link Website dapat diakses sebagai berikut : [https://green-scene-app.herokuapp.com/](https://wecannohate.herokuapp.com/)

## Deskrpisi Project

Semakin hari semakin berkurangnya kesadaran manusia akan kebersihan. Hal ini ditandai dengan banyaknya tempat berisi tumpukan sampah yang membuat lingkungan tidak enak dilihat. Sudah seharusnya masyarakat memiliki kesadaran untuk membersihkan lingkungan sekitarnya. Maka dari itu, dengan memanfaatkan *machine learning* kami membuat mesin pendeteksi kebersihan lingkungan dengan mengidentifikasi gambar masukan guna mengingatkan masyarakat pentingnya menjaga kebersihan lingkungan sekitar.

How to Clone to your computer

CD yang ditunjuk ke direktori diinginkan, kemudian jalankan perintah dibawah ini :

```
git clone https://github.com/alisyap28/backend-green-scene
```

## Components that need to be installed

Sebelum menjalankan backend, pastikan terlebih dahulu pada VSCode sudah melakukan install pada terminal sebagai berikut :

- pip install keras
- pip install tensorflow
- pip install flask_cors
- pip install pandas
- pip install base64

## Cara Menjalankan Project ini

1. Melakukan clone yang dapat dilanjutkan dengan membuka VSCode
2. Jalankan pip install venv
3. Jalankan venv di project dir
4. Lalu masukkan code ini pada terminal
```
.\venv\Scripts\activate
```

Namun, bila terjadi error bisa masukkan code dibawah ini kemudian jalankan kembali code diatas

```
Set-ExecutionPolicy Unrestricted -Scope Process
```

1. Kemudian jalankan code dibawah ini

```
python ./app.py
```

Backend pun telah hidup, selanjutnya bila ingin mengujinya dapat membuka Front-End atau tampilannya sehingga bisa dijalankan dengan maksimal

## Library or external repository/API used:

- https://github.com/tensorflow/tensorflow
- https://github.com/python-pillow/Pillow
- https://github.com/pandas-dev/pandas
- https://github.com/corydolphin/flask-cors
- https://github.com/pallets/flask
