import json
import os
import pandas as pd
from typing import Union
from datetime import datetime


def clean_messages(messages: dict) -> pd.DataFrame:
    """
    Clean the raw json messages from a slack export

    Args:
        messages (dict): dictionary of {'channel': [messages]} from :func:`.load_messages`

    Returns:
        :class:`pandas.DataFrame` : cleaned dataframe of messages
    """

    clean_messages = []

    # iter through each channel and its list of messages

    for channel, channel_messages in messages.items():
        for message in channel_messages:

            # some message types don't have usernames attached for some reason
            try:
                display_name = message['user_profile']['display_name']
                real_name    = message['user_profile']['real_name']
            except KeyError:
                display_name = None
                real_name = None

            # simplify the message
            message_simple = {
                'channel': channel,
                'timestamp': datetime.fromtimestamp(float(message['ts'])),
                'display_name':display_name,
                'real_name': real_name,
                'text': message['text']
            }


            clean_messages.append(message_simple)

    # create dataframe and return
    return pd.DataFrame(clean_messages)


def load_messages(base_dir: str, clean : bool = True) -> Union[dict, pd.DataFrame]:
    """
    Load slack .json messages from an export

    Arguments:
        base_dir (str): base directory of slack export
        clean (bool): if True (default), also :func:`.clean_messages` before returning

    Returns:
        (dict, :class:`pd.DataFrame`): dict of {'channel': [messages]}
    """

    messages = {}

    for subdir in os.listdir(base_dir):
        # iterate through folders in base directory
        subdir_complete = os.path.join(base_dir, subdir)
        if os.path.isdir(subdir_complete):
            # a folder contains .json files of messages for each day
            # create a list of messages for a subdirectory (channel)
            messages[subdir] = []
            for json_file in os.listdir(subdir_complete):
                if json_file.endswith('.json'):
                    with open(os.path.join(base_dir, subdir, json_file), 'r') as jfile:
                        json_messages = json.load(jfile)

                    messages[subdir].extend(json_messages)

    if clean:
        messages = clean_messages(messages)

    return messages