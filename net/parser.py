# parser.py
# Created On 2021-02-04, by dev. Coffee Official
# For more information or to contact, please email to this address: official.devcoffee@gmail.com

import json

class MessageData(dict):
    def toJson(self):
        return json.dumps(self, indent = 4)

class MessageParser():

    Data = MessageData()

    def FormatAsTextMsg(self, sender_address, message):
        self.Data['Status'] = 'Text'
        self.Data['Sender_Address'] = sender_address
        self.Data['Message'] = message
        return self.Data
    
    def FormatAsWhisperMsg(self, sender_address, reciever_address, message):
        self.Data['Status'] = 'Whisper'
        self.Data['Sender_Address'] = sender_address
        self.Data['Reciever_Address'] = reciever_address
        self.Data['Message'] = message
        return self.Data

    def FormatAsFileMsg(self, sender_address, file_data):
        self.Data['Status'] = 'File'
        self.Data['Sender_Address'] = sender_address
        self.Data['File_Data'] = file_data
        return self.Data
    
    def FormatAsEmojiMsg(self, sender_address, emoji_data):
        self.Data['Status'] = 'Emoji'
        self.Data['Sender_Address'] = sender_address
        self.Data['Emoji_Data'] = emoji_data
        return self.Data

    def FormatAsEventMsg(self, sender_address, event_type, data):
        self.Data['Status'] = 'Event'
        self.Data['Sender_Address'] = sender_address
        self.Data['Event_Type'] = event_type
        self.Data['Data'] = data
        return self.Data

    def DecodeJson(self, jsonObject):
        self.Data = json.loads(jsonObject)
        return self.Data
    pass

class ChatEvent():
    LOG_IN_REQUEST = 'LIR'
    USER_LIST = 'URL'
    NAME_CHANGE_REQUEST = 'NCR'
    LOG_OUT_REQUEST = 'LOR'
    FILE_UPLOAD_REQUEST = 'FUR'
    FILE_READY = 'FRD'
    FILE_DOWNLOAD_REQUEST = 'FDR'
    FILE_TRANSMISSION_START = 'FTS'
    FILE_TRANSMISSION = 'FTM'
    FILE_TRANSMISSION_END = 'FTE'
    FILE_TRANSMISSION_CANCEL = 'FTC'
    EMOJI = 'EMJ'
    CONNETCION_CANCEL = 'CNC'
    NOTICE = 'NTC'
    pass

'''
if __name__ == '__main__':
    messageParser = MessageParser()
    msg = messageParser.FormatAsTextMsg('192.0.0.1', 'Test').toJson()
    print(msg)
    print(messageParser.DecodeJson(msg))
    pass
'''