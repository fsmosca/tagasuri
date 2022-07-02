Change Log
==========

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