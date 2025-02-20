from ZipPackager.FileManager import FileManager
from ImgComparer.ImageReader import ImageReader

if __name__ == "__main__":
    img_reader = ImageReader()
    img_reader.execute()
    if len(img_reader.similarity_list) != 0:
        print("\nfind similarit!!!\n")
        for i in img_reader.similarity_list:
            print(i)
    if len(img_reader.relevance_list) != 0:
        print("\nfind relevance!!!\n")
        for i in img_reader.relevance_list:
            print(i)
    """
    file_manager = FileManager()
    file_manager.multi_compress_file()
    print("finished whole process")
    """
