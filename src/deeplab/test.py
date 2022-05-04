import os
import argparse

import torch
import torchvision

def main(args):
    model = torchvision.models.segmentation.deeplabv3_resnet101(
        pretrained=False,
        pretrained_backbone=False,
        progress=True,
        num_classes=40,
        aux_loss=None)
    ckpt_path = os.path.join(args.base, args.resume)
    checkpoint = torch.load(ckpt_path)
    # remove any aux classifier stuff
    removekeys = [
        key for key in checkpoint.keys() if key.startswith('aux_classifier')
    ]
    for key in removekeys:
        del checkpoint[key]
    model.load_state_dict(checkpoint, strict=True)
    model.to('cuda')
    model.eval()

    # make a prediction
    logits = model(image)['out']
    _, prediction = torch.max(logits, 1)

if __name__ == "__main__":
    curr_dir_path = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(description='Deeplab test')
    parser.add_argument('--base', default=curr_dir_path, help='base path folder')
    parser.add_argument('--resume', default='2987_deeplab_scannet_best.pth', help='resume from checkpoint')
    args = parser.parse_args()
    main(args)
