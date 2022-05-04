# python viz_label.py
import os
import imageio
import numpy as np

#%% color scheme
# color palette for nyu13 & nyu40 labels
def create_color_palette_old(dataset='nyu13'):
    if dataset == 'nyu13':
        return (
            np.array(
                [
                    [0, 0, 0],
                    [0, 0, 1],  # BED
                    [0.9137, 0.3490, 0.1882],  # BOOKS
                    [0, 0.8549, 0],  # CEILING
                    [0.5843, 0, 0.9412],  # CHAIR
                    [0.8706, 0.9451, 0.0941],  # FLOOR
                    [1.0000, 0.8078, 0.8078],  # FURNITURE
                    [0, 0.8784, 0.8980],  # OBJECTS
                    [0.4157, 0.5333, 0.8000],  # PAINTING
                    [0.4588, 0.1137, 0.1608],  # SOFA
                    [0.9412, 0.1373, 0.9216],  # TABLE
                    [0, 0.6549, 0.6118],  # TV
                    [0.9765, 0.5451, 0],  # WALL
                    [0.8824, 0.8980, 0.7608],
                ]
            )
            * 255
        ).astype(np.uint8)
    elif dataset == 'nyu40':
        return [
            (0, 0, 0),
            (174, 199, 232),  # wall
            (152, 223, 138),  # floor
            (31, 119, 180),  # cabinet
            (255, 187, 120),  # bed
            (188, 189, 34),  # chair
            (140, 86, 75),  # sofa
            (255, 152, 150),  # table
            (214, 39, 40),  # door
            (197, 176, 213),  # window
            (148, 103, 189),  # bookshelf
            (196, 156, 148),  # picture
            (23, 190, 207),  # counter
            (178, 76, 76),
            (247, 182, 210),  # desk
            (66, 188, 102),
            (219, 219, 141),  # curtain
            (140, 57, 197),
            (202, 185, 52),
            (51, 176, 203),
            (200, 54, 131),
            (92, 193, 61),
            (78, 71, 183),
            (172, 114, 82),
            (255, 127, 14),  # refrigerator
            (91, 163, 138),
            (153, 98, 156),
            (140, 153, 101),
            (158, 218, 229),  # shower curtain
            (100, 125, 154),
            (178, 127, 135),
            (120, 185, 128),
            (146, 111, 194),
            (44, 160, 44),  # toilet
            (112, 128, 144),  # sink
            (96, 207, 209),
            (227, 119, 194),  # bathtub
            (213, 92, 176),
            (94, 106, 211),
            (82, 84, 163),  # otherfurn
            (100, 85, 144),
        ]


def create_color_palette(dataset='nyu13'):
    if dataset == 'nyu13':
        return (
            np.array(
                [
                    [0, 0, 0],
                    [0.9765, 0.5451, 0],  # WALL
                    [0.8706, 0.9451, 0.0941],  # FLOOR
                    [0.8706, 0.9451, 0.0941],  # CABINET (TODO)
                    [0, 0, 1],  # BED
                    [0.5843, 0, 0.9412],  # CHAIR
                    [0.4588, 0.1137, 0.1608],  # SOFA
                    [0.9412, 0.1373, 0.9216],  # TABLE
                    # DOOR (TODO)
                    # WINDOW (TODO)
                    # BOOKSELF (TODO)
                    [0.4157, 0.5333, 0.8000],  # PAINTING
                    [0.9137, 0.3490, 0.1882],  # BOOKS
                    [0, 0.8549, 0],  # CEILING
                    [1.0000, 0.8078, 0.8078],  # FURNITURE
                    [0, 0.8784, 0.8980],  # OBJECTS
                    [0, 0.6549, 0.6118],  # TV
                    [0.8824, 0.8980, 0.7608],
                ]
            )
            * 255
        ).astype(np.uint8)
    elif dataset == 'nyu40':
        return (
            np.array(
                [
                    [0, 0, 0],
                    [0, 0, 1],  # BED
                    [0.9137, 0.3490, 0.1882],  # BOOKS
                    [0, 0.8549, 0],  # CEILING
                    [0.5843, 0, 0.9412],  # CHAIR
                    [0.8706, 0.9451, 0.0941],  # FLOOR
                    [1.0000, 0.8078, 0.8078],  # FURNITURE
                    [0, 0.8784, 0.8980],  # OBJECTS
                    [0.4157, 0.5333, 0.8000],  # PAINTING
                    [0.4588, 0.1137, 0.1608],  # SOFA
                    [0.9412, 0.1373, 0.9216],  # TABLE
                    [0, 0.6549, 0.6118],  # TV
                    [0.9765, 0.5451, 0],  # WALL
                    [0.8824, 0.8980, 0.7608],
                ]
            )
            * 255
        ).astype(np.uint8)


#%% viz code


def visualize_label_image(filename, image, dataset='nyu13'):
    height = image.shape[0]
    width = image.shape[1]
    vis_image = np.zeros([height, width, 3], dtype=np.uint8)
    color_palette = create_color_palette(dataset=dataset)
    for idx, color in enumerate(color_palette):
        vis_image[image == idx] = color
    imageio.imwrite(filename, vis_image)


def main():
    dataset = 'nyu40'
    prefix = dataset + '_viz_lbl_'
    curr_dir_path = os.path.dirname(os.path.abspath(__file__))
    lbl_filename = "002300.png"
    lbl_filepath = os.path.join(curr_dir_path, lbl_filename)
    image = imageio.imread(lbl_filepath)
    viz_filepath = os.path.join(curr_dir_path, prefix + lbl_filename)
    visualize_label_image(viz_filepath, image, dataset)


if __name__ == "__main__":
    main()
