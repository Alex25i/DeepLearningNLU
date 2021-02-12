import json
import os
from json.decoder import JSONDecodeError


def load_json(file):
    try:
        data = json.loads(open(file, encoding='utf-8').read())
    except JSONDecodeError:
        raise (
            BaseException("Error while parsing file \"" + file + "\". See JSONDecodeError above for details."))
    return data


def write_json(data: dict, path: str):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def find_class_labels(training_data):
    labels = set()
    dataset_size = len(training_data)
    for i in range(dataset_size):
        label = training_data[str(i)]['intent']
        labels.add(label)
    return labels


def find_slot_labels(training_data, _class_labels):
    dataset_size = len(training_data)
    _slot_labels = {}
    for class_label in _class_labels:
        _slot_labels[class_label] = set()

    for i in range(dataset_size):
        labels = training_data[str(i)]['slots']
        class_label = training_data[str(i)]['intent']
        for label in labels.keys():
            _slot_labels[str(class_label)].add(str(label))
    return _slot_labels


def split_data(data, split_ratio):
    data_size = len(data)
    samples1 = int(round(data_size * split_ratio))
    samples2 = data_size - samples1

    split1 = {}
    split2 = {}
    for i in range(samples1):
        split1[str(i)] = data[str(i)]

    for i in range(samples2):
        split2[str(i)] = data[str(i + samples1)]

    return split1, split2


if __name__ == '__main__':
    train = load_json(os.path.join("data", "orig", "train.json"))
    # class_labels = find_class_labels(train)
    # slot_labels = find_slot_labels(train, class_labels)
    # pprint(class_labels)
    # pprint(slot_labels)
    train, dev = split_data(train, 0.8)
    write_json(train, os.path.join("data", "train.json"))
    write_json(train, os.path.join("data", "dev.json"))
