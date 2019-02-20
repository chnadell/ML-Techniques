import os

def gridGen(data_dir, grid_dir):

    # get data to be read
    file_paths = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".csv")]

    # define output file
    outFile = os.path.join(grid_dir, 'gridDataOut.txt')

    # load TF model


    with open(os.path.join(grid_dir, 'gridFile.csv'), 'w+') as gridFile:
        for file_path in file_paths:
            print('file path is {}'.format(file_path))
            with open(file_path) as file:
                for line in file:
                    # extract just the geometric parameters
                    lineSplit = line.split(',')
                    geom = [float(el) for el in lineSplit[2:10]]


                    gridFile.write(",".join(geom) + '\n')






if __name__=="__main__":
    gridGen(os.path.join('.','dataIn','eval'), os.path.join('.', 'dataGrid'))
