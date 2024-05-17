import numpy as np 
import snpy

TEST_PATH = 'data\\CSP\\SN2005bl_snpy.txt'


def SNooPy_fit():
    # Load data
    s = snpy.get_sn(TEST_PATH)
    
    # Set model
    model = 'max_model'
    shapeParam = 'st'
    s.choose_model(model, stype=shapeParam)
    s.set_restbands() # Auto-sets appropriate rest bands

    # Set fit
    s.fit()

    # Summary
    s.summary()
    for param in s.paramaters:
        print("{} = {} +/- {}".format(param, s.parameters[param], s.errors[param]))

    return None

if __name__ == "__main__":
    
    SNooPy_fit()


