from tagasuri.epd import EpdTest


def epd_test(
        enginepath, inputfile, outputfile, masterfile: str = 'master.csv',
        movetime: float = 1.0, engineoptions: str = None):

    a = EpdTest(
        enginepath, inputfile, outputfile, masterfile=masterfile,
        movetime=movetime, engineoptions=engineoptions)

    df = a.run()
    a.save_to_master(df)
    dfs = a.get_summary()
    dfs.columns = ['Name', 'Total', 'Correct', 'Pct', 'Time', 'EPDFile']
    dfs = dfs.sort_values(by=['Correct'], ascending=[False])
    a.save_output(dfs, outputfile)