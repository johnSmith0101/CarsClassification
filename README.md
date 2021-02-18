**CarsClassification**  
Проект по распознованию марки, модели и цвета автомобиля на фото.  
Общая структура проекта:  
Полученная фотография передается в Yolo v3, предобученном на coco датасете. Модель решает задачу object detect'a, находит автомобили и возвращает bbox'ы. По координатам bbox'ов каждый автомобиль вырезается с фото.  
Каждое фото передается в обученный resnet101 на stanfordcar dataset.  
Для определения цвета на фото отключаются все пиксели, которые не попадают под range определенного цвета, затем считается суммарное количество оставшихся и выберается конкретный цвет. (проще на код посмотреть, чем объяснить)  
Графики процесса обучения, а так же само обучение доступно в ноутбуке в репозитории.   
Для работы модели в любом другом проекте необходимо: импортировать метод predict_car из файла car_classifier.py и передать ему путь до картинки в формате .jpg и путь до .pt файла с настройками для модели.   
Метод вернет марку, модель и год выпуска автомобиля.  
В ближайшее время будет добавлено:  
- [x] Распознование сразу нескольких автомобилей на одном фото.  
- [ ] Определение цвета авто. 

![proofs](https://github.com/johnSmith0101/CarsClassification/blob/main/it_works_yes.jpg)
