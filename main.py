from deepface import DeepFace
import json

def face_analyze(): #функция для анализа лиц
    try: 
        result_dict = DeepFace.analyze(img_path='1.jpg', actions=['age','emotion','gender', 'race'], enforce_detection=False) #анализируем картинку по признакам возраст, эмоции и т.д чел ты же умеешь читать на инглише камон

        with open('face_analyze.json', 'w') as file: # полученные данные записываем в жисон
            json.dump(result_dict, file, indent=4, ensure_ascii=False)
        
        return result_dict

    except Exception as _ex:
        return _ex

def main():
    print(face_analyze())

if __name__ == '__main__':
    main()
