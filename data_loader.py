import json
import os
from json.decoder import JSONDecodeError
from pprint import pprint


def open_json(file):
    try:
        data = json.loads(open(file, encoding='utf-8').read())
    except JSONDecodeError:
        raise (
            BaseException("Error while parsing file \"" + file + "\". See JSONDecodeError above for details."))
    return data


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


if __name__ == '__main__':
    train = open_json(os.path.join("data", "train.json"))
    class_labels = find_class_labels(train)
    slot_labels = find_slot_labels(train, class_labels)
    pprint(slot_labels)
