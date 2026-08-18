import os 
def arrange_files(files,ext):
    files_with_ext=[file for file in files if file.endswith(ext)]
    print(files_with_ext)

    for i,file in enumerate(files_with_ext):
          os.rename(file,f"iamges/photo.{i+1}{ext}")

if __name__=="__main__":
    files=os.listdir()
    arrange_files(files,".pdf")
