from os.path import abspath, join

proj_dir = abspath(__file__ + "/../../..")
data_dir = join(proj_dir, "data")
data_loc = join(data_dir, "global_emissions.csv")
docs_dir = join(proj_dir, "docs")
yearwise_loc = join(data_dir, "yearwise_sums.csv")
