# Jaro-Winkler similarity (distance) in Python

This script computes the [Jaro-Winkler distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) of two words with a simple script in [Python 3](https://www.python.org/).

Run it with `python3 distances.py [word1] [word2]`:

```sh
$ python3 distances.py word1 word2
word1: word1
word2: word2
Jaro distance: 0.825
Jaro-Winkler distance: 0.895
```

```sh
$ python3 distances.py words wodrs
word1: words
word2: wodrs
Jaro distance: 0.9333333333333332
Jaro-Winkler distance: 0.9466666666666665
```