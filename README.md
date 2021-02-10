**CarsClassification**  
resnet101, обученный на stanford cars dataset с замененной линейной функцией. Распознает 197 моделей автомобилей разных марок и годов выпуска.  Для интеграции в любой проект:  
1. Обучите модель, запустив notebook 'carsClassifierModel.ipynb', заменив пути до датасета. 
2. Импортируйте метод predict_car из файла car_classifier.py (from car_classifier import predict_car). Вызовите метод, передав ему путь до картинки и чекпоинта модели, который сохранился во время обучения.  
dataset: https://www.kaggle.com/jutrera/stanford-car-dataset-by-classes-folder
