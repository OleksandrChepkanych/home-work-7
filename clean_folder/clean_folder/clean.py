import sys, os, shutil

def transliterate(name):
    """Заміна символів по алфавітному вказівнику"""
    slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'y','й':'y','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
      'Ж':'ZH','З':'Z','И':'Y','Й':'Y','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA',',':'_','?':'_',' ':'_','~':'_','!':'_','@':'_','#':'_',
      '$':'_','%':'_','^':'_','&':'_','*':'_','(':'_',')':'_','-':'_','=':'_','+':'_',
      ':':'_',';':'_','<':'_','>':'_','\'':'_','"':'_','\\':'_','/':'_','№':'_',
      '[':'_',']':'_','{':'_','}':'_','ґ':'g','ї':'yi', 'є':'ye','Ґ':'G','Ї':'yi',
      'Є':'Ye', '—':'_'}
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name

def del_empty_dirs(catalog):
    """Функція для видалення пустих папок"""
    for d in os.listdir(catalog):
        a = os.path.join(catalog, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)

def normalize(catalog):
    """Основна функція, що проводить перебір папок, створює категорійні, та переносить туди необхідні файли."""
    find_files = []
    for root, dirs, files in os.walk(catalog):
        for file in files:
            # Перебір
            if file[-5::].lower() == '.jpeg' or file[-4::].lower() == '.png' or file[-4::].lower() == '.jpg' or file[-4::].lower() == '.svg':
                os.makedirs(catalog + '/' + 'images', exist_ok=True)
                os.rename(root.replace('\\', '/') + '/' + file, catalog + '/' + 'images' + '/' + transliterate(file))
            elif file[-4::].lower() == '.avi' or file[-4::].lower() == '.mp4' or file[-4::].lower() == '.mov' or file[-4::].lower() == '.mkv':
                os.makedirs(catalog + '/' + 'video', exist_ok=True)
                os.rename(root.replace('\\', '/') + '/' + file, catalog + '/' + 'video' + '/' + transliterate(file))
            elif file[-4::].lower() == '.doc' or file[-5::].lower() == '.docx' or file[-4::].lower() == '.txt' or file[-4::].lower() == '.pdf' or file[-5::].lower() == '.xlsx' or file[-5::].lower() == '.pptx':
                os.makedirs(catalog + '/' + 'documents', exist_ok=True)
                os.rename(root.replace('\\', '/') + '/' + file, catalog + '/' + 'documents' + '/' + transliterate(file))
            elif file[-4::].lower() == '.mp3' or file[-4::].lower() == '.ogg' or file[-4::].lower() == '.wav' or file[-4::].lower() == '.anr':
                os.makedirs(catalog + '/' + 'audio', exist_ok=True)
                os.rename(root.replace('\\', '/') + '/' + file, catalog + '/' + 'audio' + '/' + transliterate(file))
            elif file[-4::].lower() == '.zip' or file[-3::].lower() == '.gz' or file[-4::].lower() == '.tar':
                # Із архівом ми додатково проводим розпакування та видалення файлу архіва
                os.makedirs(catalog + '/' + 'archives', exist_ok=True)
                os.rename(root.replace('\\', '/') + '/' + file, catalog + '/' + 'archives' + '/' + transliterate(file))
                shutil.unpack_archive(catalog + '/' + 'archives' + '/' + transliterate(file), catalog + '/' + 'archives' + '/' + transliterate(file[:-4]) + '/')
                os.remove(catalog + '/' + 'archives' + '/' + transliterate(file))
    # Видаляєм пусті папки
    del_empty_dirs(catalog)

def not_nul():
    # Перевірка на ввід параметра шляху до папки(існування значення)
    if len(sys.argv) > 1:
        catalog = sys.argv[1]
        return catalog
    
if __name__ == '__main__':
    normalize(not_nul()) if not_nul() else print('Шлях не введено')