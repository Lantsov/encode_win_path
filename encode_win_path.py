# при распаковке архива пути и названия файлов с кириллицей ломается кодировка

def repair_path_coding(path=''):
    path = path.split(sep='/')
    path[-1] = path[-1].encode('cp437').decode('cp866')
    return '/'.join(path)


path = 'путь/еще путь/название с пробелами/¡áºóá¡¿Ñ ß »α«íÑ½á¼¿.vbs'
print(path, repair_path_coding(path), sep='\n')
