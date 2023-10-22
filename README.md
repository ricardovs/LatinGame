# Latin Game

![GitHub repo size](https://img.shields.io/github/repo-size/ricardovs/LatinGame?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/ricardovs/LatinGame?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/ricardovs/LatinGame?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/ricardovs/LatinGame?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/ricardovs/LatinGame?style=for-the-badge)

Remember latin cases' endings !! Under development beta version !!

<table style="text-align:center;">
<thead>
  <tr style="text-align:center;">
    <th colspan="2"></th>
    <th>1st <br>Declension</th>
    <th colspan="2">2nd <br>Declension</th>
    <th colspan="2">3rd <br>Declension</th>
    <th colspan="2">4th <br>Declension</th>
    <th>5th <br>Declension</th>
  </tr>
</thead>
<tbody style="border-bottom:1px solid;">
  <tr>
    <td colspan="2"></td>
    <td>F</td>
    <td>M</td>
    <td>N</td>
    <td>M/F</td>
    <td>N</td>
    <td>M</td>
    <td>N</td>
    <td>F</td>
  </tr>
  <tr>
    <td rowspan="6">SIN</td>
    <td>VOC</td>
    <td>a</td>
    <td>us</td>
    <td>um</td>
    <td>--</td>
    <td>--</td>
    <td>us</td>
    <td>&umacr;</td>
    <td>&emacr;s</td>
  </tr>
  <tr>
    <td>NOM</td>
    <td>a</td>
    <td>us</td>
    <td>um</td>
    <td>--</td>
    <td>--</td>
    <td>us</td>
    <td>&umacr;</td>
    <td>&emacr;s</td>
  </tr>
  <tr>
    <td>GEN</td>
    <td>ae</td>
    <td>&imacr;</td>
    <td>&imacr;</td>
    <td>is</td>
    <td>is</td>
    <td>&umacr;s</td>
    <td>&umacr;s</td>
    <td>&emacr;&imacr;/e</td>
  </tr>
  <tr>
    <td>DAT</td>
    <td>ae</td>
    <td>&omacr;</td>
    <td>&omacr;</td>
    <td>&imacr;</td>
    <td>&imacr;</td>
    <td>u&imacr;/&umacr;</td>
    <td>&umacr;</td>
    <td>&emacr;&imacr;/e</td>
  </tr>
  <tr>
    <td>ABL</td>
    <td>&amacr;</td>
    <td>&omacr;</td>
    <td>&omacr;</td>
    <td>e/&imacr;</td>
    <td>e/&imacr;</td>
    <td>&umacr;</td>
    <td>&umacr;</td>
    <td>&emacr;</td>
  </tr>
  <tr>
    <td>ACC</td>
    <td>am</td>
    <td>um</td>
    <td>um</td>
    <td>em/im</td>
    <td>--</td>
    <td>um</td>
    <td>&umacr;</td>
    <td>em</td>
  </tr>
  <tr>
    <td rowspan="6">PLU</td>
    <td>VOC</td>
    <td>ae</td>
    <td>&imacr;</td>
    <td>a</td>
    <td>&emacr;s</td>
    <td>a/ia</td>
    <td>&umacr;s</td>
    <td>ua</td>
    <td>&emacr;s</td>
  </tr>
  <tr>
    <td>NOM</td>
    <td>ae</td>
    <td>&imacr;</td>
    <td>a</td>
    <td>&emacr;s</td>
    <td>a/ia</td>
    <td>&umacr;s</td>
    <td>ua</td>
    <td>&emacr;s</td>
  </tr>
  <tr>
    <td>GEN</td>
    <td>&amacr;rum</td>
    <td>&omacr;rum</td>
    <td>&omacr;rum</td>
    <td>um/ium</td>
    <td>um/ium</td>
    <td>uum</td>
    <td>uum</td>
    <td>&emacr;rum</td>
  </tr>
  <tr>
    <td>DAT</td>
    <td>&imacr;s/abus</td>
    <td>&imacr;s</td>
    <td>&imacr;s</td>
    <td>ibus</td>
    <td>ibus</td>
    <td>ibus/ubus</td>
    <td>ibus/ubus</td>
    <td>&emacr;bus</td>
  </tr>
  <tr>
    <td>ABL</td>
    <td>&imacr;s/abus</td>
    <td>&imacr;s</td>
    <td>&imacr;s</td>
    <td>ibus</td>
    <td>ibus</td>
    <td>ibus/ubus</td>
    <td>ibus/ubus</td>
    <td>&emacr;bus</td>
  </tr>
  <tr>
    <td>ACC</td>
    <td>&amacr;s</td>
    <td>&omacr;s</td>
    <td>a</td>
    <td>&emacr;s/&imacr;s</td>
    <td>a/ia</td>
    <td>&umacr;s</td>
    <td>ua</td>
    <td>&emacr;s</td>
  </tr>
</tbody>
</table>

## Task list and issues
```[tasklist]
- [x] Add 1st declension to dataset
- [ ] Add 2nd declension to dataset
- [ ] Add 3rd declension to dataset
- [ ] Add 4th declension to dataset
- [ ] Add 5th declension to dataset
- [x] Table showing the case endings
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
