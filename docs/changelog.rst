Change Log
==========


v0.5.0 [2022-07-06]
^^^^^^^^^^^^^^^^^^^

* Fix logging
* Add --engine-name option


v0.4.2 [2022-07-03]
^^^^^^^^^^^^^^^^^^^

* Add logging by process id with islogging flag.

::
   tagasuri epd-test --input-file 7men_human.epd --islogging ...


v0.4.1 [2022-07-03]
^^^^^^^^^^^^^^^^^^^

* Disable file logging.


v0.4.0 [2022-07-03]
^^^^^^^^^^^^^^^^^^^

Save unsolved puzzle to text file.


v0.3.0 [2022-07-02]
^^^^^^^^^^^^^^^^^^^

Supports parallel engine testing with ``--workers`` option

tagasuri epd-test --input-file 7men_human.epd --engine-file stockfish_15_modern.exe --engine-options "{'Hash': 256, 'Threads': 1}" --move-time 5 --workers 4 --output-file 7men.txt


v0.2.0 [2022-07-02]
^^^^^^^^^^^^^^^^^^^

1. Add command line options

tagasuri epd-test --input-file eret.epd --engine-file stockfish_15_modern.exe --engine-options "{'Hash': 256, 'Threads': 1}" --move-time 5 --output-file eret.txt
tagasuri epd-test --input-file eret.epd --engine-file cheng4_x64.exe --move-time 5 --output-file eret.txt
tagasuri epd-test --input-file eret.epd --engine-file CT800_V1.43_x64.exe --move-time 5 --output-file eret.txt
tagasuri epd-test --input-file eret.epd --engine-file cdrill_1800.exe --move-time 5 --output-file eret.txt

Output eret.txt::

                 Name  Total  Correct   Pct  Time  EPDFile
         Stockfish 15    111       90 81.08   5.0 eret.epd
          CDrill 1800    111       16 14.41   5.0 eret.epd
           Cheng 4.40    111       16 14.41   5.0 eret.epd
   CT800 V1.43 64 bit    111       10  9.01   5.0 eret.epd
