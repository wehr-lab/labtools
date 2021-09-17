import json
import os
import pandas as pd
from tqdm import tqdm
from typing import Union, Optional
from datetime import datetime
from pathlib import Path
import requests


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

            files = message.get('local_files', [])

            # simplify the message
            message_simple = {
                'channel': channel,
                'timestamp': datetime.fromtimestamp(float(message['ts'])),
                'display_name':display_name,
                'real_name': real_name,
                'files': files,
                'text': message['text']
            }

            clean_messages.append(message_simple)

    # create dataframe and return
    return pd.DataFrame(clean_messages)


def download_attachments(messages: dict, base_dir: Path, download_subdir: str = 'files') -> dict:
    """
    Download all linked attachments and save them in `download_subdir` beneath `base_dir`.

    Args:
        messages (dict): Dict of (uncleaned) messages from :func:`.load_messages`
        base_dir (:class:`pathlib.Path`): base directory, beneath which to save the files
        download_subdir (str): subdirectory beneath `base_dir` into which the files should be downloaded.

    Returns:
        dict: dict like input but with a list of local files
    """

    download_dir = Path(base_dir) / download_subdir
    if not download_dir.exists():
        download_dir.mkdir(parents=True)

    # count all messages
    n_messages = 0
    for msgs in messages.values():
        n_messages += len(msgs)

    msg_pbar = tqdm(total=n_messages, position=0)
    for channel, channel_messages in messages.items():
        for i, message in enumerate(channel_messages):
            local_files = []
            for file in message.get('files', []):
                if 'url_private_download' not in file.keys():
                    continue
                file_name = f"{file['id']}_{file['name']}"
                file_path = download_dir / file_name
                local_files.append(file_name)

                if file_path.exists():
                    # have already downloaded
                    continue

                # download that file as a stream!
                with requests.get(file['url_private_download'], stream=True) as req:
                    total_size_in_bytes = int(req.headers.get('content-length', 0))
                    block_size = 1024  # 1 Kibibyte
                    download_pbar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, position=1)
                    with open(file_path, 'wb') as open_file:
                        for data in req.iter_content(block_size):
                            download_pbar.update(len(data))
                            open_file.write(data)
                    download_pbar.close()

            if len(local_files)>0:
                messages[channel][i]['local_files'] = local_files

            msg_pbar.update()
    msg_pbar.close()
    return messages


def load_messages(base_dir: str, clean : bool = True, download : bool = True) -> Union[dict, pd.DataFrame]:
    """
    Load slack .json messages from an export, optionally cleaning and downloading attachments.

    Arguments:
        base_dir (str): base directory of slack export
        clean (bool): if True (default), also :func:`.clean_messages` before returning
        download (bool): if True (default), download attached files with :func:`.download_attachments`

    Returns:
        (dict, :class:`pandas.DataFrame`): dict of {'channel': [messages]}
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

    if download:
        messages = download_attachments(messages, Path(base_dir).resolve())

    if clean:
        messages = clean_messages(messages)

    return messages


