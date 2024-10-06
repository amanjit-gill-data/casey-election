# Technical Notes

## wget to download questionnaires

reference: https://unix.stackexchange.com/questions/700709/how-to-download-all-pdf-files-linked-from-a-single-page-using-wget

```
wget -r -l1 -H -nd -np -A.pdf "https://vec.vic.gov.au/voting/2024-local-council-elections/casey-city-council/nominations.html"
```

meanings of all the options:

```
-r          recursive download
-l1         only one level deep (i.e. only files directly linked from this page)
-H          span hosts (follow links to other hosts)
-nd         don't create a dir structure; download files into current dir
-np         don't follow links to parent directories
-A.pdf      accept only .pdf files
```

could also have added the following, to prevent anti-DOS measures:

```
wait=2          Wait 2 seconds between each retrieval
random-wait     Wait from 0.5 to 1.5 * --wait seconds between retrievals
limit-rate=20k  Limit the download rate to 20 kilobytes per second
```

## reminders 

manually add non-respondents to all-candidates-sorted.csv 
- before converting to all-candidates-sorted.tsv, splitting by ward, etc
