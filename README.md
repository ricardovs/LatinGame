# Latin Game

![GitHub repo size](https://img.shields.io/github/repo-size/ricardovs/LatinGame?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/ricardovs/LatinGame?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/ricardovs/LatinGame?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/ricardovs/LatinGame?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/ricardovs/LatinGame?style=for-the-badge)

Remember latin cases' endings !! Under development beta version !!

## Philosophy
Some things to clarify:
- Latin does not have accents. The macron and the breve are guides to pronuntiation, so they are not part of this dataset.
- We go after the rule, not the exception, so:
    - The 1st declension words can be masculine or feminine, but the feminine compresses the majority, so you will only be asked about them as feminine. This may change, but it has not yet.
    - The 3rd declension Nominative will never be asked (you should know why).

## Task list and issues
```[tasklist]
- [x] Add 1st declension to dataset
- [ ] Add 2nd declension to dataset
- [ ] Add 3rd declension to dataset
- [ ] Add 4th declension to dataset
- [ ] Add 5th declension to dataset
- [ ] Chart showing the case endings that were added
- [ ] Add report page
- [ ] Add configuration page
```

## Running and Playing
The game was developed to run on a Linux distro. Keep in mind.

1. Start virtual environment
```
$ make venv
$ source ./venv/bin/activate
```
2. Install dependencies
```
$ make depends
```
3. Run the app.
You can use `make run` or simply the `make` command.
```
$ make
```

## Leaving the game

1. Desactivate the environment
```
$ deactivate
```

2. Cleaning
```
make clear
```

## 📝 License
Code released under the MIT License. More details on [LICENSE](LICENSE).
