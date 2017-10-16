"""Basic source file plagiarism detection via pairwise document similarity."""

import difflib
import sys

HITS = []
RATS = []

def comp(a, b):
    """Computes the textual similarity of two files."""
    afile = open(a)
    atext = afile.read()
    afile.close()
    bfile = open(b)
    btext = bfile.read()
    bfile.close()
    skip = None  # lambda x: x in " \t\r\n"
    sm = difflib.SequenceMatcher(skip, atext, btext)
    r = sm.ratio()
    if r > 0.85:
        HITS.append([r, a, b, str(len(atext)), str(len(btext))])
    RATS.append(r)

def main(files):
    """Compares each pair of files in the given paths."""
    nfile = len(files)
    print "Comparing %d files..." % nfile
    for i in range(0, nfile):
        for j in range(i+1, nfile):
            comp(files[i], files[j])
    # output the similarity ratios
    RATS.sort()
    print "Average similarity:", sum(RATS) / len(RATS)
    print " Median similarity:", RATS[len(RATS) / 2]
    print
    #~ data = open("RATS.csv", "w")
    #~ data.write("ratio\n")
    #~ data.writelines([str(ra) + '\n' for ra in RATS])
    #~ data.close()
    # output the potential matches
    for hit in sorted(HITS, reverse=True):
        hit[0] = format(hit[0], '.3f')
        print '\t'.join(hit)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python cheat.py */*.java"
    else:
        main(sys.argv[1:])
