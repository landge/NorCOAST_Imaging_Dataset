'''Read imaging data in Imaging_data directory and create a csv file with the following columns:
subject-id, session-id, modality, file-name, file-path
'''

'''Import pandas and pathlib modules'''
import pandas as pd
from pathlib import Path

data_directory = Path('../the_complete_NorCOAST_dataset')

'''Create a list of all the imaging data files'''
def read_imaging_data(directory):
    imaging_data = [f for f in Path(directory).glob('**/*') if f.is_file()]
    return imaging_data

def check_term_in_modality(term):
    if 'SWAN' in term:
        return 'SWI'
    elif 'MRI-T1' in term:
        return 'T1'
    else:
        return term

def make_order(term):
    match term:
        case 'CT-1':
            return 1
        case 'CT-2':
            return 2
        case  'CTA':
            return 3
        case 'DWI':
            return 4
        case 'ADC':
            return 5
        case '3D-FLAIR':
            return 6
        case '3D-T1':
            return 7
        case 'SWI':
            return 8
        case 'T1':
            return 9
        case 'T2':
            return 10
        case 'T2-FLAIR':
            return 11
        case 'MRA':
            return 12
        
def create_columns_from_path(imaging_data):
    '''Create a list of subject ids, session ids, modalities, file names and file paths'''
    subject_ids = []
    session_ids = []
    modalities = []
    file_names = []
    file_paths = []
    examinations = []
    order = []

    for f in imaging_data:
        if len(f.parts) >=4:
            subject_ids.append(f.parts[2])
            session_ids.append(f.parts[3])
            file_paths.append(str(f))
            examinations.append(f.name.split('.')[0].split('_')[-1])
            if not '-MR' in f.parts[3]:
                mod = check_term_in_modality(f.parts[4])
                order.append(make_order(mod))
                modalities.append(mod)
                file_names.append(f.parts[5].split('.')[0])
            else:
                mod = check_term_in_modality(f.name.split('.')[0].split('_')[-1])
                order.append(make_order(mod))
                modalities.append(mod)
                file_names.append(f.parts[5].split('.')[0])



    return subject_ids, session_ids, modalities, file_names, file_paths, examinations, order

'''Create a dataframe with the columns subject-id, session-id, modality, file-name, file-path'''
def create_dataframe(subject_ids, session_ids, modalities, file_names, file_paths, examinations, order):
    df = pd.DataFrame({'subject-id': subject_ids, 'timepoint': session_ids, 'modality': modalities, 'file-name': file_names, 'file-path': file_paths, 'examintaion': examinations, 'order': order})
    return df

'''Run the functions and save the dataframe as a csv file'''
def main():
    imaging_data = read_imaging_data(data_directory)
    subject_ids, session_ids, modalities, file_names, file_paths, examinations, order = create_columns_from_path(imaging_data)
    df = create_dataframe(subject_ids, session_ids, modalities, file_names, file_paths, examinations, order)
    df.to_csv('imaging_data.csv', index=False)

'''Get image type from file name'''
def get_image_type(file_name):
    image_type = file_name.name.split('.')[0].split('_')[2:]
    print(image_type)

'''Add session to file name'''
def add_session_to_file_name(f):
    if len(f.parts) >= 4:
        if '_' in f.parts[3]: 
            print(f.as_posix())
            new_path = Path(f.parts[0], f.parts[1], f.parts[2], f.parts[3].replace('_','-'), f.parts[4], f.name)
            f.rename(new_path)
            print(new_path.as_posix())

'''Check if underscore in modality part of file name'''
def check_underscore_in_modality(file_name):
    if '_' in file_name.parts[3]:
        print(f'Still not correct {file_name.as_posix()} --> substitue with {file_name.name.split(".")[0].split("_")[-1]}') 


if __name__ == '__main__':
    main()
