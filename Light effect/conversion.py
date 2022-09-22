group = [{'name': weight_name, 'data': np.ndarray}, ...]   # 1 *.bin file


pip install tensorflowjs


from typing import Dict, ByteString
import torch
from tensorflowjs.read_weights import decode_weights
from tensorflowjs.write_weights import write_weights

def convert2tensor(weights: ByteString, model: Dict) -> Dict[str, torch.Tensor]:
    manifest = model['weightsManifest']
    # If flatten=False, returns a list of groups equal to the number of .bin files.
    # Use flatten=True to convert to a single group
    group = decode_weights(manifest, weights, flatten=True)
    # Convert dicts in tfjs group format into pytorch's state_dict format:
    # {name: str, data: ndarray} -> {name: tensor}
    state_dict = {d['name']: torch.from_numpy(d['data']) for d in group}
    return state_dict

def convert2bin(state_dict: Dict[str: np.ndarray], model: Dict, directory='./'):
    # convert state_dict to groups (list of 1 group)
    groups = [[{'name': key, 'data': value} for key, value in state_dict.items()]]
    # this library function will write to .bin file[s], but you can read it back
    # or change the function internals my copying them from source
    write_weights(groups, directory, write_manifest=False)
