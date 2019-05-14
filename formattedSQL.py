# Gib mir alle Männer
def SQLStatement(StringA, StringB, StringD):
    SQL1 = f'select * from {StringA} where {StringB}={StringD}'
    return SQL1

# Join mit 2 where-Bedingungen
def SQLJoin(String1, String2, String3, String4, String5, String6, String7):
    SQL1 = f'select * from {String1} ' \
        f'join {String2} on {String1}.{String3}= {String2}.{String3}' \
        f' where {String4}={String5} and {String6}={String7}'
    return SQL1


def SQLBack(String1, String2, String3, String4, String5, String6, String7, String8):
    SQL1 = f'select {String6}.{String1} from {String2} ' \
        f'join {String3} on {String3}.{String4} = {String2}.{String5} ' \
        f'join {String6} on {String2}.{String1} = {String6}.{String1} ' \
        f'where {String3}.{String7} like \'{String8 + "%%"}\''
    return SQL1
