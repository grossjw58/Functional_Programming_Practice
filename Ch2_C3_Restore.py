'''
Complete the restore_documents function in one line. It takes two tuples of document strings, originals and backups, as input and returns a set.

Convert all documents to the same case with .upper() for comparison.
Filter out documents that are corrupted strings of random numbers with .isdigit().
Return the combined originals and backups documents with any duplicates removed using a set.
'''

def restore_documents(originals: tuple[str], backups: tuple[str]) -> set[str]:
    return(set(filter(lambda doc: not doc.isdigit(),(map(lambda doc: doc.upper(),originals + backups)))))
