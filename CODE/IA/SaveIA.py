import os.path

from UTIL.Path import rootpath


def saveIA(etat, levelname):
    
    savelines = []
    while etat.parent:
        savelines.append("{}\n".format(etat.dir))
        etat = etat.parent
    savelines.reverse()

    savepath = os.path.join(rootpath(), "IA_solutions", levelname)
    print("saving solution in {}...".format(savepath))

    file = open(savepath, 'w')
    file.writelines(savelines)        
    file.close()
    
    print("saved solution in: " + savepath)