import pickle

input_file="e:\\TestData\\flower.png"
pickle_file="e:\\TestData\\flower_pickle.pickle"
# output_file="e:\\TestData\\flower_new.png"

with open(input_file, "rb") as ifile:
    content=ifile.read()
    with open(pickle_file, "wb") as pfile:
        pickle.dump(content,pfile)

# with open(pickle_file, "rb") as pfile:
#     content=pickle.load(pfile)
#     with open(output_file, "wb") as ofile:
#         ofile.write(content)
