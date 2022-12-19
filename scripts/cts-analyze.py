#!/usr/bin/python3
# SPDX-License-Identifier: CC-BY-4.0
# Copyright Contributors to the ODPi Egeria project.

import json
import tarfile
import sys

basedir = '.'
workdir = basedir + '/work'

# unpack reportFile
reportFile = tarfile.open(basedir + '/export/cts.tar.gz')
reportFile.extractall(workdir)
reportFile.close()

# unpack detailed result file
pdfile = tarfile.open(workdir + '/pd.tar.gz')
pdfile.extractall(workdir)
pdfile.close()

# Load the profile results
with open(workdir + '/openmetadata_cts_summary.json') as f:
    summary = json.load(f)

totalGood = 0
totalBad = 0

# Assume standard CTS
profileSummaries = summary['testLabSummary']['testSummariesFromWorkbenches'][0]['profileSummaries']

for p in profileSummaries:
    # print(p);
    name = p['name']
    priority = p['profilePriority']
    conformanceStatus = p['conformanceStatus']

    # Capture any errors
    fname = name.replace(" ", "_")
    with open(workdir + '/profile-details/' + fname + '.json') as f:
        details = json.load(f)
        good = 0
        bad = 0
        try:
            results = details['profileResult']['requirementResults']
            for r in results:
                try:
                    good += len(r.get('positiveTestEvidence'))
                # if empty list - ie all good
                except Exception:
                    pass
                try:
                    bad += len(r.get('negativeTestEvidence'))
                # if empty list - ie no fails
                except Exception:
                    pass
        # If this function isn't supported at all
        except Exception:
            pass
    totalGood += good
    totalBad += bad

    print("%30s %17s %26s [ %6i / %6i ]" % (name, priority, conformanceStatus, good, bad))

if totalBad == 0:
    print("\nPASS [%i/%i]" % (totalGood, totalBad))
else:
    print("\nFAIL [%i/%i]" % (totalGood, totalBad))

sys.exit(totalBad != 0)
