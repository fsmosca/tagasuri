# Tagasuri
An application that will test a computer chess program on epd test suites.

## Installation
`pip install tagasuri`

## Dependencies
Tagasuri is dependent on the following packages:

1. python chess
2. pandas
3. pretty-html-table

They are installed automatically when tagasuri is installed.


## Command line

Test the engine with a chess puzzle in epd file.

```
tagasuri epd-test --input-file "7men_human.epd" --engine-file "c:/engines/sf15.exe" --engine-options "{'Hash': 128, 'Threads': 1}" --workers 1 --move-time 1 --output-file 7men.txt
```

Sample output

```
                       Name  Total  Correct   Pct  Time        EPDFile
               Stockfish 15   1110     1103 99.37   1.0 7men_human.epd
Lc0 v0.29.0-dev+git.025105e   1110     1096 98.74   1.0 7men_human.epd
      Komodo 12.1.1 64-bit    1110     1064 95.86   1.0 7men_human.epd
                 Texel 1.07   1110     1045 94.14   1.0 7men_human.epd
                 Cheng 4.40   1110     1042 93.87   1.0 7men_human.epd
         CT800 V1.43 64 bit   1110     1023 92.16   1.0 7men_human.epd
                CDrill 1800   1110      899 80.99   1.0 7men_human.epd
```

If your processor has a quad or 4 cores, you can increase the workers to 3 with `--workers 3` for example to finish the test early. If you use Lc0 with GPU and your system has only 1 GPU just use `--workers 1`.

## Access help

`tagasuri -h`

`tagasuri epd-test -h`

## Credits
* [Python chess](https://python-chess.readthedocs.io/en/latest/)
* [Pandas](https://pandas.pydata.org/)
* [pretty-html-table](https://pypi.org/project/pretty-html-table/)

