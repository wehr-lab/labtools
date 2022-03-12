"""
Functions to load and save ScanImage data
"""
import typing
from pathlib import Path
import json
import pdb

import numpy as np
from skvideo.io import FFmpegWriter
from ScanImageTiffReader import ScanImageTiffReader as TiffReader
from tqdm import tqdm

def bigtiff_nframes(path: typing.Union[Path, TiffReader]) -> int:
    """
    Check the number of frames in a bigtiff
    """
    if isinstance(path, (Path, str)):
        path = Path(path).resolve()
        reader = TiffReader(str(path))
    elif isinstance(path, TiffReader):
        reader = path
    else:
        raise ValueError('Need to be given a path or an open tiffreader')

    shape = reader.shape()
    if len(shape) == 2:
        nframes = 1
    else:
        nframes = shape[2]

    return nframes

def iter_bigtiff(
    path: Path=None, 
    batch_size:int=1,
    reader: typing.Optional[TiffReader] = None,
    start_frame:int = 0,
    end_frame: typing.Optional[int] = None):
    """
    Iterate through frames in a BigTiff file

    Examples:

        for frame in iter_bigtiff(path):
            # do something with the frame

    Arguments:
        path (pathlib.Path): Path to input tiff
        batch_size (int): Number of images to yield at once
        reader (ScanImageTiffReader): Optional - an already-opened
            TiffReader. Either path or reader needs to be passed
    """
    if reader is not None:
        assert isinstance(reader, TiffReader)
    elif path is not None:
        path = Path(path).resolve()
        reader = TiffReader(str(path))
    else:
        raise ValueError('Need to pass either a path or an open reader')

    nframes = bigtiff_nframes(reader)

    current_frame = start_frame

    if end_frame is None:
        end_frame = nframes

    while current_frame < end_frame:

        yield reader.data(
            beg=current_frame, 
            end=np.clip(current_frame + batch_size, 0, end_frame)
        )
        current_frame += batch_size




def bigtiff_to_video(
    path: Path, 
    output:typing.Optional[Path]=None,
    ops: typing.Optional[Path] = None,
    start_frame:int = 0,
    end_frame: typing.Optional[int] = None,
    source_fps: int = 30,
    output_fps: int = 30,
    codec: str = 'libx264',
    pix_fmt: str = 'yuv420p',
    input_kwargs: typing.Optional[dict] = None,
    output_kwargs: typing.Optional[dict] = None,
    verbosity: int = 1,
    brightness: float = 1,
    dfof_kwargs: typing.Optional[dict] = None
    ) -> Path:
    """
    Convert a bigtiff to a video file using scikit-image.

    Arguments:
        path (Path): Input bigtiff path
        output (Path): Optional, output video path. If None,
            then just replace extension with `.mp4`
        ops (Path): Ops file. if None, try to get ``<path>_ops.json``
        start_frame (int): Frame of input to start on
        end_frame (int): Frame of input to end output video
        source_fps (int): fps of source video
        output_fps (int): fps to convert output video to
        codec (str): video codec!
        pix_fmt (str): pixel format (default ``yuv420p``)
        input_kwargs: Passed to :class:`skvideo.io.FFMpegWriter`
        output_kwargs: Passed to :class:`skvideo.io.FFMpegWriter`
        brightness (float): adjust brightness (linearly, by multiplication lmao)
        dfof_kwargs (dict): if not None, a dictionary passed to :func:`.dfof`

    Returns:
        Path of encoded video

    References:
        https://github.com/MouseLand/suite2p/blob/main/suite2p/io/tiff.py
    """

    in_kwargs = {
        '-r': str(source_fps)
    }

    out_kwargs = {
        '-r': str(output_fps),
        '-vcodec': codec,
        '-pix_fmt': pix_fmt
    }

    if isinstance(input_kwargs, dict):
        in_kwargs.update(input_kwargs)

    if isinstance(output_kwargs, dict):
        out_kwargs.update(output_kwargs)



    path = Path(path).resolve()

    if output is None:
        output = path.with_suffix('.mp4')

    if ops is None:
        ops = Path(path.parent / (path.stem + '_ops')).with_suffix('.json')

    with open(ops, 'r') as ofile:
        ops = json.load(ofile)


    reader = TiffReader(str(path))
    nframes = bigtiff_nframes(reader)

    if dfof_kwargs is not None:
        dfof_arr = dfof(reader, **dfof_kwargs)
        dfof_arr -= np.min(dfof_arr)
        dfof_arr += 1

    else:
        dfof_arr = None

    if end_frame is None:
        end_frame = nframes

    if verbosity > 0:
        print(f'Input: {path}')
        print(f'Output: {output}')
        print(f'Writing n frames: {nframes}')

    writer = FFmpegWriter(str(output),
        inputdict = in_kwargs,
        outputdict = out_kwargs,
        verbosity = verbosity
    )

    try:
        for frame in tqdm(iter_bigtiff(
            reader=reader, 
            start_frame=start_frame,
            end_frame=end_frame), 
        total=end_frame-start_frame):
            

            if dfof_arr is not None:
                frame = ((frame-dfof_arr)+1)/(dfof_arr)
                frame[np.isnan(frame)] = 0

            else:
                # reduce to 8-bit
                frame = frame.astype(np.float64)
                frame *= (2**8)/(2**16)

            frame = (frame-np.min(frame))*brightness

            frame = restack_bigtiff(frame, ops)

            writer.writeFrame(frame)
    finally:
        writer.close()

    return output

def gamma_correct(frame:np.ndarray, gamma:float=1):
    """8-bit gamma"""
    frame = ((frame/255) ** (1/gamma))*255
    frame = np.round(frame).astype(np.uint8)
    return frame


def minmax(frame, max_=255):
    return (frame-np.min(frame))/(np.max(frame)-np.min(frame))*max_


def iterative_median(
    reader:TiffReader,
    batch_size:int=10) -> np.ndarray:
    """
    Find the median of a big huge video by taking the med
    """
    medians = []
    for chunk in iter_bigtiff(reader=reader, batch_size=batch_size):
        medians.append(np.median(chunk, axis=0))

    med = np.median(np.stack(medians, axis=0), axis=0)
    med[med == 0] = 0.001
    pdb.set_trace()
    return med



def dfof(
    input:TiffReader,
    method:typing.Literal['median','mean']='median',
    iterative=False,
    **kwargs) -> np.ndarray:
    """
    Calculate the median of each frame of a video 
    """

    if iterative:
        if method == 'median':
            out_arr = iterative_median(input, **kwargs)
        elif method == 'mean':
            raise NotImplementedError('Havent done this yet, gotta load into memory!')
    else:
        raise NotImplementedError('Havent done this yet!')

    return out_arr




def restack_bigtiff(frame:np.ndarray, ops:dict) -> np.ndarray:
    """
    bigtiffs are usually just huge vertical strips.

    Use the ops file to unstack them into normal frames.

    .. note::

        This is just an approximation for the sake of making a video, don't use this for analysis!

    References:
        https://github.com/MouseLand/suite2p/blob/main/suite2p/io/tiff.py
    """

    if ops['nplanes']>1:
        raise NotImplementedError('suite2p does some incomprehensible stuff and im just trying to get data real quick!')

    height = len(ops['lines'][0])



    # height = np.floor(frame.shape[1]/ops['nrois']).astype(int)
    if height % 2 > 0:
        height -= 1

    out_arr = np.zeros((1, height, frame.shape[2]*ops['nrois']), dtype=frame.dtype)
    for i in range(ops['nrois']):
        out_arr[0,:,i*frame.shape[2]:(i+1)*frame.shape[2]] = frame[0, ops['lines'][i], :]

    #     out_arr[0,:,i*frame.shape[2]:(i+1)*frame.shape[2]] = frame[0,i*height:(i+1)*height, :]
    return out_arr



