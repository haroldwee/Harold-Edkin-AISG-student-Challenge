import splitfolders

splitfolders.ratio("{/Volumes.Edkin/images/subsample}", # The location of dataset
                   output="{/Volumes.Edkin/images/new}", # The output location
                   seed=42, # The number of seed
                   ratio=(.8, .2, 0), # The ratio of splited dataset
                   group_prefix=None, # If your dataset contains more than one file like ".jpg", ".pdf", etc
                   move=False # If you choose to move, turn this into True
                   )