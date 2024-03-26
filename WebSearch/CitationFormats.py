__Program__     = "CitationFormats"    
__programer__   = "Themadhood Pequot"
__Date__        = "3/26/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""   

import Error



def FormatWithAll():
    Error.Log(f"Citation with all formats","Log.txt")
    st = Error.time.time()
    retar = dict()
    try:
        for Format in __formats:
            formated = formatsdict[Format]()
            retar.update([Format:formated])

    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"class","MLA",
                                f"mesage",e],"Functions")
    Error.Log(f"Citation with all formats Total Runtime: {Error.LenTime(st)}",
              "Log.txt")
    return retar


__RemoveFormats = dir()
__RemoveFormats.append("__RemoveFormats")

#########################################################################
#########################################################################
#########################################################################

def MLA():
    try:
        pass

    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"class","MLA",
                                f"mesage",e],"Functions")

def APA():
    try:
        pass

    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"class","APA",
                                f"mesage",e],"Functions")







#########################################################################
#########################################################################
#########################################################################
        
#run on init of modual so only needs to run onece
__formats = dir()
while __RemoveFormats > []:
    remove = __RemoveFormats.pop()
    __formats.remove(remove)


__formatsdict = vars()

if __name__ == "__main__":
    print(__formats)
















