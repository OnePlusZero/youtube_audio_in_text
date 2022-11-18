# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import emoji 


# Создаем модель. 


# функция для расчепления аудио на чанки - части. 
# и применения распознавания аудио
def get_large_audio_transcription(path,):
    """
        разрываем на чанки большие аудио
    """
    r = sr.Recognizer()
    # открываем аудио используя pydub
    sound = AudioSegment.from_wav(path)  
    # Спилитим аудио где тишь больше 700 милисекунд
    chunks = split_on_silence(sound,
        # єксперементируем с аудио
        min_silence_len = 500,
        # найстройка под
        silence_thresh = sound.dBFS-14,
        # задержка после каждого слова 1 секунду для лучшего распознавания
        keep_silence=500,
    )
    folder_name = "temporary-files"
    # Создаем папку под каждый чанк
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # обрабатываем каждый чанк 
    for i, audio_chunk in enumerate(chunks, start=1):
        # экспортируем чанки и сохранаяем
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # распознаем
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # пробуем 
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print(emoji.emojize("Увы но несколько слов не распознано :pensive_face:"), str(e))
            else:
                text = f"{text.capitalize()}. "
                whole_text += text
    #возвращаем текстом все чанки переработанніе
    return whole_text

def start():
 #   lol = str(input("Введите название файла для переработки. Предварительно кинув его в папку с программой \n Или перетащите в консоль и нажмите enter:  \n "))
    path = "output.wav"
    file = open("static/txt/text.txt", "w")
    file.write("\nFull text: {}".format(get_large_audio_transcription(path)))
    file.close()

    

