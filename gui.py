
def get_index_rfc(list_colums):
    if "RFC" in list_colums or "R.F.C." in list_colums:
        for c,i in enumerate(list_colums):
            if "RFC" in i or "R.F.C." in i:
                return c+1
    else:
        print "no se encontro columna RFC o R.F.C."
        return None


def get_rfcs(filepath):
    fileopen = open(filepath)

    lines = fileopen.readlines()
    list_colums = lines[0].split(",")
    datas = lines[1:]

    index_rfc = get_index_rfc(list_colums)
    if index_rfc:
        print "No se encontro RFC o R.F.C."
        sys.exit()

    return  [row.split(",")[index_rfc] for row in datas]

def genpdf(filepath):
    from code import run
    run(get_rfcs("archivo.csv"))

if __name__ == "__main__":
