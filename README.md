**CarsClassification**  
Обученная нейронная сеть, распознающая 197 моделей автомобилей разных марок и годов выпуска. Для работы модели в любом проекте написан скрипт.   
В основе лежит предобученный resnet101, в котором были заменены некоторые слои. 
Графики процесса обучения, а так же само обучение доступно в ноутбуке в репозитории. 
Для работы модели в любом другом проекте необходимо: импортировать метод predict_car из файла carsClassificarion.py и передать ему путь до картинки в формате .jpg и путь до .pt файла с настройками для модели. Метод вернет марку, модель и год выпуска автомобиля.
