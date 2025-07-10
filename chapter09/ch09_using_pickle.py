import pickle

# PICKLING AND UNPICKLING DEMO IN THE SAME FILE

input_file="e:\\TestData\\flower.png"
output_file="e:\\TestData\\flower_new.png"
pickle_file="e:\\TestData\\flower_pickle.pickle"

with open(input_file, "rb") as ifile:
    content=ifile.read()
    with open(pickle_file, "wb") as pfile:
        pickle.dump(content,pfile)

with open(pickle_file, "rb") as pfile:
    content=pickle.load(pfile)
    with open(output_file, "wb") as ofile:
        ofile.write(content)