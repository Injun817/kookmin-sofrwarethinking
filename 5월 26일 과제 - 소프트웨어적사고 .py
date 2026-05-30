import os

def get_file_list(dir_path):
    file_list = []
    
    with os.scandir(dir_path) as it:
        for entry in it:
            if entry.is_file():  
                name = entry.name
                size = entry.stat().st_size 
                full_path = entry.path 
                
                file_list.append([name, size, full_path])
                
    return file_list

def compare_directories():
    dir1 = input("첫 번째 디렉토리: ")
    dir2 = input("두 번째 디렉토리: ")
    
    if not os.path.exists(dir1) or not os.path.exists(dir2):
        print("입력한 디렉토리 중 존재하지 않는 항목이 있음.")
        return

    list1 = get_file_list(dir1)
    list2 = get_file_list(dir2)

    if len(list1) != len(list2):
        print("파일 수가 다릅니다.")
        return


    for item1 in list1:
        filename = item1[0]
        filesize = item1[1]
        path1 = item1[2]

        path2 = None
        
        for item2 in list2:
            if item2[0] == filename and item2[1] == filesize:
                path2 = item2[2]
                break

        if path2 is None:
            print("파일이 상대 디렉토리에 없습니다.")
            return
        
        with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
            if f1.read() != f2.read():
                print("파일의 내용이 서로 다릅니다.")
                return

    print("일치합니다.")

if __name__ == "__main__":
    compare_directories()