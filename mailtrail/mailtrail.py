import time, json, os
import pendulum
import schedule
#from .graphconnector import GraphConnector
from .config import Config
from pyews import UserConfiguration, GetSearchableMailboxes, SearchMailboxes


class MailTrail:

    config = Config()
    __user_config = None
    __mailbox_list = []
    __messages = []
    
    def run(self):
        print(self.__get_user_configuration(), flush=True)
        self.__search_mailboxes()
        if self.__messages:
            self.__write_json(self.__messages)
        else:
            print('No messages', flush=True)
        schedule.every(self.config.CHECK_DURATION).hours.do(self.__search_mailboxes)
        while True:
            schedule.run_pending()
            time.sleep(10)
            if self.__messages:
                self.__write_json(self.__messages)

    def __write_json(self, messages):
        with open(os.path.abspath(self.config.STORAGE_PATH), 'w+') as file:
            return_dict = {}
            return_dict['timestamp'] = pendulum.now().to_iso8601_string
            for message in messages:
                if message.get('Subject') and message.get('Subject') not in return_dict:
                    return_dict[message['Subject']] = message
            json.dump(return_dict, file)
            print(message, flush=True)
        self.__messages = None

    def __search_mailboxes(self):
        # + ' AND Received:today AND Sent:today'
        for search in SearchMailboxes(
            self.config.QUERY, 
            self.__get_user_configuration(), 
            self.__get_searchable_mailboxes()
        ).response:
            self.__messages.append(search)

    def __get_searchable_mailboxes(self):
        if not self.__mailbox_list:
            for mailbox in GetSearchableMailboxes(self.__user_config).response:
                self.__mailbox_list.append(mailbox['ReferenceId'])
        return self.__mailbox_list

    def __get_user_configuration(self):
        if not self.__user_config:
            self.__user_config = UserConfiguration(
                self.config.USERNAME, 
                self.config.PASSWORD
            )
        return self.__user_config
