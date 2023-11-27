import os
class PreprocessData:
    def get_id_to_text(self, ):
        id_to_text = {}
        all_files = os.listdir("datasets")
        txt_files = filter(lambda x: x[-4:] == '.txt', all_files)
        for txt_file in txt_files:
            txt_file_wav = txt_file.replace(".txt",".wav")
            file_content = self.read_first_line(f"datasets\{txt_file}")
            id_to_text[txt_file_wav] = file_content
        return id_to_text    
    def read_first_line(self,file):
        with open(file, 'rt', encoding='utf-8') as fd:
            first_line = fd.readline()
            return first_line