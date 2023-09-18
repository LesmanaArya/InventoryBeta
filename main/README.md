Tautan Adaptable:
https://inventorybeta.adaptable.app/

TUGAS 2
1. Pertama-tama, kita harus membuat proyek dimana app kita yang bernama main berada. Dalam hal ini, saya menamai proyek sata sebagai InventoryBeta dan kemudian saya hubungkan ke repository github. Setelah tercipta project nya, kita jalankan startapp main untuk membuat app bernama main. Jangan lupa, kita harus menambahkan main pada INSTALLED APPS yang ada di settings.py proyek InventoryBeta. Hal ini bertujuan agar Django mengenali bahwa main merupakan app yang bisa dijalankan. Setelah itu, kita isi models.py dengan Class Item dan atribut-atributnya sesuai yang di ketentuan. Setelah model selesai dibuat, saya terlebih dahulu membuat folder template serta membuat file home.html, agar ketika membuat fungsi di views.py, kita sudah tau file html mana yang mau ditampilkan. Setelah membuat file html nya, saya membuat fungsi home yang digunakan untuk me-render file home.html yang nantinya akan digunakan untuk menampilkan data model kita. Setelah menyelesaikan views, kita isi urls.py yang ada di InventoryBeta supaya kita bisa mengatur rute url agar spesifik ke aplikasi main kita. Disini saya men-setting, jika url nya string kosong, maka langsung jalankan url milik app main agar tidak perlu memasukkan /main lagi. Barulah setelah itu kita mengisi urls.py yang ada di main. Saya setting agar jika kita memasukkan url kosong, maka jalankan fungsi home yang ada di views.py agar secara default, app main akan menampilkan home.html yang adalah tampilan data kita. Terakhir, kita tinggal commit dan push ke github, setelah itu deploy ke Adaptable. Saya juga menambahkan test case untuk model dimana isinya adalah mengecek apakah field dan atribut model Item kita yang diinput dan yang tersimpan sudah benar, serta apakah field name nya sudah sesuai maksimal karakter yang diberikan. 

2. !(Screenshot (1263).png)

3. Virtual environment berfungsi supaya aplikasi dan segala hal yang berhubungan dengan proyek django kita tidak bentrok dengan python dan django versi lainnya yang mungkin saja terinstall di komputer kita yang mungkin saja bisa menyebabkan masalah. Kita bisa saja tidak menggunakan virtual environment untuk project django, tetapi seperti poin diatas, bisa menyebabkan bentrok dengan python atau django versi lain yang terinstall di komputer.

4.
MVT adalah Model View Template, yaitu suatu arsitektur untuk menampilkan web, aplikasi, atau    User Interface lain. Perbedaannya dengan MVC adalah di bagian Template. Template disini adalah kode HTML yang akan befungsi untuk menampilkan respons dari request HTTP client. Model dan View pada MVT akan di-manage atau dijembatani oleh framework.

MVC adalah Model View Controller. Pada MVC, Controller akan berfungsi sebagai jembatan bagi
Model dan View. Controller ini yang akan memerintahkan Model untuk meng-update kondisinya jika ada perubahan serta memerintahkan View untuk menampilkan ke user ataupun mengubah tampilannya jika ada perubahan juga. Hal ini berbeda dengan MVT dimana Template lah yang akan memberikan tampilan ke Client, sementara yang menjadi jembatan antara Model dan View adalah framework.

MVVM adalah Model-View-ViewModel. Pada MVVM, yang menjadi jembatan antar Model dan View adalah Model-View. Model-View ini merupakan tempat dimana function, command, serta method dituliskan untuk membantu menampilkan isi dan kondisi dari View, sekaligus menjadi tempat pengoperasian model kita. Hal ini berbeda dengan MVT yang menggunakan framework, atau MVC yang menggunakan Controller


TUGAS 2
1. Untuk POST, nama variabel atau value nya tidak ditampilkan di url serta tidak ada batas panjang value yang ingin diberikan. Untuk GET, nama variabel atau value akan ditampilkan di url serta batas panjang value yang akan diberikan adalah 255 karakter. POST juga men-support berbagai jenis data seperti String, Integer, Binary, dll, sedangkan GET hanya support String.
2.