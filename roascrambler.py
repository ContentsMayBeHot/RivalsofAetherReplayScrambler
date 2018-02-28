import os
import sys
import datetime as dt

REPLAYS_DNAME = 'replays'
OUTPUT_DNAME = 'scrambled'

def main():
    if not os.path.isdir(REPLAYS_DNAME):
        os.mkdir(REPLAYS_DNAME)
    if not os.path.isdir(OUTPUT_DNAME):
        os.mkdir(OUTPUT_DNAME)
    
    args = sys.argv
    if len(args) < 2:
        return
    for fname in args[1:]:
        # Get input data
        input_path = os.path.join(REPLAYS_DNAME, fname)
        with open(input_path, 'r') as fin:
            output_path = os.path.join(OUTPUT_DNAME, fname)
            with open(output_path, 'w+') as fout:
                # Metadata
                now = dt.datetime.now()
                ln = fin.readline()
                t1 = now.strftime('%H%M%S%d%m%Y')
                t2 = now.strftime('REPLAY %Y-%m-%d ')
                t3 = now.strftime('(%H:%M)')
                version = ln[1:7]
                meta = '0' + version + t1 + t2 + t3
                pos = len(meta)
                meta += ln[pos:]
                fout.write(meta)

                ln = fin.readline()
                fout.write(ln)


if __name__ == '__main__':
    main()
