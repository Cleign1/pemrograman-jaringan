# Welcome

Selamat datang di repositori untuk Lab Pemrograman Jaringan

Repositori ini menggunakan Conda untuk mengelola dependensi. Anda dapat membuat environment baru dengan perintah berikut:

## Instalasi dengan Conda

jika conda terinstall di pc anda, silahkan jalankan perintah berikut di terminal atau command prompt:

```bash
conda create -n "pemjar" python=3.11.4 ipython
```

Aktivasi environment conda tersebut:

```bash
conda activate pemjar
```

Setelah itu, install semua dependensi yang ada di file `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Instalasi dengan Python-venv

atau gunakan python env, secara normal dengan cara:

```bash
python -m venv pemjar
```

Aktivasi environment tersebut:

```bash
venv pemjar\Scripts\activate
```

Setelah itu, install semua dependensi yang ada di file `requirements.txt`:

```bash
pip install -r requirements.txt
```

Jika sudah dilaksanakan langkah diatas, environment sudah siap digunakan!
