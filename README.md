# DeepLearningNLU
Coding Task NUL for the course "Deep learning for speech &amp; language processing" WS 20/21

## Notes on Coding Tasks

* data will be published on Dec 1st, 2020 at 12am on the excercise webpage
* you will get 2 files: one for training (contains labels), one for evaluation (does not contain labels)
* for evaluation, upload your predictions in the same format as the download 
    * each data sample in a file has a unique id
        * upload only the data sample id and your predicted label
        * don't upload the input data (there is a size limit for each upload)
* format: JSON
    * python has built-in functionallity to read / write JSON
    * if you never used it (with python), there is a short overview: https://realpython.com/python-json/

### NLU train data
```
{
    "0": {
        "intent": "AddToPlaylist",
        "text": "Add a tune to my elrow Guest List",
        "slots": {
            "music_item": "tune",
            "playlist_owner": "my",
            "playlist": "elrow Guest List"
        },
        "positions": {
            "music_item": [
                6,
                9
            ],
            "playlist_owner": [
                14,
                15
            ],
            "playlist": [
                17,
                32
            ]
        }
    },
    "1": {
        "intent": "AddToPlaylist",
        "text": "Add a guy is a guy to the infinite indie folk playlist.",
        "slots": {
            "entity_name": "a guy is a guy",
            "playlist": "infinite indie folk"
        },
        "positions": {
            "entity_name": [
                4,
                17
            ],
            "playlist": [
                26,
                44
            ]
        }
    },
...
```
___
Upload your predictions without "text" and "position" fields!

###Emotion train data
features-entry contains a list of a list with 26 items.

length of inner list: 26 (float numbers - represent one preprocessed speech frame (logMel))
length of outer list: number of frames per data-point, e.g. 10 or 15, ...
for easy parsing into an array, have a look at e.g. https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.fromstring.html
```
{"0": {"valence": 0, 
       "activation": 1,
       "features": [[5.502810676891276, 5.389630715979907, 5.89079939835461, 5.462222408074205, 5.482823967430299, 6.776999420417389, 7.500191549370183, 8.304382413190043, 8.01058604345238, 6.033706406358724, 7.067212416470815, 6.4463667723745965, 6.923879604046541, 8.091544891207468, 7.972158444902915, 7.641215050710871, 7.1507373690379525, 7.507756141316357, 7.074741477204279, 7.992954055443716, 7.576059013864094, 7.7207549746760975, 8.649263126832178, 8.220149828892483, 6.811228837696475, 6.457873509412178], [...], ...]
       },
 "1: "valence": 1, 
       "activation": 1,
       "features": [[3.502810676891276, 5.389630715979907, 5.89079939835461, 5.462222408074205, 5.482823967430299, 6.776999420417389, 7.500191549370183, 8.304382413190043, 8.01058604345238, 6.033706406358724, 7.067212416470815, 6.4463667723745965, 2.923879604046541, 8.091544891207468, 7.972158444902915, 7.641215050710871, 7.1507373690379525, 7.507756141316357, 7.074741477204279, 7.992954055443716, 7.576059013864094, 7.7207549746760975, 8.649263126832178, 8.220149828892483, 6.811228837696475, 6.457873509412178], [...], ...]
       },
       ...
```
Upload your predictions without "features" fields!