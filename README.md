Lab13 – Зам олох алгоритмууд (Temporal Paths)

Зорилго:
Lab13-ийн зорилго нь динамик сүлжээ (temporal network) дотор зам олох таван төрлийн стратегийг хэрэгжүүлэх явдал юм. Эдгээр зам олох аргууд нь сүлжээн дэх холболтуудын цаг хугацааны шинж чанарыг харгалзан үздэг.

Хэрэгжүүлсэн зам олох аргууд:

1. Shortest Path – Узелүүдийн хамгийн богино зам
2. Fastest Path – Цаг хугацааны хувьд хамгийн хурдан зам
3. Foremost Path – Эхний ирэлттэй зам (хамгийн эрт хүрдэг)
4. Fastest Shortest Path – Хамгийн богино зам дундаас хамгийн хурдан нь
5. Shortest Fastest Path – Хамгийн хурдан зам дундаас хамгийн богино нь

Файлын бүтэц:
Lab13/
├── scripts/
│ └── temporal_paths.py # Зам олох функцуудыг агуулсан Python скрипт
├── notebooks/
│ └── 05-temporal-paths-example.ipynb # Хэрэглээний жишээ бүхий notebook
└── README.md # Тайлбар, заавар

Хэрэглэсэн технологиуд:

- Python 3
- NetworkX
- Matplotlib
- Jupyter Notebook

Хэрхэн ажиллуулах вэ:

1. Орчин бэлтгэх:
   pip install networkx matplotlib notebook

2. Notebook ажиллуулах:
   jupyter notebook notebooks/05-temporal-paths-example.ipynb

3. Замуудыг турших:
   Жишээ граф ашиглан 5 төрлийн замын үр дүнг харна.
   Хэрвээ хүсвэл edges жагсаалтыг өөрчилж шинэ граф туршиж болно.

Жишээ гаралт:
Shortest path: [1, 3, 5]
Fastest path: [1, 2, 3, 4, 5]
Foremost path: [1, 3, 5]
Fastest Shortest path: [1, 3, 5]
Shortest Fastest path: [1, 3, 5]

Боловсруулсан:
Temuulen – МУИС, Компьютерын ухаан, 3-р курс
Dynamic Network Analysis & Algorithms
