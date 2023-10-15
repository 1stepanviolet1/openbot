from var import CREATE_ACT_FLAG, _CONST


TOKEN: _CONST = "6262186295:AAFp6dOoOCbvAx1Is6jeyhjCGhJRAPBb4Ls"


DATA_DELETE_FILE: _CONST = "delete_document"

DATA_TRANS_EN_RU: _CONST = "SEND_EN_RU"
DATA_TRANS_RU_EN: _CONST = "SEND_RU_EN"
DATA_TRANS: set = {DATA_TRANS_EN_RU, DATA_TRANS_RU_EN}

LIST_OF_UNKNOWN_CONTENT_TYPES: set = {
    'audio', 'document', 'photo', 
    'sticker', 'video', 'video_note', 
    'voice', 'location', 'contact' 
}


ACT_FLAG: CREATE_ACT_FLAG = CREATE_ACT_FLAG()

NONE: _CONST = "None"

FLAG_TRANS_EN_RU: _CONST = "EN-RU"
FLAG_TRANS_RU_EN: _CONST = "RU-EN"
